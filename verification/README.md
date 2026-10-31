# Reproducible finite verification

The script [checks.py](checks.py) checks the fermionic signs, exact block spectrum, explicit state preparations, selected-space variational energies, and connected hopping example used in the scientific proofs. It also screens finite random Gaussian states against the subset and heat-kernel inequalities. [results.json](results.json) contains the actual output of the recorded run.

These checks complement the proofs. A finite random ensemble cannot establish a universal Gaussian bound or determine the optimal Gaussian state.

## Reproduce the run

The recorded environment is CPython 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The third-party packages are pinned in [requirements.txt](requirements.txt), and [.python-version](.python-version) records the Python version. From the repository root, use an isolated environment and run:

```bash
python3.12 -m venv /tmp/fermionic-configuration-verification
/tmp/fermionic-configuration-verification/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/fermionic-configuration-verification/bin/python verification/checks.py
```

The script prints one pass summary and writes `verification/results.json`. A failed check raises an exception and prevents a success report. To preserve the committed report while reproducing:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verification/checks.py --output /tmp/fermionic-configuration-results.json
```

The random seed is fixed at `20261031`. No network access, quantum hardware, external datasets, or symbolic-mathematics service is needed after installing the dependencies. Floating-point roundoff can differ across platforms, so compare the stated assertions and tolerances rather than requiring byte-identical JSON. The largest dense matrices are 256 by 256; the largest state vectors have 4096 amplitudes.

## Recorded results

The recorded run passed **973 checks** with the pinned versions above. Its local spectrum was zero once, one four times, two nine times, and five twice. The exact Gaussian map and Clifford preparation had zero vector residual; the number-conserving preparation residual was approximately $`1.1\times10^{-16}`$. The determinant saturator had energy exactly $`1/2`$ and saturated the tested heat-kernel values to floating-point precision.

All 100 random Gaussian samples satisfied every tested subset and heat-kernel inequality. The selected orbital spaces gave the four variational energies displayed below. For the connected two-block systems at couplings $`1/64`$, $`1/32`$, and $`1/16`$, the ground energies were approximately $`-3.05176\times10^{-5}`$, $`-1.22070\times10^{-4}`$, and $`-4.88281\times10^{-4}`$, while the simple trial retained energy zero. The two covariance-example states had matching two-point matrices and total energies zero and two.

The result file preserves unrounded values, numerical residuals, and the stated limits of interpretation.

## Checks and the claims they address

| Check | Scientific purpose |
| --- | --- |
| Canonical anticommutation relations and expanded Hamiltonian | Fix the ordered Fock convention and verify the stated two-body operator |
| Complete 16-dimensional spectrum and defect comparison | Verify the unique zero, gap one, norm five, and positivity used in the energy lift |
| Exact Gaussian equivalence, two preparations, and local eigenbasis measurement | Catch relative-phase, pair-transfer, particle-number, and readout-label conventions |
| Explicit determinant energy and heat-kernel saturation | Check the sharp one-determinant floor and the Gaussian envelope |
| Every block subset in 100 random Gaussian states | Screen the subset inequality, including cross-block correlations and both parities |
| Four inverse temperatures for those random states | Screen the positive-coefficient heat-kernel expansion |
| Selected spaces with one to four orbital configurations on two blocks | Check the variational and trace arguments at nontrivial energies below the determinant floor |
| Three connected two-block Hamiltonians | Check the link norm, noncommutativity witness, trial expectation, and perturbation bracket |
| Product-pair state and two-term cat on two blocks | Check identical full two-point data despite their distinct extensive energies |
| Explicit Chernoff optimizer and equal-accuracy exponents | Check the numerical constants quoted in the perturbation example |

### Random Gaussian ensemble

Each sample starts in a uniformly chosen occupation vector and applies `12 * modes` adjacent matchgates. The even and odd two-dimensional blocks of each gate are independently sampled SU(2) matrices. Their determinants agree, so the gate is a fermionic Gaussian matchgate. Starting occupations include both total-parity sectors.

There are 40 samples on four modes, 40 on eight modes, and 20 on twelve modes. Every nonempty subset of the one, two, or three blocks is checked. This includes the separated first-and-third-block subset in the twelve-mode case. The distribution is a reproducible convention screen; it is not claimed to sample Gaussian states with Haar measure.

### Selected spaces

A passive orbital rotation produces the explicit determinant saturator and an orthogonal Gaussian partner on each block. On two blocks, their four product configurations span the exact target. Taking the first one, two, three, and four configurations gives exact total variational energies

```math
1,\qquad \frac12,\qquad 1-\frac1{\sqrt2},\qquad0.
```

These examples test the orthogonal-space inequality in the range where it constrains the energy, rather than only at random high-energy states. The script checks both the optimized entropy bound and the operator-norm-to-positive-trace step.

## Tolerances and limits

The local matrix tolerance is $`10^{-12}`$; accumulated random-circuit and selected-space inequalities allow absolute slack $`2\times10^{-11}`$. The report records residuals and the maximum tested ratios to the bounds.

The four-mode diagonalization is a finite check of the analytic spectrum in [model.md](../science/model.md). Universal Gaussian fidelity is imported from [RS24](../references/README.md#rs24), and unrestricted approximate Gaussian rank from [RS26](../references/README.md#rs26); the script does not re-prove either external theorem. The general-rank portion of the script evaluates its Chernoff constants only, not arbitrary nonorthogonal decompositions.

The local-certification checks validate the exact measurement basis and the covariance counterexample in [local_certification.md](../science/local_certification.md). They do not replace the analytical Hoeffding guarantee with a Monte Carlo coverage claim.

The connected calculations use two blocks. They do not establish a thermodynamic spectral gap, exact perturbed ground-state preparation, optimal exponents, or hardness for other classical representations. Those statements are not required by the [uniform perturbation proof](../science/perturbations.md).
