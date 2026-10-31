# Primary sources and the scope of the result

This document records the primary results used in the proofs and the closest algorithmic comparisons. The source versions listed below were checked on 31 October 2026. Version numbers matter: an updated journal article can contain discussion that is absent from an earlier preprint. The [BibTeX file](bibliography.bib) gives reusable metadata, and the [reference index](README.md) provides short citation links.

## What is inherited and what is proved here

The [model](../science/model.md) is an explicit number-conserving, two-body fermionic Hamiltonian on $4m$ modes. Its unperturbed ground state is a product of correlated four-mode pairs. A Gaussian change of variables identifies each pair with the standard four-mode fermionic magic state. The exact target fidelity in [RS24](#RS24), the approximate target-rank bound in [RS26](#RS26), and the stronger asymptotic bound in [WWLL26](#WWLL26) are **inputs**, not new results of this project.

The new argument changes the output criterion from approximation of one target vector in global norm to a bound for **every state of sufficiently low local energy**. Occupation postselection transfers the target-overlap bound to every subset of blocks. Expanding a positive heat kernel then combines all subset bounds, and scalar Jensen converts the result into an energy-density constraint. The [orthogonal proof](../science/orthogonal_configurations.md) uses a trace over an orthonormal Gaussian basis. The [general-rank proof](../science/gaussian_rank.md#low-energy-theorem) instead uses the uniform approximate-rank input, so it permits nonorthogonal terms, separate orbital choices, arbitrary coefficients, and border rank.

These are different approximation criteria. For example, replacing one block of the ground-state product by an orthogonal two-particle eigenstate gives a state orthogonal to the ground state with total energy one, hence vanishing energy density as $m$ grows. A global-fidelity theorem for the ground state alone therefore does not establish a uniform energy-density theorem. The subset and heat-kernel steps supply the missing argument.

For a state of defect density at most $e$, the explicit unrestricted bound proved here is

$$
K\ge\frac{8}{9(m+1)}\exp\!\left[mD_{\mathrm{KL}}(e\Vert q)\right],
\qquad q=1-\frac{256}{27(8+2\sqrt7)},\quad e<q.
$$

The stronger orthogonal bound is $\log K\ge m[\log2-h(e)]$ for $e<1/2$. The larger threshold requires orthogonality and is not asserted for arbitrary Gaussian rank. The [perturbation argument](../science/perturbations.md) transfers both results to a connected, finite-range interacting family at fixed energy-density accuracy. The [local certificate](../science/local_certification.md) estimates a bounded local energy observable and gives a separate, explicitly defined mixed-state guarantee.

## Comparison at the level of the claimed output

| Prior result or algorithm | Its relevant output or hypothesis | Relationship to this work |
| --- | --- | --- |
| Gaussian fidelity and approximate rank | Fidelity or global-norm approximation to a specified tensor-power target | Imported quantitative ingredients; the all-state low-energy implication is proved here. |
| Selected configuration interaction, QSCI, and SQD | A variational state in a selected global configuration span | The theorem lower-bounds the final span size on the explicit family, independent of how it is selected. |
| Nonorthogonal determinant optimization, including EIDOS | A linear combination of individually optimized Slater determinants | Included in the unrestricted Gaussian-rank theorem, with its smaller energy threshold. |
| Classical CI size-extensivity analysis | Correct extensive energy can require exponentially many configurations | The qualitative limitation is established background; the result here is a quantitative uniform energy floor over the stated representation classes. |
| Gaussian-assisted nontrivial-low-energy-state constructions | A lower bound on preparation depth, including free Gaussian operations | Different resource. The present trial state has constant preparation depth. |
| Covariance-based non-Gaussianity witnesses | Tests of Gaussianity or related non-Gaussian resources | They do not by themselves certify the exponential rank proved here; a same-covariance counterexample is given in the certification document. |

No comparison in this table claims a lower bound for every classical algorithm, a failure on every molecular instance, or a quantum advantage. The exact ground state of the unperturbed model has compact classical descriptions. The contribution concerns a specified global linear representation and a physical accuracy criterion; see [algorithmic scope](../science/algorithmic_scope.md).

## Imported mathematical results

<a id="RS24"></a>

### RS24 — multiplicativity for the four-mode target

**Oliver Reardon-Smith.** *The fermionic linear optical extent is multiplicative for 4 qubit parity eigenstates.* arXiv:2407.20934v1, 30 July 2024. [Record](https://arxiv.org/abs/2407.20934v1) · [Primary text](https://arxiv.org/html/2407.20934v1).

Lemma 1, Eqs. (10)–(12), establishes that appending the four-mode state $a_8=(|0000\rangle+|1111\rangle)/\sqrt2$ multiplies the maximum squared Gaussian overlap by $1/2$, for a fixed-parity pure input. Iteration gives $F_G(a_8^{\otimes s})=2^{-s}$. This specific identity is the input to the orthogonal configuration proof. No general multiplicativity theorem for the Gaussian fidelity of arbitrary states is assumed. The paper's extent result and correction of an earlier argument should not be presented as new here.

<a id="RS26"></a>

### RS26 — explicit uniform approximate-rank input

**Oliver Reardon-Smith.** *Exponential lower bounds on the fermionic Gaussian rank of magic states and the bosonic coherent state rank of Fock states.* arXiv:2610.03699v1, 2 October 2026. [Record](https://arxiv.org/abs/2610.03699v1) · [Primary text](https://arxiv.org/html/2610.03699v1).

Theorem 2, Eqs. (5)–(7), gives the bound $(1-\delta^2)8R^s/[9(s+1)]$ on the number of Gaussian terms approximating $a_8^{\otimes s}$ within vector-norm error $\delta<1$, where $R=27(8+2\sqrt7)/256$. The denominator contains $s+1$. Section IV, Eqs. (81)–(87), supports the unnormalized-approximant formulation and uniform dependence on $\delta$, essential when converting rank to overlap. This is a target-vector theorem; the energy-density lift and finite weak-coupling application are the present deductions.

<a id="WWLL26"></a>

### WWLL26 — robust rank, border rank, and an inherited improvement

**Fuchuan Wei, Kong-Wing Wu, Zhengwei Liu, and Zi-Wen Liu.** *Robust exponential lower bounds for fermionic and bosonic Gaussian ranks.* arXiv:2610.02172v1, 1 October 2026. [Record](https://arxiv.org/abs/2610.02172v1) · [Primary text](https://arxiv.org/html/2610.02172v1).

Theorem 1 treats robust exponential rank growth for tensor powers of a fixed non-Gaussian pure state, with definite parity assumed in the fermionic case. For the four-mode target, Theorem 12, Eqs. (73)–(74), gives finite coefficient bounds and a uniform lower bound $c(1-\delta^2)(343/243)^s$ for an absolute $c>0$. The statement includes approximate border rank. Appendix B.2.1 also records the occupation-postselection closure used in such arguments. Substituting this input into our lift improves the threshold to $100/343$; the improvement is inherited, and no explicit value of $c$ is claimed.

<a id="Bravyi05"></a>

### Bravyi05 — Gaussian operations and occupation postselection

**Sergey Bravyi.** *Lagrangian representation for fermionic linear optics.* Quantum Information and Computation **5**(3), 216–238 (May 2005). DOI: [10.26421/QIC5.3-3](https://doi.org/10.26421/QIC5.3-3). [Publisher record](https://www.rintonpress.com/journals/doi/QIC5.3-3.html) · [Checked preprint, quant-ph/0404180v2](https://arxiv.org/abs/quant-ph/0404180v2) · [Primary PDF](https://arxiv.org/pdf/quant-ph/0404180v2).

Section V, Theorem 1 and Corollary 2 in the checked preprint characterize Gaussian operators and their action on Gaussian states. Occupation-measurement projectors are included among Gaussian operations. A nonzero occupation-conditioned branch of a pure Gaussian state is Gaussian; after discarding the measured modes, the retained pure state remains Gaussian. Applied termwise, this implies that conditioning cannot increase the number of Gaussian terms in an expansion. Branch probabilities are retained in the averaging argument.

<a id="Hoeffding63"></a>

### Hoeffding63 — the local measurement confidence bound

**Wassily Hoeffding.** *Probability Inequalities for Sums of Bounded Random Variables.* Journal of the American Statistical Association **58**(301), 13–30 (March 1963). DOI: [10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830). [Original article scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf).

Printed page 16, Theorem 2, Eq. (2.6), bounds the upper tail of an average of independent bounded variables. Applying it to the negative of the observed local-energy outcomes, whose range is five, gives $\Pr\{e_\rho>\widehat e+\eta\}\le\exp(-2T\eta^2/25)$. This is the one-sided statement used in [local certification](../science/local_certification.md#statistical-guarantee). A two-sided interval requires the additional factor two in the failure-probability bound. Neither independence nor trusted measurement is supplied by Hoeffding's inequality itself.

## Configuration methods and size extensivity

<a id="Chan24"></a>

### Chan24 — the qualitative CI limitation is established background

**Garnet Kin-Lic Chan.** *Spiers Memorial Lecture: Quantum chemistry, classical heuristics, and quantum advantage.* Faraday Discussions **254**, 11–52 (2024). DOI: [10.1039/D4FD00141A](https://doi.org/10.1039/D4FD00141A). The checked preprint is titled *Quantum chemistry, classical heuristics, and quantum advantage*, [arXiv:2407.11235v1](https://arxiv.org/abs/2407.11235v1), 15 July 2024. [Primary text](https://arxiv.org/html/2407.11235v1).

Section 3.9.1 and Table 1 identify exponential cost as the price of extensive energy for configuration interaction. Sections 3.9.3–3.9.4 contrast exponential coupled-cluster parametrizations and tensor networks. Thus “CI can require exponential resources for extensive accuracy” is not the novelty claim. Our statements quantify a fixed-density obstruction for every admissible orbital choice and, separately, arbitrary nonorthogonal Gaussian expansions of an explicit local model.

<a id="QSCI23"></a>

### QSCI23 — the selected-subspace contract

**Keita Kanno, Masaya Kohda, Ryosuke Imai, Sho Koh, Kosuke Mitarai, Wataru Mizukami, and Yuya O. Nakagawa.** *Quantum-Selected Configuration Interaction: classical diagonalization of Hamiltonians in subspaces selected by quantum computers.* arXiv:2302.11320v1, 22 February 2023. [Record](https://arxiv.org/abs/2302.11320v1) · [Primary text](https://arxiv.org/html/2302.11320v1).

Section II.2 selects computational-basis configurations from quantum samples and classically diagonalizes the projected Hamiltonian. Section V discusses costs and its relation to selected CI. The resulting state lies in the selected determinant span, which is the output class constrained here. The lower bound concerns the size of that final span, even if selection is ideal. It does not identify that size with a universal number of quantum shots.

<a id="SQD25"></a>

### SQD25 — concentration assumptions and orbital optimization

**Javier Robledo-Moreno and coauthors.** *Chemistry beyond the scale of exact diagonalization on a quantum-centric supercomputer.* Science Advances **11**(25), eadu9991 (2025). DOI: [10.1126/sciadv.adu9991](https://doi.org/10.1126/sciadv.adu9991). Checked version: [arXiv:2405.05068v3](https://arxiv.org/abs/2405.05068v3), 13 July 2025. [Primary text](https://arxiv.org/html/2405.05068v3). Full authors are recorded in the bibliography.

The method recovers configurations and solves a projected variational problem. Supplementary Section 1.1.1, Eq. (S1), makes concentration parameters explicit; Supplementary Section 2.1 includes orbital optimization. The theorem here already allows arbitrary global orbitals and selection. It therefore identifies a family without a small successful configuration output, rather than contradicting a conditional convergence statement. Recovery or classical augmentation can add configurations not individually observed, so the theorem is not an unconditional shot lower bound.

<a id="GJ26"></a>

### GJ26 — finite-size evidence with ideal input sampling

**Cedric Gaberle and Manpreet Singh Jattana.** *A Critical Assessment of the Sample-Based Quantum Diagonalization for Heisenberg and Hubbard Models.* arXiv:2605.02494v2, 6 May 2026. [Record](https://arxiv.org/abs/2605.02494v2) · [Primary PDF](https://arxiv.org/pdf/2605.02494v2).

The paper studies one- and two-dimensional Heisenberg and Hubbard systems up to 20 qubits, including sampling from exact ground-state distributions. Section 3.4, Eq. (8), uses a relative-energy fidelity and reports scaling at specified thresholds. These computations are relevant evidence about idealized SQD costs, but the fits are not a theorem uniform over all orbital rotations or all possible determinant subsets. Selecting the most probable configurations is also not established there as globally optimal for variational energy.

<a id="Sugisaki26"></a>

### Sugisaki26 — product completion and size consistency

**Kenji Sugisaki.** *Size-consistent implementation of Hamiltonian simulation-based quantum-selected configuration interaction method for the supramolecular approach.* arXiv:2510.23154v2, 5 January 2026; v1 appeared 27 October 2025. [Record](https://arxiv.org/abs/2510.23154v2) · [Primary PDF](https://arxiv.org/pdf/2510.23154v2).

The introduction and Supplementary Information B analyze the sampling burden associated with size consistency. The proposed treatment uses localized monomer information and augments dimer spaces with required Cartesian-product configurations. This already identifies the product-completion issue. Our parameter $K$ counts the final global expansion after any such completion; it does not count only the configurations directly sampled. Keeping a product representation without materializing the global expansion is an allowed escape from the representation class studied here.

<a id="EIDOS25"></a>

### EIDOS25 — independently optimized nonorthogonal determinants

**Clemens Giuliani, Jannes Nys, Rocco Martinazzo, Giuseppe Carleo, and Riccardo Rossi.** *Precise Quantum Chemistry calculations with few Slater Determinants.* arXiv:2503.14502v2, 2 May 2025. [Record](https://arxiv.org/abs/2503.14502v2) · [Primary text](https://arxiv.org/html/2503.14502v2). The record links a later journal article at DOI [10.1038/s41467-026-70255-z](https://doi.org/10.1038/s41467-026-70255-z).

Equation (1) uses a sum of individually optimized, generally nonorthogonal Slater determinants. Appendix B discusses size consistency through numerical examples. Such an ansatz is included in unrestricted Gaussian rank, not in the orthogonal proof. The later journal discussion should not be silently attributed to v2. Our theorem is a worst-case statement about the explicit local family; it does not contest the reported numerical accuracy on the systems examined in this source.

## Other resource notions that must remain distinct

<a id="VO24"></a>

### VO24 — orbital-optimized participation complexity

**Tuomas I. Vanhala and Teemu Ojanen.** *Complexity of fermionic states.* Physical Review Research **6**, 023178 (2024). DOI: [10.1103/PhysRevResearch.6.023178](https://doi.org/10.1103/PhysRevResearch.6.023178). Checked version: [arXiv:2306.07584v2](https://arxiv.org/abs/2306.07584v2), 5 March 2024. [Primary text](https://arxiv.org/html/2306.07584v2).

Equation (1) defines a participation quantity minimized over orbital choices, and Eq. (3) bounds it through correlation entropy. Equation (4) is a proposed scaling relation, not a uniform theorem for arbitrary many-body states. These quantities motivate basis-independent questions, but do not supply the all-state energy-density or arbitrary nonorthogonal-rank bounds proved here. In particular, constant lower bounds on participation entropy are not exponential configuration lower bounds.

<a id="HATH24"></a>

### HATH24 — low-energy circuit depth with Gaussian assistance

**Yaroslav Herasymenko, Anurag Anshu, Barbara M. Terhal, and Jonas Helsen.** *Fermionic Hamiltonians without trivial low-energy states.* Physical Review A **109**(5), 052431 (2024). DOI: [10.1103/PhysRevA.109.052431](https://doi.org/10.1103/PhysRevA.109.052431). [Checked accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.109.052431), dated 7 March 2024; journal publication 21 May 2024.

Theorem 7 proves logarithmic preparation-depth lower bounds for constructed Hamiltonians, including a model with free Gaussian operations and a linear ancillary-mode budget. Lemma 8 uses separated measurement outcomes. This is a different restriction from the number of terms in a Gaussian superposition: an even-mode cat state has Gaussian rank at most two while its two occupation outcomes are maximally separated. Our constant-depth product preparation is therefore not a construction of this circuit-depth property.

<a id="HTS26"></a>

### HTS26 — Gaussianity tests and covariance witnesses

**Tobias Haug, Xhek Turkeshi, and Piotr Sierant.** *Practical Tests and Witnesses of Fermionic non-Gaussianity.* arXiv:2605.26218v3, 31 July 2026. [Record](https://arxiv.org/abs/2605.26218v3) · [Primary text](https://arxiv.org/html/2605.26218v3).

The fermionic anti-flatness framework supplies covariance-based tests and witnesses, including purity-dependent mixed-state criteria; Appendix I compares witnesses. Non-Gaussianity and an exponential Gaussian superposition rank are distinct conclusions. Our [same-covariance example](../science/local_certification.md#covariance-does-not-certify-this-resource) gives two pure states with identical complete quadratic data but very different ranks and local pairing energies. The certificate here uses the model-specific local energy and the proved rank-energy inequality, not covariance alone.

## Limits of the comparison

The bibliography supports the particular theorem statements and algorithmic contracts described above. It is not evidence that every possible related formulation has been excluded. The scientifically checkable claim is the proof in this repository: a quantitative obstruction for the stated representation classes, on a specified local model and its bounded perturbations, at the stated energy-density thresholds. Neither practical behavior on generic chemistry instances nor a separation between unrestricted quantum and classical computation follows from that claim.
