# Local energy and the cost of Gaussian configurations

The scientific question is whether a compact variational output class can fail even when the desired physical accuracy is modest and a suitable state is easy to prepare. The class considered here is a global linear combination of Slater determinants or, more generally, pure fermionic Gaussian states. Its cost parameter is the number of terms. Its accuracy criterion is a fixed additive energy error per block as the system grows.

This distinction matters for algorithms that select configurations from quantum samples and then solve a classical projected problem. Improving the samples, orbital optimization, or the projected solver cannot produce a small successful output if no state in the permitted representation class has the required energy. At the same time, a large expansion need not imply a difficult physical problem: retaining correlated blocks as a product can be far more efficient than expanding that product globally.

## A physical model with transparent preparation

The [model](model.md) starts from four fermionic modes and the two-particle state

```math
|M\rangle=\frac{|1100\rangle+|0011\rangle}{\sqrt2}.
```

A pair-hopping term favors its coherence, while a number penalty excludes unwanted particle sectors. Their sum is a positive, number-conserving, two-body fermionic Hamiltonian with a unique zero-energy state and gap one. Summing this block Hamiltonian over $`m`$ blocks gives $`H_0`$, with exact ground state $`M^{\otimes m}`$ and $`4m`$ modes.

This ground state is a product of small correlated units. It has an explicit linear-size circuit and constant parallel depth. It is also a simple classical product or geminal state. Yet its global occupation expansion contains exponentially many terms. The nontrivial question is whether arbitrary orbital rotations, nonorthogonal configurations, or acceptance of nonzero energy density can eliminate that expansion cost.

The analytical defect operator

```math
D_m=\sum_{j=1}^{m}(I-P_j),
\qquad P_j=|M\rangle\langle M|_j,
```

counts failed block projectors and obeys $`D_m\le H_0`$. Low physical energy therefore implies a small mean number of defects. The proof uses this expectation constraint, not a promise of high global fidelity. Indeed, exciting just one block produces a state orthogonal to the ground state with energy density $`1/m`$. A ground-state-fidelity statement alone does not control the whole low-energy region.

## The two proof routes

Both routes first control simultaneous success of any subset of block projectors. Occupation measurement on complementary modes preserves Gaussianity in every nonzero conditional branch. This lets a theorem about a tensor-power target constrain an arbitrary reduced subset, even when the original state has global Gaussian correlations.

For an **orthogonal Gaussian configuration space**, the imported exact Gaussian-fidelity identity gives a factor of one half for each retained block. A positive operator expectation in a normalized state is at most its trace over the containing space. This introduces the number of orthonormal Gaussian configurations, $`K`$, without assuming that the selected configurations came from sampling or that the orbitals were chosen efficiently.

For an **arbitrary Gaussian expansion**, orthogonalizing the list would generally destroy Gaussianity. The proof instead imports a robust approximate-rank theorem. Because it allows unnormalized approximants with errors arbitrarily close to one, it bounds even exponentially small target overlap in terms of $`K`$. Conditioning then gives the needed subset estimates without imposing a Gram-matrix or coefficient bound. Continuity extends the argument to border rank.

The common final step is the positive expansion

```math
e^{-\beta D_m}
=e^{-\beta m}\prod_{j=1}^{m}
\big[I+(e^\beta-1)P_j\big],
\qquad\beta\ge0.
```

Every coefficient is nonnegative, so every subset estimate can be inserted without cancellation. Scalar Jensen's inequality lower-bounds this heat-kernel expectation using the mean defect energy. Optimizing over $`\beta`$ produces a binary relative-entropy exponent, the same mathematical optimization familiar from Chernoff bounds.

| Ingredient | Orthogonal route | Arbitrary-expansion route |
| --- | --- | --- |
| Imported input | Exact Gaussian fidelity of the four-mode tensor target | Uniform approximate Gaussian-rank bound for that target |
| How configuration count enters | Trace over an orthonormal Gaussian basis | Rank bound for an unnormalized projected approximant |
| Reduction to subsets | Gaussian occupation postselection | The same operation, applied term by term |
| Energy conversion | Positive heat kernel and scalar Jensen | Positive heat kernel and scalar Jensen |
| Certified energy region | Below one half per block | Below approximately 0.28665 with the fully explicit constants |
| Main proof | [Orthogonal configurations](orthogonal_configurations.md) | [Gaussian rank and border rank](gaussian_rank.md) |

The sharper orthogonal threshold cannot be transferred to an arbitrary nonorthogonal expansion. Conversely, the unrestricted theorem covers separate orbital optimization for every determinant and singular limiting decompositions. Both statements allow more powerful selection than a particular practical algorithm may implement.

## Connected interactions at the same accuracy

The decoupled model isolates the mechanism. [The perturbation theorem](perturbations.md) shows that it also gives an energy-accuracy separation for weak connected interactions. If a perturbation has norm at most $`\delta m`$, the original product state stays within $`2\delta m`$ of the perturbed ground energy. Any state within $`\epsilon m`$ of that same optimum has unperturbed defect density at most $`\epsilon+2\delta`$.

There is therefore a nonempty interval of fixed accuracies for which the explicit product trial succeeds and every successful Gaussian expansion requires exponentially many terms. Nearest-block hopping supplies a connected, bounded-range, number-conserving example whose links fail to commute with the original blocks. Neither the coupling strength nor the allowed error density needs to vanish with system size.

This argument concerns a certified trial, and it does not require a theorem about the exact perturbed ground state's circuit depth or spectral gap. Keeping that distinction avoids attributing more to norm perturbation theory than it establishes.

## A locally accessible certificate

[The certification protocol](local_certification.md) chooses one block uniformly at random on each independent copy and measures its bounded local energy. The resulting estimator targets the energy density directly. Its outcome range is independent of system size, yielding a copy count independent of $`m`$ at fixed statistical slack and confidence. Each copy still contains the entire system, and its preparation cost remains extensive.

For a pure source, an energy upper-confidence bound below the threshold gives a Gaussian border-rank lower bound. For an unknown mixed source, the precise conclusion excludes the closed convex hull of pure states with a uniformly bounded border rank. The account defines this convex class and its confidence guarantee explicitly.

The observable probes local pair coherence that one-body covariance misses. The hard product state and a two-determinant cat can have identical complete quadratic data while their local energies differ extensively. Thus testing non-Gaussianity from covariance and certifying exponential Gaussian expansion size are distinct tasks.

## What the result changes

Exponential configuration costs and failures of truncated CI size extensivity are established background. The [source comparison](../references/related_work.md) credits that history and the recent rank theorems. The contribution here is a quantitative all-state low-energy consequence for an explicit physical family, uniformly over the specified orbital choices and expansion classes, together with connected perturbations and an operational local witness.

The [algorithmic account](algorithmic_scope.md) spells out the output contract. Final configurations count even when added through classical augmentation; no universal shot lower bound is inferred. An implicit product, a doubles-cluster exponential, a small tensor network, or a non-Gaussian block basis can escape the linear-expansion restriction. These compact alternatives explain how preparation, physical energy accuracy, and Gaussian configuration count can have very different costs in the same model.

For a theorem audit, read the model, then the appropriate rank proof, then perturbations and certification. For implementation conventions, use the [finite verification guide](../verification/README.md). Finite calculations establish signs, spectra and examples; the general scaling laws rely on the written arguments and precisely attributed inputs.
