#!/usr/bin/env python3
"""Finite validation of the fermionic configuration model and conventions.

Run from any directory; the default report is verification/results.json.
The analytic proofs establish universal statements. Random finite screens here
only look for convention errors and counterexamples in the sampled instances.
"""

from __future__ import annotations

import argparse
import json
import platform
from itertools import combinations
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm


SEED = 20261031
MATRIX_TOL = 1e-12
SCREEN_TOL = 2e-11
CHECK_COUNT = 0


def require(condition: bool, description: str) -> None:
    """Keep checks active even if Python is invoked with optimization flags."""
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(description)


def annihilator(modes: int, mode: int) -> np.ndarray:
    """Ordered Fock convention; mode 0 is the most significant bit."""
    out = np.zeros((2**modes, 2**modes), dtype=complex)
    for label in range(2**modes):
        bits = [(label >> (modes - 1 - j)) & 1 for j in range(modes)]
        if bits[mode]:
            target = label ^ (1 << (modes - 1 - mode))
            out[target, label] = (-1) ** sum(bits[:mode])
    return out


def occupation(bits: str) -> np.ndarray:
    state = np.zeros(2 ** len(bits), dtype=complex)
    state[int(bits, 2)] = 1
    return state


def binary_entropy(probability: float) -> float:
    if probability in (0.0, 1.0):
        return 0.0
    return float(
        -probability * np.log(probability)
        - (1 - probability) * np.log1p(-probability)
    )


def binary_relative_entropy(left: float, right: float) -> float:
    first = 0.0 if left == 0 else left * np.log(left / right)
    second = 0.0 if left == 1 else (1 - left) * np.log((1 - left) / (1 - right))
    return float(first + second)


def apply_adjacent_gate(
    state: np.ndarray, gate: np.ndarray, site: int, modes: int
) -> np.ndarray:
    shaped = state.reshape((2**site, 4, 2 ** (modes - site - 2)))
    return np.einsum("ab,ibj->iaj", gate, shaped).reshape(-1)


def apply_single_gate(
    state: np.ndarray, gate: np.ndarray, site: int, modes: int
) -> np.ndarray:
    shaped = state.reshape((2**site, 2, 2 ** (modes - site - 1)))
    return np.einsum("ab,ibj->iaj", gate, shaped).reshape(-1)


def apply_cnot(state: np.ndarray, control: int, target: int, modes: int) -> np.ndarray:
    result = np.zeros_like(state)
    for label, amplitude in enumerate(state):
        destination = label
        if (label >> (modes - 1 - control)) & 1:
            destination ^= 1 << (modes - 1 - target)
        result[destination] = amplitude
    return result


def apply_block_operator(
    state: np.ndarray, operator: np.ndarray, block: int, blocks: int
) -> np.ndarray:
    shaped = state.reshape((16**block, 16, 16 ** (blocks - block - 1)))
    return np.einsum("ab,ibj->iaj", operator, shaped).reshape(-1)


def random_su2(rng: np.random.Generator) -> np.ndarray:
    axis = rng.normal(size=3)
    axis /= np.linalg.norm(axis)
    angle = rng.uniform(-np.pi, np.pi)
    axis_pauli = np.array(
        [[axis[2], axis[0] - 1j * axis[1]],
         [axis[0] + 1j * axis[1], -axis[2]]]
    )
    return np.cos(angle) * np.eye(2) - 1j * np.sin(angle) * axis_pauli


def random_gaussian_state(modes: int, rng: np.random.Generator) -> np.ndarray:
    """A random Fock vector followed by nearest-neighbor matchgates.

    Both parity sectors are sampled. The two 2x2 blocks have determinant one,
    so each gate is a parity-preserving Gaussian matchgate. This distribution
    is not asserted to be Haar measure on the Gaussian manifold.
    """
    state = np.zeros(2**modes, dtype=complex)
    state[int(rng.integers(2**modes))] = 1
    for _ in range(12 * modes):
        site = int(rng.integers(modes - 1))
        gate = np.zeros((4, 4), dtype=complex)
        gate[np.ix_([0, 3], [0, 3])] = random_su2(rng)
        gate[np.ix_([1, 2], [1, 2])] = random_su2(rng)
        state = apply_adjacent_gate(state, gate, site, modes)
    return state


