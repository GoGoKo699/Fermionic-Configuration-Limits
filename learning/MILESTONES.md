# Thirty milestones for Fermionic Configuration Limits

This map organizes the project's scientific story for any reader. The question is how many Gaussian or determinant terms are needed to reach a fixed energy density, even when the same state admits a compact preparation and a compact classical description. The canonical statements and proofs remain in [the science documents](../science/README.md).

The single educational anchor is **McArdle et al., *Quantum computational chemistry*, Reviews of Modern Physics 92, 015003 (2020)**, [DOI](https://doi.org/10.1103/RevModPhys.92.015003). The [McArdle bridge](MCARDLE_BRIDGE.md#source-map) identifies the checked manuscript and its section and page conventions. The primary research papers cited below supply theorem inputs and attribution; they are not additional educational anchors. The 2020 review supplies foundations and does not contain the later Gaussian-rank theorems or this project's energy-density argument.

The allocation follows the structure of the result:

- **M01–M12: background/preliminaries.** Move from individual fermionic occupations and interactions to states, representation classes, energy criteria, and a complete computational contract.
- **M13–M30: narrative/innovation.** Move from the four-mode construction through the two lower-bound mechanisms to certification, connected perturbations, and the full meaning and limits of the representation obstruction.

The first phase integrates its ingredients in M12. The second culminates in M30. The additional space in the second phase reflects the distinct orthogonal and nonorthogonal proofs and the need to connect them to a physical accuracy and resource statement. The map covers the central understanding targets and their dependencies; specialist calculations and full derivations remain in the linked sources.

## Phase I — Background and preliminaries

<a id="m01"></a>

### M01 — Occupations and fermionic signs

**Phase:** Background/preliminaries.

**Central question:** What does an occupation string specify, and why does operator order matter for fermions?

**Understanding target:** Read an occupation state as a pattern of occupied modes; distinguish a mode from a particle; and explain how anticommutation fixes the sign of a creation or annihilation operation in an ordered basis.

**Earlier dependencies and story role:** None. This establishes the local objects and conventions from which every state and interaction in the project is built.

**Conceptual connection:** Second quantization makes the chemistry Hamiltonian and the representation problem expressible in the same occupation language.

**Source pointers:** McArdle §III.B, “First and Second quantisation”; [bridge notation](MCARDLE_BRIDGE.md#notation); [model conventions](../science/model.md#conventions-and-locality).

<a id="m02"></a>

### M02 — Local interactions and conserved particle number

**Phase:** Background/preliminaries.

**Central question:** What makes a term one-body or two-body, and how can a two-body term involve four modes?

**Understanding target:** Interpret number operators, hopping, density interactions, and pair transfer; identify number conservation; and distinguish fermionic interaction order from the number of qubits touched after an encoding.

**Earlier dependencies and story role:** [M01](#m01). This turns occupation notation into the local Hamiltonian ingredients used later.

**Conceptual connection:** An explicitly listed, bounded-range fermionic Hamiltonian supplies a concrete input model without a data-loading oracle.

**Source pointers:** McArdle §§III.B and IV.B on second quantization and encodings; [bridge notation](MCARDLE_BRIDGE.md#notation); [four-mode Hamiltonian](../science/model.md#the-four-mode-hamiltonian).

<a id="m03"></a>

### M03 — Determinants and orbital choices

**Phase:** Background/preliminaries.

**Central question:** What changes when orbitals are rotated, and what remains a single Slater determinant?

**Understanding target:** Relate an occupation configuration to an antisymmetrized product of occupied orbitals; distinguish a different orbital basis from a superposition of configurations; and recognize that a global orbital optimization can correlate the description across all blocks.

**Earlier dependencies and story role:** [M01](#m01), [M02](#m02). This identifies the elementary states counted by selected configuration methods.

**Conceptual connection:** A representation lower bound must survive the allowed orbital choices, rather than merely count nonzero coefficients in one convenient basis.

**Source pointers:** McArdle §III.C.3, “Configuration interaction”; [bridge representation classes](MCARDLE_BRIDGE.md#representation-classes); [orthogonal representation and accuracy](../science/orthogonal_configurations.md#representation-and-accuracy).

<a id="m04"></a>

### M04 — The larger Gaussian class and parity

**Phase:** Background/preliminaries.

**Central question:** How does a fermionic Gaussian state generalize a fixed-particle Slater determinant?

**Understanding target:** Distinguish particle-number-preserving orbital rotations from general Gaussian transformations, which may mix creation and annihilation operators; separate definite parity from definite particle number; and explain why a bound for the larger Gaussian class also constrains determinants.

**Earlier dependencies and story role:** [M01](#m01), [M03](#m03). This fixes the free-state class before its superpositions are counted.

**Conceptual connection:** Allowing more Gaussian states strengthens the eventual obstruction, while parity remains essential when importing fermionic results and conditioning subsystems.

**Source pointers:** [Bridge representation classes](MCARDLE_BRIDGE.md#representation-classes); [Gaussian definitions](../science/gaussian_rank.md#definitions-and-conventions); [Bravyi05](../references/README.md#bravyi05). McArdle §III.B supplies the fermionic notation; the Gaussian extension is supplied locally.

<a id="m05"></a>

### M05 — Linear expansions versus compact products

**Phase:** Background/preliminaries.

**Central question:** Why can a short product or cluster expression expand into exponentially many configurations?

**Understanding target:** Distinguish an explicitly enumerated linear configuration expansion from a product of correlated factors and an exponential cluster parametrization. Explain why their description lengths need not agree.

**Earlier dependencies and story role:** [M02](#m02), [M03](#m03). This supplies the representation comparison that prevents an exponential configuration count from becoming a general complexity claim.

**Conceptual connection:** Configuration interaction and coupled cluster can describe the same state through different mathematical objects, with different costs for keeping the description explicit.

**Source pointers:** McArdle §§III.C.3–III.C.4, “Configuration interaction” and “Coupled cluster”; [two-block bridge example](MCARDLE_BRIDGE.md#two-block-example); [classical alternatives](../science/algorithmic_scope.md#easy-preparation-and-classical-alternatives).

<a id="m06"></a>

### M06 — Variational energy and a density target

**Phase:** Background/preliminaries.

**Central question:** What is being approximated when the allowed energy error is proportional to system size?

**Understanding target:** Interpret the variational energy as an expectation minimized over a specified state class; distinguish total energy, energy per block, and error above the ground energy; and keep the Hilbert-space sector and normalization fixed in a comparison.

**Earlier dependencies and story role:** [M02](#m02), [M03](#m03), [M05](#m05). This defines the physical success criterion for a representation.

**Conceptual connection:** The theorem asks for a fixed additive energy-density accuracy, which remains meaningful under a change of energy origin and as more blocks are added.

**Source pointers:** McArdle §V.B, “Variational algorithms”; [bridge task and source map](MCARDLE_BRIDGE.md#source-map); [input and accuracy contract](../science/algorithmic_scope.md#input-and-accuracy-contract).

<a id="m07"></a>

### M07 — Energy accuracy versus global fidelity

**Phase:** Background/preliminaries.

**Central question:** Why can a state have low energy density while being orthogonal to the ground state?

**Understanding target:** Distinguish vector error, squared overlap, and energy expectation. Explain why a fixed total excitation can have vanishing density in a growing system, and why a spectral-gap argument using total error does not automatically solve a fixed-density problem.

**Earlier dependencies and story role:** [M06](#m06). This identifies the logical gap between the imported target-state results and the project's desired all-low-energy conclusion.

**Conceptual connection:** A lower bound for approximating one vector cannot be substituted for a lower bound applying to every state that meets the energy criterion.

**Source pointers:** [Bridge energy versus fidelity](MCARDLE_BRIDGE.md#energy-versus-fidelity); [inherited and new results](../references/related_work.md#what-is-inherited-and-what-is-proved-here); McArdle §V.B for the variational-energy setting.

<a id="m08"></a>

### M08 — Pure states, mixtures, and linear observations

**Phase:** Background/preliminaries.

**Central question:** How does a probabilistic mixture change the meaning of a statement about a state-vector expansion?

**Understanding target:** Distinguish a coherent superposition from a mixed ensemble, use a density operator to express linear observable averages, and recognize that a mixed state can have many ensemble decompositions.

**Earlier dependencies and story role:** [M05](#m05), [M06](#m06). This supplies the language needed to state a physical-source certificate without assuming purity silently.

**Conceptual connection:** A pure-state representation bound can extend to a specified convex class of mixtures, but that extension requires a definition and does not become a claim about ordinary matrix rank.

**Source pointers:** McArdle §V.B.2, “Measurement,” for observable estimation; [bridge local certification](MCARDLE_BRIDGE.md#local-certification); [mixed-state class](../science/local_certification.md#mixed-state-guarantee).

<a id="m09"></a>

### M09 — Gaussian rank, nonorthogonality, and border rank

**Phase:** Background/preliminaries.

**Central question:** What is counted by Gaussian rank, and why is taking a limit a separate issue?

**Understanding target:** Define the least number of Gaussian terms in a vector, distinguish orthogonal and nonorthogonal lists, and explain how diverging coefficients can cancel in a convergent sequence. Distinguish exact rank, border rank, and approximation at a specified nonzero error.

**Earlier dependencies and story role:** [M04](#m04), [M05](#m05), [M07](#m07). This establishes the unrestricted representation resource before any lower bound is used.

**Conceptual connection:** Orthogonalization preserves a span but generally does not preserve Gaussianity of its basis vectors; border rank prevents a bound from relying on well-conditioned coefficients.

**Source pointers:** [Bridge representation classes](MCARDLE_BRIDGE.md#representation-classes); [rank definitions](../science/gaussian_rank.md#definitions-and-conventions); [WWLL26, Appendix A.3](../references/README.md#wwll26).

<a id="m10"></a>

### M10 — Gaussian conditioning and branch probabilities

**Phase:** Background/preliminaries.

**Central question:** What remains after occupations of some modes are measured and a particular outcome is retained?

**Understanding target:** Distinguish an unnormalized conditional vector from its normalized branch state; keep the branch probability in averages; and use the fact that occupation conditioning maps a pure Gaussian state to a Gaussian state or zero. Account for the retained branch's parity.

**Earlier dependencies and story role:** [M04](#m04), [M08](#m08), [M09](#m09). This supplies the local operation that will transfer a target-overlap theorem to arbitrary block subsets.

**Conceptual connection:** The proof uses conditioning as a mathematical decomposition of an expectation, so it averages all outcomes instead of paying a physical inverse-success-probability cost.

**Source pointers:** [Bridge imported ingredients](MCARDLE_BRIDGE.md#imported-ingredients); [conditional Gaussian closure](../science/gaussian_rank.md#conditioning-on-complementary-modes); [Bravyi05](../references/README.md#bravyi05).

<a id="m11"></a>

### M11 — Positive operators and spectral probability

**Phase:** Background/preliminaries.

**Central question:** How can positivity and scalar convexity bound an expectation of a function of energy?

**Understanding target:** Interpret a state as inducing a probability distribution on the eigenvalues of an observable; read an exponential energy filter as a positive operator; and distinguish scalar Jensen's inequality from an operator-monotonicity assertion. Understand why positive coefficients allow inequalities to be summed safely.

**Earlier dependencies and story role:** [M06](#m06), [M07](#m07), [M08](#m08). This connects individual spectral weights to the global inequalities needed in both proof paths.

**Conceptual connection:** A positive filter is the common language through which overlap information will constrain an energy expectation.

**Source pointers:** [Bridge orthogonal bound](MCARDLE_BRIDGE.md#orthogonal-bound); [Gaussian heat-kernel argument](../science/orthogonal_configurations.md#a-gaussian-heat-kernel-bound); [Jensen step in the general proof](../science/gaussian_rank.md#low-energy-theorem). These mathematical steps are supplied locally beyond the review's measurement setting.

<a id="m12"></a>

### M12 — The complete computational contract

**Phase:** Background/preliminaries.

**Central question:** What must an algorithm receive, produce, and pay for in the problem studied here?

**Understanding target:** State the explicit local Hamiltonian input, allowed Gaussian or determinant output class, fixed energy-density target, and permitted orbital optimization. Separate final configuration count from state-preparation gates, supplied copies, measurement shots, and classical solver operations. Distinguish conditioning used inside a proof from access supplied to an algorithm.

**Earlier dependencies and story role:** [M03](#m03), [M05](#m05), [M06](#m06), [M08](#m08), [M09](#m09), [M10](#m10), [M11](#m11). This integrates the first phase into one operational problem whose assumptions can be carried through the proof.

**Conceptual connection:** The chemistry workflow motivates the task, while the output contract determines exactly which algorithms the forthcoming theorem constrains.

**Source pointers:** McArdle §§IV.B, V.B, and V.B.2; [bridge resource contract](MCARDLE_BRIDGE.md#resource-contract); [algorithmic scope](../science/algorithmic_scope.md#which-output-representations-are-constrained).

## Phase II — Narrative and innovation

<a id="m13"></a>

### M13 — The correlated four-mode block

**Phase:** Narrative/innovation.

**Central question:** How does a simple two-body Hamiltonian select a correlated pair as its unique ground state?

**Understanding target:** Explain the roles of the pair-hopping term and the particle-number penalty in $`h=I-(A+A^\dagger)+(N-2)^2`$. Identify its symmetric zero-energy state, gap one, norm five, and comparison with the defect projector $`I-\vert M\rangle\langle M\vert `$.

**Earlier dependencies and story role:** [M01](#m01), [M02](#m02), [M03](#m03), [M06](#m06). The narrative begins with a complete local mechanism and its sign convention.

**Conceptual connection:** The block converts an abstract non-Gaussian target into the low-energy state of an explicit number-conserving physical Hamiltonian.

**Source pointers:** [Bridge local Hamiltonian](MCARDLE_BRIDGE.md#local-hamiltonian); [block Hamiltonian and spectrum](../science/model.md#the-four-mode-hamiltonian).

<a id="m14"></a>

### M14 — Many blocks and an easy trial state

**Phase:** Narrative/innovation.

**Central question:** What changes when the correlated block is repeated across a growing system?

**Understanding target:** Relate $`H_0`$, the commuting defect sum $`D_m`$, and the product ground state. Explain the extensive norm, persistent gap, fixed particle number, and exact preparation with $`O(m)`$ gates and constant block-parallel depth.

**Earlier dependencies and story role:** [M05](#m05), [M12](#m12), [M13](#m13). This assembles the local example into the family on which the representation obstruction is proved.

**Conceptual connection:** Repetition makes an extensive accuracy question possible while retaining an explicit, inexpensive source state and a compact classical product description.

**Source pointers:** [Two-block bridge example](MCARDLE_BRIDGE.md#two-block-example); [many-block model](../science/model.md#the-many-block-model); [charged preparation](../science/model.md#exact-preparation-and-charged-resources).

<a id="m15"></a>

### M15 — Importing the target fidelity with the correct equivalence

**Phase:** Narrative/innovation.

**Central question:** Why can a theorem for the vacuum–full four-mode superposition be applied to the fixed-number block?

**Understanding target:** Explain the Gaussian-unitary map $`W`$ between the two targets and why its failure to conserve particle number does not invalidate the representation comparison. Identify the inherited squared-fidelity identity $`F_G(M^{\otimes s})=2^{-s}`$ and its specific target-orbit scope.

**Earlier dependencies and story role:** [M04](#m04), [M07](#m07), [M13](#m13), [M14](#m14). This connects the constructed model to an existing quantitative theorem without attributing that theorem to this project.

**Conceptual connection:** A mathematical change of Gaussian variables can preserve the relevant resource even when the physical preparation follows a different, number-conserving route.

**Source pointers:** [Bridge imported ingredients](MCARDLE_BRIDGE.md#imported-ingredients); [exact target equivalence](../science/model.md#exact-equivalence-to-the-standard-fermionic-magic-state); [RS24, Lemma 1](../references/README.md#rs24).

<a id="m16"></a>

### M16 — Fidelity on every retained subset

**Phase:** Narrative/innovation.

**Central question:** How does a bound for one product target constrain all retained subsets of a globally correlated Gaussian state?

**Understanding target:** Reconstruct the conditioning argument for $`\langle P_S\rangle_g\le2^{-\vert S\vert }`$, including averaging branch probabilities, odd and zero branches, the empty subset, and Gaussian permutations of noncontiguous blocks.

**Earlier dependencies and story role:** [M10](#m10), [M14](#m14), [M15](#m15). This is the first local-to-global transfer step in the orthogonal proof.

**Conceptual connection:** Global Gaussian correlations are allowed throughout; conditioning supplies a subset statement without assuming that the Gaussian competitor factorizes across blocks.

**Source pointers:** [Bridge orthogonal bound](MCARDLE_BRIDGE.md#orthogonal-bound); [retained-subset lemma](../science/orthogonal_configurations.md#lemma-1-the-same-bound-controls-every-retained-block-subset); [Bravyi05](../references/README.md#bravyi05).

<a id="m17"></a>

### M17 — Combining subset information with a positive filter

**Phase:** Narrative/innovation.

**Central question:** Why does the exponential of the defect sum combine all subset bounds without uncontrolled cancellations?

**Understanding target:** Explain the product expansion of $`e^{-\beta D_m}`$ for $`\beta\ge0`$, the nonnegative coefficients of every $`P_S`$, and the resulting single-Gaussian bound $`[(1+e^{-\beta})/2]^m`$. Identify where commutation is used.

**Earlier dependencies and story role:** [M11](#m11), [M14](#m14), [M16](#m16). This turns many local subset constraints into one global spectral constraint.

**Conceptual connection:** The proof gains control of a distribution of defect energies, rather than only the overlap with its zero-defect vector.

**Source pointers:** [Bridge orthogonal bound](MCARDLE_BRIDGE.md#orthogonal-bound); [Gaussian heat-kernel bound](../science/orthogonal_configurations.md#a-gaussian-heat-kernel-bound).

<a id="m18"></a>

### M18 — The orthogonal configuration bound

**Phase:** Narrative/innovation.

**Central question:** How does a bound on each Gaussian basis vector constrain every vector in their selected span?

**Understanding target:** Connect positivity, the trace over an orthonormal Gaussian basis, scalar Jensen, and optimization over $`\beta`$ to obtain $`\log K\ge m[\log2-h(e)]`$ for $`0\le e\lt 1/2`$. Explain why the trace step needs orthonormality and why the exponent is not continued above the threshold.

**Earlier dependencies and story role:** [M09](#m09), [M11](#m11), [M12](#m12), [M17](#m17). This completes the first global representation theorem.

**Conceptual connection:** The span's dimension becomes an explicit multiplicative allowance in the positive-filter bound, converting a physical energy target into an output-size requirement.

**Source pointers:** [Bridge orthogonal bound](MCARDLE_BRIDGE.md#orthogonal-bound); [orthogonal configuration theorem](../science/orthogonal_configurations.md#the-orthogonal-configuration-theorem).

<a id="m19"></a>

### M19 — The exact determinant optimum and asymptotic floor

**Phase:** Narrative/innovation.

**Central question:** What improvement over the best single determinant can a subexponential orthogonal expansion achieve?

**Understanding target:** Explain the explicit determinant attaining energy $`m/2`$, the Pinsker energy floor for dimension $`K`$, and their implication that the optimal density tends to $`1/2`$ whenever $`\log K=o(m)`$. Distinguish this sharp asymptotic statement from an unproved finite-$`K`$ frontier.

**Earlier dependencies and story role:** [M03](#m03), [M13](#m13), [M18](#m18). This translates the orthogonal exponent into a statement about recovering extensive correlation energy after optimal orbital choice.

**Conceptual connection:** The comparison has a matching simple variational benchmark, so its physical meaning is stronger than counting the ground state's coefficients in one basis.

**Source pointers:** [Bridge orthogonal bound](MCARDLE_BRIDGE.md#orthogonal-bound); [best determinant and sharp floor](../science/orthogonal_configurations.md#the-best-determinant-and-the-sharp-asymptotic-floor).

<a id="m20"></a>

### M20 — Uniform approximation bounds become weak-overlap bounds

**Phase:** Narrative/innovation.

**Central question:** How can a theorem about approximating a target vector control an exponentially small overlap with that target?

**Understanding target:** Identify the imported unnormalized approximation theorem and apply it to the scaled vector $`z\chi`$, where $`z=\langle\chi\vert M^{\otimes s}\rangle`$. Explain why the squared error is $`1-\vert z\vert ^2`$ and why a uniform factor $`1-r^2`$ as the approximation radius $`r\to1`$ is indispensable.

**Earlier dependencies and story role:** [M07](#m07), [M09](#m09), [M15](#m15). This supplies the different quantitative ingredient needed when orthogonality is removed.

**Conceptual connection:** The source theorem controls the number of Gaussian terms despite arbitrary coefficients; scaling extracts exactly the overlap information needed for the energy argument.

**Source pointers:** [Bridge weak overlap](MCARDLE_BRIDGE.md#weak-overlap); [uniform approximate-rank input](../science/gaussian_rank.md#uniform-approximate-rank-input); [weak target-overlap lemma](../science/gaussian_rank.md#rank-controls-even-very-small-target-overlap); [RS26, Theorem 2 and Section IV](../references/README.md#rs26).

<a id="m21"></a>

### M21 — Subset bounds for arbitrary Gaussian superpositions

**Phase:** Narrative/innovation.

**Central question:** Why does conditioning preserve a useful term-count bound even when the Gaussian summands overlap or nearly cancel?

**Understanding target:** Apply occupation conditioning term by term, normalize each nonzero branch without changing rank, and average its weak target overlap. Recover the bound proportional to $`K(s+1)R^{-s}`$ for every retained subset without a Gram-conditioning assumption.

**Earlier dependencies and story role:** [M09](#m09), [M10](#m10), [M16](#m16), [M20](#m20). This replaces the orthogonal-basis trace mechanism with a statement valid for arbitrary Gaussian decompositions.

**Conceptual connection:** The global number of terms bounds every conditional branch; branch probabilities prevent postselection from introducing an artificial inverse-probability penalty.

**Source pointers:** [Bridge weak overlap](MCARDLE_BRIDGE.md#weak-overlap); [conditioning on complementary modes](../science/gaussian_rank.md#conditioning-on-complementary-modes).

<a id="m22"></a>

### M22 — The unrestricted low-energy rank theorem

**Phase:** Narrative/innovation.

**Central question:** What energy-density obstruction survives arbitrary nonorthogonal Gaussian choices?

**Understanding target:** Combine the general subset estimate with the positive filter, Jensen, and the optimized nonnegative parameter to obtain $`K\ge8\exp[m\,d(e\Vert q)]/[9(m+1)]`$ for $`0\le e\lt q`$, where $`q=1-1/R`$. Explain the polynomial prefactor and the smaller threshold relative to the orthogonal theorem.

**Earlier dependencies and story role:** [M17](#m17), [M18](#m18), [M21](#m21). This completes the second global lower bound and identifies its exact representation scope.

**Conceptual connection:** Binary relative entropy measures the exponential cost of forcing the defect density below the value controlled by the imported rank input.

**Source pointers:** [Bridge rank–energy argument](MCARDLE_BRIDGE.md#rank-energy); [general low-energy theorem](../science/gaussian_rank.md#low-energy-theorem).

<a id="m23"></a>

### M23 — Closure, endpoints, and inherited improvements

**Phase:** Narrative/innovation.

**Central question:** Which limits preserve the theorem, and where does its quantitative conclusion stop?

**Understanding target:** Pass bounded-operator expectations to a border-rank limit at fixed $`m`$; distinguish that passage from finite-error approximation of an arbitrary low-energy state; and explain the zero-energy limit and zero optimized rate at and above $`q`$. Identify the stronger inherited WWLL26 input and its unspecified absolute constant without treating either threshold as optimal.

**Earlier dependencies and story role:** [M09](#m09), [M20](#m20), [M22](#m22). This settles the robustness and precise boundaries of the unrestricted theorem before it is used operationally.

**Conceptual connection:** A meaningful representation obstruction must survive ill-conditioned limiting descriptions while respecting the actual parameter domain of its proof.

**Source pointers:** [Bridge rank–energy argument](MCARDLE_BRIDGE.md#rank-energy); [border rank and endpoints](../science/gaussian_rank.md#border-rank-and-endpoints); [stronger inherited bound](../science/gaussian_rank.md#stronger-inherited-asymptotic-bound); [WWLL26](../references/README.md#wwll26).

<a id="m24"></a>

### M24 — A finite-confidence local energy certificate

**Phase:** Narrative/innovation.

**Central question:** How can measurements on one block per copy certify a global representation requirement?

**Understanding target:** Explain uniform classical block selection, the charged four-mode measurement of $`h_j`$, and outcomes in $`[0,5]`$. Use the one-sided confidence bound with $`T\ge\lceil25\ln(1/\alpha)/(2\eta^2)\rceil`$ to obtain an energy upper bound and a pure-state rank certificate, under independent identical copies and trusted measurement.

**Earlier dependencies and story role:** [M08](#m08), [M12](#m12), [M13](#m13), [M22](#m22), [M23](#m23). This connects the proved energy constraint to data from a physical source.

**Conceptual connection:** A bounded estimator of density needs no system-size factor in its sampling range. Each full-state copy contains $`4m`$ modes; the explicit product source costs $`O(m)`$ preparation gates per copy, while an unknown source's preparation cost must be charged separately.

**Source pointers:** McArdle §V.B.2, “Measurement”; [bridge local certification](MCARDLE_BRIDGE.md#local-certification); [measurement model](../science/local_certification.md#measurement-model); [statistical guarantee](../science/local_certification.md#statistical-guarantee); [Hoeffding63](../references/README.md#hoeffding63).

<a id="m25"></a>

### M25 — What low energy certifies for a mixed source

**Phase:** Narrative/innovation.

**Central question:** What is the correct representation conclusion when the observed source is not known to be pure?

**Understanding target:** Define the closed convex hull of pure states with Gaussian border rank at most $`K`$, extend the filter bound by linearity and continuity, and interpret exclusion when $`K\lt B_m(e_U)`$. Separate that conclusion from ordinary density-matrix rank and from a claim that every component of every ensemble has high rank.

**Earlier dependencies and story role:** [M08](#m08), [M22](#m22), [M23](#m23), [M24](#m24). This supplies the physical-source scope of the local certificate.

**Conceptual connection:** The measured energy is linear in the density operator, allowing a rigorous convex-class exclusion without identifying a preferred ensemble decomposition.

**Source pointers:** [Bridge local certification](MCARDLE_BRIDGE.md#local-certification); [mixed-state guarantee](../science/local_certification.md#mixed-state-guarantee).

<a id="m26"></a>

### M26 — Identical covariance, different rank and energy

**Phase:** Narrative/innovation.

**Central question:** Why can complete two-point fermionic data miss the exponential representation obstruction?

**Understanding target:** Compare the product of correlated blocks with the rank-at-most-two global cat for $`m\ge2`$. Explain their identical one-particle density matrices and vanishing anomalous covariance, yet different local pair coherence and energies $`0`$ and $`m`$.

**Earlier dependencies and story role:** [M04](#m04), [M08](#m08), [M14](#m14), [M22](#m22), [M24](#m24). This identifies what information the local energy measurement adds beyond quadratic observables.

**Conceptual connection:** The project certifies a many-term representation requirement, which is a different conclusion from detecting non-Gaussianity or reconstructing Gaussian covariance data.

**Source pointers:** [Two-block bridge example](MCARDLE_BRIDGE.md#two-block-example); [covariance counterexample](../science/local_certification.md#covariance-does-not-certify-this-resource); [comparison with covariance witnesses](../references/related_work.md#HTS26).

<a id="m27"></a>

### M27 — Transferring the obstruction under an extensive perturbation

**Phase:** Narrative/innovation.

**Central question:** How does a bound on perturbation norm control both a low-energy competitor and the easy trial?

**Understanding target:** Derive the ground-energy sandwich for $`H=H_0+V`$ with $`\Vert V\Vert \le\delta m`$, the defect-density bound $`e\le\epsilon+2\delta`$ for a state within $`\epsilon m`$ of the ground energy, and the trial error at most $`2\delta m`$. Keep the same particle-number sector throughout the comparison.

**Earlier dependencies and story role:** [M06](#m06), [M14](#m14), [M18](#m18), [M22](#m22). This moves the representation theorem beyond exactly independent blocks without assuming a perturbed spectral gap or global-fidelity estimate.

**Conceptual connection:** Operator-norm control transfers a fixed density criterion even when the perturbation fails to commute with the original Hamiltonian.

**Source pointers:** [Bridge connected family](MCARDLE_BRIDGE.md#connected-family); [uniform perturbation theorem](../science/perturbations.md#a-uniform-perturbation-theorem).

<a id="m28"></a>

### M28 — Connected interactions at the same requested accuracy

**Phase:** Narrative/innovation.

**Central question:** Can the easy trial and the lower bound be compared at one accuracy in a genuinely coupled family?

**Understanding target:** Explain the fixed-strength adjacent-block hopping, its norm and noncommutativity witness, and the choices $`2\delta\le\epsilon\lt q-2\delta`$ or the orthogonal endpoint $`1/2-2\delta`$. Distinguish preparing a certified trial from preparing the exact perturbed ground state.

**Earlier dependencies and story role:** [M02](#m02), [M12](#m12), [M19](#m19), [M23](#m23), [M27](#m27). This integrates locality, coupling, and approximation into the final physical comparison.

**Conceptual connection:** The interaction strength need not vanish with system size, and both representations are judged against the same additive energy-density tolerance.

**Source pointers:** [Bridge connected family](MCARDLE_BRIDGE.md#connected-family); [equal-accuracy comparison](../science/perturbations.md#equal-accuracy-comparison); [connected noncommuting example](../science/perturbations.md#an-explicit-connected-noncommuting-family).

<a id="m29"></a>

### M29 — Compact escapes and the costs they avoid

**Phase:** Narrative/innovation.

**Central question:** How can an exponentially large Gaussian expansion coexist with an easy classical and quantum description of the same trial?

**Understanding target:** Explain the exact geminal product and doubles-cluster identity using commuting nilpotent block excitations, the compact matrix-product description, and the charged non-Gaussian basis change that makes the trial one configuration. Separate explicit output records, quantum shots, solver operations, and full-state preparation costs.

**Earlier dependencies and story role:** [M05](#m05), [M12](#m12), [M14](#m14), [M19](#m19), [M24](#m24), [M28](#m28). This consolidates the constructive alternatives and the resource boundaries of the negative result.

**Conceptual connection:** The obstruction belongs to an explicit global Gaussian linear representation. Keeping a product or cluster expression changes that output contract and provides a substantive escape.

**Source pointers:** McArdle §III.C.4, “Coupled cluster”; [bridge resource contract](MCARDLE_BRIDGE.md#resource-contract); [bridge scope](MCARDLE_BRIDGE.md#scope); [exact classical alternatives](../science/algorithmic_scope.md#easy-preparation-and-classical-alternatives); [selected-configuration workflows](../science/algorithmic_scope.md#consequences-for-selected-configuration-workflows).

<a id="m30"></a>

### M30 — The complete representation and certification principle

**Phase:** Narrative/innovation.

**Central question:** What does the project establish once its source inputs, accuracy, representation classes, and costs are all stated together?

**Understanding target:** Give one connected account of the local construction, inherited target theorems, subset-to-energy mechanism, distinct orthogonal and unrestricted conclusions, mixed-source certificate, and equal-accuracy perturbation result. Explain the advance from target fidelity to all-low-energy constraints while retaining the compact classical alternatives and the absence of an unrestricted computational-hardness or quantum-advantage claim.

**Earlier dependencies and story role:** [M12](#m12), [M19](#m19), [M23](#m23), [M25](#m25), [M26](#m26), [M28](#m28), [M29](#m29). This integrates the two phases into the project's scientific contribution and its limits.

**Conceptual connection:** A state can be easy to prepare and describe, and locally certifiable, while every sufficiently accurate explicit global Gaussian expansion is exponentially large. Representation choice, physical accuracy, and information access jointly determine what that statement means.

**Source pointers:** [Bridge scope](MCARDLE_BRIDGE.md#scope); [science overview](../science/README.md); [algorithmic scope and resource accounting](../science/algorithmic_scope.md); [inherited and new contributions](../references/related_work.md#what-is-inherited-and-what-is-proved-here).
