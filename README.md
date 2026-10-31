# Fermionic Configuration Limits

**Can a state be easy to prepare and certify, yet require exponentially many Gaussian configurations at fixed energy accuracy?** An explicit local fermionic model gives this separation. Every state below a fixed energy density requires exponentially many terms in a global Gaussian expansion, even when each term has independently optimized orbitals and the terms are nonorthogonal.

The model has four modes per block and bounded, number-conserving two-body fermionic interactions. Its exact ground state is a product of correlated pairs,

$$
|\Omega_m\rangle
=\left(\frac{|1100\rangle+|0011\rangle}{\sqrt2}\right)^{\otimes m},
$$

prepared with $O(m)$ gates and constant parallel depth. Weak finite-range hopping connects the blocks while preserving a separation at the same fixed energy-density target. The state also has compact classical product, geminal, coupled-cluster and tensor-network descriptions. The resource constrained here is the length of a **global linear expansion in Gaussian states**.

## Principal results

Write $H_0$ for the explicit Hamiltonian with ground energy zero, $P_j=|M\rangle\langle M|_j$ for its block ground-state projectors, and $D_m=\sum_j(I-P_j)$. The [model proof](science/model.md) establishes $0\le D_m\le H_0$. Energies below are per four-mode block.

### Arbitrary nonorthogonal Gaussian expansions

For every normalized pure state with $\langle D_m\rangle\le em$ and $0\le e<q$,

$$
\boxed{
\underline\chi_{\mathrm G}(\psi)
\ge\frac{8}{9(m+1)}\exp\!\big[m\,d(e\|q)\big],
\qquad
q=1-\frac{256}{27(8+2\sqrt7)}\simeq0.28665.
}
$$

Here $d$ is binary relative entropy with natural logarithms and $\underline\chi_{\mathrm G}$ is Gaussian border rank. Thus the bound includes exact sums, arbitrary coefficients and conditioning, different orbitals for every term, and limits of such sums. Slater determinant expansions are included. The [complete proof](science/gaussian_rank.md) gives all conventions and endpoints, and records the stronger asymptotic threshold $100/343$ obtained from the stronger inherited rank bound.

The load-bearing fixed-target rank bounds are prior results of [Reardon-Smith](references/README.md#rs26) and [Wei, Wu, Liu and Liu](references/README.md#wwll26). The argument here converts their uniform approximation bounds into a constraint on **every state in a low-energy-density region**, by Gaussian occupation conditioning and a positive heat-kernel expansion.

### Orthogonal configurations and the best determinant

If a state belongs to a span of $K$ orthonormal Gaussian vectors and has energy at most $em$, then

$$
\boxed{
K\ge\exp\!\big[m(\ln2-h(e))\big],
\qquad 0\le e<\tfrac12,
}
$$

where $h$ is binary entropy in nats. This allows arbitrary global orbital optimization and configuration selection. A single optimized determinant has energy $m/2$, and the energy density optimized over all orthogonal Gaussian configuration spaces of subexponential dimension tends to $1/2$. The [orthogonal proof](science/orthogonal_configurations.md) explains why this sharper threshold requires orthogonality.

| Representation class | Certified threshold | What may be optimized |
| --- | --- | --- |
| Orthogonal Gaussian configuration space | Energy density below one half | Global orbitals and the entire selected configuration set |
| Arbitrary Gaussian sum or border-rank limit | Energy density below approximately 0.28665 in the fully explicit bound | Separate orbitals, coefficients, nonorthogonality and conditioning |
| Product, geminal, cluster or tensor-network description | Outside this expansion-size constraint | Correlated block factors or another implicit representation |

### Connected perturbations and local certification

For $H=H_0+V$ with $\|V\|\le\delta m$, any state within $\epsilon m$ of the perturbed ground energy has defect density at most $\epsilon+2\delta$. The simple product trial is within $2\delta m$ of optimal. Choosing $2\delta\le\epsilon<q-2\delta$ therefore compares the easy trial and the unrestricted Gaussian expansion at the **same accuracy**. The [perturbation account](science/perturbations.md) supplies an explicit connected hopping family and an example with fixed nonzero coupling.

A trusted measurement of one randomly selected four-mode term per independent copy estimates the energy density using $O(\eta^{-2}\ln(1/\alpha))$ copies for slack $\eta$ and failure probability $\alpha$. [Local certification](science/local_certification.md) gives exact constants, charges full-state preparation, and defines the mixed-state class excluded by the witness. It also gives a rank-two state with the same covariance as the hard product state, showing why quadratic data alone cannot certify this rank separation.

## Read the science

The [scientific overview](science/README.md) connects the physical question, proof mechanism and algorithmic consequence. For a direct proof route, use:

| Question | Authoritative account |
| --- | --- |
| What is the Hamiltonian, and how is its ground state prepared? | [Model, exact spectrum and preparation](science/model.md) |
| Why do arbitrary nonorthogonal expansions need exponentially many terms? | [Gaussian rank at fixed energy density](science/gaussian_rank.md) |
| What stronger statement holds for orthogonal configurations? | [Orthogonal configuration theorem](science/orthogonal_configurations.md) |
| Does the obstruction survive connected interactions at matched accuracy? | [Perturbation transfer and explicit family](science/perturbations.md) |
| What can a local measurement certify? | [Finite-confidence and mixed-state guarantees](science/local_certification.md) |
| Which algorithms and resource models are constrained? | [Algorithmic scope and compact classical alternatives](science/algorithmic_scope.md) |
| Which results are imported, and how does this differ from earlier work? | [Primary comparisons](references/related_work.md), [citation index](references/README.md), and [bibliography](references/bibliography.bib) |

[The LLM reading guide](llms.txt) maps questions to these sources and preserves the essential distinctions.

## Reproduce the finite checks

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
```

The [verification guide](verification/README.md) documents the environment, checks, expected outputs and numerical tolerances. The recorded run passes 973 checks of the CAR conventions, spectrum, preparation, Gaussian examples, variational spaces, connected links, quoted constants and covariance counterexample. These finite checks support the algebraic conventions and examples. The universal and asymptotic claims follow from the written proofs and attributed theorems.

## Scope

The result is a representation obstruction on an explicit bounded-range lattice family. It is not a general classical-computation lower bound, a claim of quantum advantage, a theorem about generic molecular Hamiltonians, or a universal quantum-sampling lower bound. Final configuration count includes classical augmentation and product completion. The perturbed analysis certifies an energy-accurate trial without asserting a perturbed spectral gap or efficient exact ground-state preparation. The certified unrestricted-rank threshold is not claimed optimal.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