def check_local_model() -> tuple[dict, dict]:
    identity = np.eye(16)
    operators = [annihilator(4, j) for j in range(4)]
    numbers = [a.conj().T @ a for a in operators]
    number = sum(numbers)
    transfer = operators[0].conj().T @ operators[1].conj().T @ operators[3] @ operators[2]
    pair_hop = transfer + transfer.conj().T
    penalty = number - 2 * identity
    hamiltonian = identity - pair_hop + penalty @ penalty
    expanded = 5 * identity - 3 * number - pair_hop
    for i, j in combinations(range(4), 2):
        expanded += 2 * numbers[i] @ numbers[j]
    target = (occupation("1100") + occupation("0011")) / np.sqrt(2)
    projector = np.outer(target, target.conj())
    defect = identity - projector
    gaussian = (
        (operators[0].conj().T + operators[2].conj().T)
        @ (operators[1].conj().T + operators[3].conj().T)
        @ occupation("0000") / 2
    )

    car_residual = 0.0
    for i, a in enumerate(operators):
        for j, b in enumerate(operators):
            car_residual = max(
                car_residual,
                float(np.linalg.norm(a @ b + b @ a)),
                float(np.linalg.norm(a @ b.conj().T + b.conj().T @ a - (i == j) * identity)),
            )
    require(car_residual < MATRIX_TOL, "Canonical anticommutation relations")
    require(np.linalg.norm(hamiltonian - expanded) < MATRIX_TOL, "Two-body expansion")
    require(np.linalg.norm(transfer @ occupation("0011") - occupation("1100")) < MATRIX_TOL,
            "Pair-transfer fermionic sign")
    spectrum = np.linalg.eigvalsh(hamiltonian)
    require(np.allclose(spectrum, [0] + [1] * 4 + [2] * 9 + [5] * 2, atol=MATRIX_TOL, rtol=0),
            "Complete block spectrum")
    require(np.linalg.norm(hamiltonian @ target) < MATRIX_TOL, "Target energy zero")
    min_comparison = float(np.linalg.eigvalsh(hamiltonian - defect).min())
    require(min_comparison > -MATRIX_TOL, "h dominates the defect projector")
    require(np.linalg.norm(hamiltonian @ number - number @ hamiltonian) < MATRIX_TOL,
            "Particle-number conservation")
    require(np.linalg.norm(hamiltonian @ defect - defect @ hamiltonian) < MATRIX_TOL,
            "h and the defect commute")
    gaussian_energy = float(np.vdot(gaussian, hamiltonian @ gaussian).real)
    require(abs(gaussian_energy - 0.5) < MATRIX_TOL, "Explicit Gaussian energy saturator")
    require(abs(np.vdot(gaussian, gaussian).real - 1) < MATRIX_TOL, "Gaussian normalization")
    require(abs(abs(np.vdot(gaussian, target)) ** 2 - 0.5) < MATRIX_TOL,
            "Explicit Gaussian fidelity saturator")

    # Exact FLO equivalence W=-i gamma_1 gamma_4, with the primary-source GHZ sign.
    ghz = (occupation("0000") + occupation("1111")) / np.sqrt(2)
    gamma1 = operators[0] + operators[0].conj().T
    gamma4 = 1j * (operators[1].conj().T - operators[1])
    gaussian_map = -1j * gamma1 @ gamma4
    map_error = float(np.linalg.norm(gaussian_map @ ghz - target))
    require(map_error < MATRIX_TOL, "Exact Gaussian equivalence and phase")
    require(np.linalg.norm(gaussian_map.conj().T @ gaussian_map - identity) < MATRIX_TOL,
            "Gaussian equivalence is unitary")

    # Exact number-conserving preparation; the sign of the exponent is tested.
    pair_y = 1j * (transfer.conj().T - transfer)
    pair_unitary = expm(-1j * np.pi / 4 * pair_y)
    pair_preparation_error = float(np.linalg.norm(pair_unitary @ occupation("1100") - target))
    require(pair_preparation_error < MATRIX_TOL, "Number-conserving preparation sign")
    require(np.linalg.norm(pair_unitary @ number - number @ pair_unitary) < MATRIX_TOL,
            "Preparation conserves particle number")

    # The inverse preparation is the trusted h-eigenbasis measurement circuit.
    measurement_unitary = pair_unitary.conj().T
    measured_h = measurement_unitary @ hamiltonian @ measurement_unitary.conj().T
    assigned_energies = np.array([1 + (label.bit_count() - 2) ** 2 for label in range(16)], dtype=float)
    assigned_energies[int("1100", 2)] = 0
    assigned_energies[int("0011", 2)] = 2
    measurement_residual = float(np.linalg.norm(measured_h - np.diag(assigned_energies)))
    require(measurement_residual < MATRIX_TOL, "Local eigenbasis measurement and energy labels")
    antisymmetric = (occupation("1100") - occupation("0011")) / np.sqrt(2)
    require(np.linalg.norm(measurement_unitary @ antisymmetric + occupation("0011")) < MATRIX_TOL,
            "Antisymmetric eigenvector measurement phase")

    # Exact six-gate Clifford preparation in the occupation encoding.
    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    clifford_state = apply_single_gate(occupation("0000"), hadamard, 0, 4)
    for target_mode in [1, 2, 3]:
        clifford_state = apply_cnot(clifford_state, 0, target_mode, 4)
    for site in [0, 1]:
        clifford_state = apply_single_gate(clifford_state, pauli_x, site, 4)
    clifford_error = float(np.linalg.norm(clifford_state - target))
    require(clifford_error < MATRIX_TOL, "Exact Clifford preparation")

    saturations = []
    for beta in [0.0, 0.1, 0.7, 2.0, 6.0]:
        value = float(np.vdot(gaussian, expm(-beta * hamiltonian) @ gaussian).real)
        bound = float((1 + np.exp(-beta)) / 2)
        require(abs(value - bound) < MATRIX_TOL, "Actual-h heat-kernel saturation")
        saturations.append({"beta": beta, "expectation": value, "bound": bound})

    data = {"operators": operators, "h": hamiltonian, "P": projector, "d": defect,
            "M": target, "g_star": gaussian}
    report = {
        "spectrum": spectrum.tolist(),
        "car_max_frobenius_residual": car_residual,
        "minimum_eigenvalue_h_minus_defect": min_comparison,
        "gaussian_saturator_energy": gaussian_energy,
        "gaussian_equivalence_vector_error": map_error,
        "number_conserving_preparation_vector_error": pair_preparation_error,
        "clifford_preparation_vector_error": clifford_error,
        "eigenbasis_measurement_residual": measurement_residual,
        "heat_kernel_saturations": saturations,
    }
    return data, report


def check_random_gaussians(data: dict) -> list[dict]:
    rng = np.random.default_rng(SEED)
    reports = []
    for blocks, trials in [(1, 40), (2, 40), (3, 20)]:
        max_subset_ratio = 0.0
        max_heat_ratio = 0.0
        min_energy_density = np.inf
        for _ in range(trials):
            state = random_gaussian_state(4 * blocks, rng)
            require(abs(np.linalg.norm(state) - 1) < SCREEN_TOL, "Random Gaussian normalization")
            energy = sum(
                np.vdot(state, apply_block_operator(state, data["h"], j, blocks)).real
                for j in range(blocks)
            )
            min_energy_density = min(min_energy_density, float(energy / blocks))
            require(energy / blocks >= 0.5 - SCREEN_TOL, "Sampled Gaussian energy floor")
            for length in range(1, blocks + 1):
                for subset in combinations(range(blocks), length):
                    result = state
                    for block in subset:
                        result = apply_block_operator(result, data["P"], block, blocks)
                    ratio = float(np.vdot(state, result).real * 2**length)
                    max_subset_ratio = max(max_subset_ratio, ratio)
                    require(ratio <= 1 + SCREEN_TOL, "Every sampled block-subset fidelity")
            for beta in [0.1, 0.7, 2.0, 6.0]:
                kernel = np.exp(-beta) * np.eye(16) + (1 - np.exp(-beta)) * data["P"]
                result = state
                for block in range(blocks):
                    result = apply_block_operator(result, kernel, block, blocks)
                value = float(np.vdot(state, result).real)
                bound = float(((1 + np.exp(-beta)) / 2) ** blocks)
                max_heat_ratio = max(max_heat_ratio, value / bound)
                require(value <= bound + SCREEN_TOL, "Sampled Gaussian defect heat kernel")
        reports.append({
            "blocks": blocks,
            "modes": 4 * blocks,
            "trials": trials,
            "largest_subset_ratio": max_subset_ratio,
            "largest_heat_kernel_ratio": max_heat_ratio,
            "lowest_sampled_energy_density": min_energy_density,
        })
    return reports


def check_selected_spaces(data: dict) -> list[dict]:
    """Use actual selected orbital configurations crossing below the HF floor.

    A passive block orbital rotation produces g_star and an orthogonal Gaussian
    partner. On two blocks the four corresponding configurations contain the
    exact target; K=1,2,3,4 therefore test nontrivial variational energies.
    """
    a = data["operators"]
    generator = (
        a[2].conj().T @ a[0] - a[0].conj().T @ a[2]
        + a[3].conj().T @ a[1] - a[1].conj().T @ a[3]
    )
    orbital = expm(np.pi / 4 * generator)
    require(np.linalg.norm(orbital @ occupation("1100") - data["g_star"]) < MATRIX_TOL,
            "Explicit saturator is a passive orbital rotation")
    first, second = orbital[:, int("1100", 2)], orbital[:, int("0011", 2)]
    basis = np.column_stack([
        np.kron(first, first), np.kron(first, second),
        np.kron(second, first), np.kron(second, second),
    ])
    require(np.linalg.norm(basis.conj().T @ basis - np.eye(4)) < MATRIX_TOL,
            "Selected Gaussian configurations are orthonormal")
    h0 = np.kron(data["h"], np.eye(16)) + np.kron(np.eye(16), data["h"])
    expected_energies = [1.0, 0.5, 1 - 1 / np.sqrt(2), 0.0]
    reports = []
    for size in [1, 2, 3, 4]:
        selected = basis[:, :size]
        energy = float(np.linalg.eigvalsh(selected.conj().T @ h0 @ selected)[0])
        require(abs(energy - expected_energies[size - 1]) < MATRIX_TOL,
                "Selected-space variational spectrum")
        density = max(0.0, energy / 2)
        if abs(density - 0.5) < MATRIX_TOL:
            density = 0.5
        exponential_bound = float(np.exp(2 * (np.log(2) - binary_entropy(density))))
        require(size >= exponential_bound - SCREEN_TOL, "Nontrivial selected-space entropy bound")
        max_ratio = 0.0
        for beta in [0.1, 0.7, 2.0, 6.0]:
            local_kernel = expm(-beta * data["h"])
            restricted_kernel = selected.conj().T @ np.kron(local_kernel, local_kernel) @ selected
            largest = float(np.linalg.eigvalsh(restricted_kernel)[-1])
            trace_bound = float(size * ((1 + np.exp(-beta)) / 2) ** 2)
            require(largest <= trace_bound + SCREEN_TOL, "Selected-space positive trace bound")
            max_ratio = max(max_ratio, largest / trace_bound)
        reports.append({
            "blocks": 2, "configurations": size,
            "variational_energy": energy, "energy_density": density,
            "entropy_lower_bound_on_configurations": exponential_bound,
            "largest_heat_kernel_to_trace_bound_ratio": max_ratio,
        })
    return reports


def check_connected_perturbations(data: dict) -> dict:
    a = [annihilator(8, j) for j in range(8)]
    number = sum(operator.conj().T @ operator for operator in a)
    connector = a[3].conj().T @ a[4] + a[4].conj().T @ a[3]
    h0 = np.kron(data["h"], np.eye(16)) + np.kron(np.eye(16), data["h"])
    target = np.kron(data["M"], data["M"])
    connector_norm = float(np.max(np.abs(np.linalg.eigvalsh(connector))))
    require(abs(connector_norm - 1) < MATRIX_TOL, "Hopping-link norm")
    require(np.linalg.norm(connector @ number - number @ connector) < MATRIX_TOL,
            "Hopping conserves total particle number")
    hopped = connector @ target
    require(abs(np.vdot(hopped, hopped).real - 0.5) < MATRIX_TOL, "Nonzero hopping witness")
    commutator_witness_error = float(np.linalg.norm(h0 @ hopped - 4 * hopped))
    require(commutator_witness_error < MATRIX_TOL, "Noncommuting-link energy witness")
    require(abs(np.vdot(target, connector @ target)) < MATRIX_TOL, "Zero trial hopping expectation")
    records = []
    for strength in [1 / 64, 1 / 32, 1 / 16]:
        connected = h0 + strength * connector
        energy0 = float(np.linalg.eigvalsh(connected)[0])
        trial = float(np.vdot(target, connected @ target).real)
        require(abs(trial) < MATRIX_TOL, "Connected trial energy is zero")
        require(-strength - MATRIX_TOL <= energy0 <= MATRIX_TOL, "Perturbed ground-energy norm bracket")
        require(trial - energy0 <= strength + MATRIX_TOL, "Sharpened explicit-link trial guarantee")
        records.append({
            "lambda": strength, "ground_energy_two_blocks": energy0,
            "easy_trial_energy": trial, "trial_error_per_block": (trial - energy0) / 2,
        })
    return {"link_norm": connector_norm,
            "commutator_witness_residual": commutator_witness_error,
            "couplings": records}


def check_covariance_example(data: dict) -> dict:
    """The two-block covariance example in local_certification.md."""
    operators = [annihilator(8, j) for j in range(8)]
    product_pair = np.kron(data["M"], data["M"])
    two_term_cat = (occupation("11001100") + occupation("00110011")) / np.sqrt(2)
    h0 = np.kron(data["h"], np.eye(16)) + np.kron(np.eye(16), data["h"])
    covariance_data = []
    energies = []
    for state in [product_pair, two_term_cat]:
        annihilated = np.column_stack([a @ state for a in operators])
        created = np.column_stack([a.conj().T @ state for a in operators])
        normal = annihilated.conj().T @ annihilated
        anomalous = created.conj().T @ annihilated
        require(np.linalg.norm(normal - 0.5 * np.eye(8)) < MATRIX_TOL,
                "Covariance example has half-filled diagonal one-body matrix")
        require(np.linalg.norm(anomalous) < MATRIX_TOL,
                "Covariance example has zero anomalous matrix")
        covariance_data.append((normal, anomalous))
        energies.append(float(np.vdot(state, h0 @ state).real))
    require(abs(energies[0]) < MATRIX_TOL, "Product-pair example has zero energy")
    require(abs(energies[1] - 2) < MATRIX_TOL, "Rank-two cat has one energy unit per block")
    discrepancy = max(float(np.linalg.norm(left - right))
                      for left, right in zip(covariance_data[0], covariance_data[1]))
    require(discrepancy < MATRIX_TOL, "Equal full two-point data")
    return {"blocks": 2,
            "two_point_data_difference_frobenius": discrepancy,
            "product_pair_energy": energies[0], "two_term_cat_energy": energies[1],
            "cat_occupation_strings": ["11001100", "00110011"]}


def check_chernoff_constants() -> dict:
    base = float(27 * (8 + 2 * np.sqrt(7)) / 256)
    threshold = 1 - 1 / base
    density = 3 / 16
    beta = float(np.log(threshold * (1 - density) / (density * (1 - threshold))))
    optimized_expression = float(-beta * density - np.log((1 - threshold) + threshold * np.exp(-beta)))
    divergence = binary_relative_entropy(density, threshold)
    require(beta > 0, "Positive Chernoff optimizer below threshold")
    require(abs(optimized_expression - divergence) < MATRIX_TOL, "Chernoff and relative-entropy expressions agree")
    require(divergence > 0, "Positive explicit unrestricted-rank exponent")
    return {
        "R": base, "q": threshold, "delta": 1 / 32, "epsilon": 1 / 8,
        "effective_defect_density": density,
        "orthogonal_exponent_bits_per_block": float((np.log(2) - binary_entropy(density)) / np.log(2)),
        "unrestricted_exponent_bits_per_block": float(divergence / np.log(2)),
        "unrestricted_prefactor": "8 / (9 * (m + 1))",
        "chernoff_optimizer_beta": beta,
        "chernoff_expression_residual": abs(optimized_expression - divergence),
    }


def run_checks() -> dict:
    data, model = check_local_model()
    random_states = check_random_gaussians(data)
    selected_spaces = check_selected_spaces(data)
    perturbations = check_connected_perturbations(data)
    covariance_example = check_covariance_example(data)
    constants = check_chernoff_constants()
    return {
        "report_format": 1,
        "status": "passed",
        "checks_passed": CHECK_COUNT,
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "random_seed": SEED,
        "tolerances": {"matrix_absolute": MATRIX_TOL, "screen_absolute": SCREEN_TOL},
        "local_model": model,
        "gaussian_screening": random_states,
        "orthogonal_selected_spaces": selected_spaces,
        "connected_perturbations": perturbations,
        "covariance_counterexample": covariance_example,
        "equal_accuracy_example": constants,
        "limits": (
            "Finite floating-point checks validate signs, spectra and representation conventions. "
            "The random Gaussian ensemble is not a proof of a universal bound or a Gaussian optimization. "
            "The analytic proofs establish the asymptotic statements; the two-block perturbation data "
            "make no thermodynamic gap or ground-state preparation claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"),
                        help="JSON report path; default is alongside this script")
    args = parser.parse_args()
    report = run_checks()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"PASS: {report['checks_passed']} finite checks; report written to {args.output}")


if __name__ == "__main__":
    main()
