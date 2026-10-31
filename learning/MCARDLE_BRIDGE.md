# From quantum computational chemistry to configuration limits

Consider a calculation that prepares a many-electron state, selects some electron configurations, and minimizes the energy inside their span. A useful trial state may be easy to prepare while its accurate expansion in those configurations is very large. This project makes that distinction quantitative on an explicit local Hamiltonian. The restriction persists after optimizing orbitals and, with a different bound, after allowing nonorthogonal Gaussian terms.

The selected educational anchor is **Sam McArdle, Suguru Endo, Alán Aspuru-Guzik, Simon C. Benjamin, and Xiao Yuan, _Quantum computational chemistry_, Reviews of Modern Physics 92, 015003 (2020)**. [Publisher record](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.92.015003) · [DOI](https://doi.org/10.1103/RevModPhys.92.015003) · [Publisher-hosted accepted manuscript](https://link.aps.org/accepted/10.1103/RevModPhys.92.015003).

This bridge supplies the missing project-specific reasoning. It can be read directly, with the review serving as a reference rather than a prerequisite to finish first. The [30-milestone map](MILESTONES.md) records the project's common understanding targets; the linked science documents remain the canonical theorem and proof statements.

<a id="source-map"></a>

## 1. Where the review connects to the project

The checked manuscript is dated **8 January 2020**; its publisher cover records publication on **30 March 2020**. The locators below use the manuscript's **printed page numbers**, excluding the extra publisher cover from the count. Equation numbers in this table belong to the review; subsequent equations belong to this bridge.

| Review location | Connection used here |
| --- | --- |
| §III.B.2a, p. 12, Eqs. (23)–(27) | Occupations, anticommutation, and a fermionic Hamiltonian. |
| §III.C.3, pp. 15–16, Eq. (32), “Configuration interaction” | Linear determinant expansions and size consistency. |
| §III.C.4, p. 16, Eqs. (33)–(35), “Coupled cluster” | Products and exponential parametrizations. |
| §IV.B.1, p. 22, Eqs. (50)–(54) | Occupation encoding and a four-mode example. |
| §V.B, pp. 31–32, Eqs. (64)–(68), “Variational algorithms” | Energy minimization, preparation, and expectation values. |
| §V.B.1b, p. 33, Eqs. (69)–(70) | Unitary excitation gates. |
| §V.B.2, pp. 34–35, Eq. (72), “Measurement” | Precision and repeated preparations. |

Three levels of attribution remain distinct. The review supplies the chemistry and algorithm vocabulary. The Gaussian fidelity and rank theorems are later research inputs, identified in [Section 7](#imported-ingredients). The subset, positive-filter, and energy-density arguments are proved in this project. The review does not contain current SQD/QSCI contracts or the 2024/2026 rank results. Those primary papers are research dependencies, not additional educational anchors.

<a id="notation"></a>

## 2. Occupations, energy, and a notation dictionary

A fermionic **mode** is one available single-particle state. Each mode can be empty or occupied once. Here there are $`4m`$ modes, grouped into $`m`$ consecutive blocks of four. The string $`\vert 1100\rangle`$ denotes two occupied modes followed by two empty modes. A normalized state is a linear combination of such strings; squared magnitudes of its coefficients give occupation-measurement probabilities. Relative phases also matter, because operators can connect different strings.

The creation operator $`a_i^\dagger`$ adds a particle to mode $`i`$ if it is empty; $`a_i`$ removes one if present. Their signs encode fermionic exchange:

```math
a_i a_j^\dagger+a_j^\dagger a_i=\delta_{ij}I,
\qquad a_i a_j+a_j a_i=0.
```

Here $`I`$ leaves a state unchanged, and $`\delta_{ij}`$ is one when $`i=j`$ and zero otherwise. The operator $`n_i=a_i^\dagger a_i`$ returns the occupation of mode $`i`$. We fix

```math
|n_1\cdots n_{4m}\rangle
=(a_1^\dagger)^{n_1}\cdots(a_{4m}^\dagger)^{n_{4m}}|\mathrm{vac}\rangle.
```

This ordering determines every sign. For example, removing a particle from mode $`i`$ contributes $`(-1)^{\sum_{k\lt i}n_k}`$. The [model](../science/model.md#conventions-and-locality) uses this convention throughout.

A Hamiltonian $`H`$ is a Hermitian operator specifying energies. For a normalized state $`\vert \psi\rangle`$, the expression $`\langle\psi\vert H\vert \psi\rangle`$, abbreviated $`\langle H\rangle_\psi`$, is its mean energy. Its minimum over all allowed normalized states is the ground energy $`E_0(H)`$. Restricting the states being minimized over cannot lower that minimum. This elementary variational fact makes a chosen configuration span an algorithmically meaningful restriction.

| Review notation | Project notation and distinction |
| --- | --- |
| $`M`$ spin-orbitals, $`N`$ electrons | $`4m`$ modes and, in the fixed-particle sector, $`2m`$ particles. The ket $`\lvert M\rangle`$ below denotes a state, not a mode count. |
| $`\lvert f_{M-1},\ldots,f_0\rangle`$ in Eq. (23) | Our displayed string puts the lowest mode index first. Translate indices and the creation convention together. |
| $`h_{pq}`$ and $`h_{pqrs}`$ in Eq. (27) | Coefficients of fermionic monomials; our $`h_j`$ is an entire block operator. |
| Pauli strings $`P_j`$ in Eqs. (52), (67) | Our $`P_j=\lvert M\rangle\langle M\rvert_j`$ is a block projector. |
| Excitation generator $`T`$ in Eq. (34) | We write $`T_{\mathrm{cl}}`$ for a cluster generator, keeping $`T_{\mathrm{copies}}`$ for measurement copies. |
| Energy precision in Eq. (72) | Here $`\epsilon`$ is variational error per block, and $`\eta`$ is a statistical margin for energy per block. |

The task studied here is

```math
\langle H\rangle_\psi-E_0(H)\le\epsilon m.
```

Thus a fixed $`\epsilon`$ means fixed accuracy per four-mode block, or $`\epsilon/4`$ per mode. It permits total error proportional to system size. It differs from requiring a fixed total-energy error as $`m`$ increases.

<a id="representation-classes"></a>

## 3. Determinants, Gaussian states, and what is being counted

A **Slater determinant** fills a specified set of mutually orthogonal single-particle orbitals. Occupation strings are determinants in the original orbital basis. A global orbital rotation replaces the creation operators by linear combinations,

```math
b_p^\dagger=\sum_i U_{ip}a_i^\dagger,
\qquad U^\dagger U=I.
```

Filling the new orbitals gives another determinant. The rotation may mix modes across all blocks. The theorem grants that freedom, even if implementing or optimizing the rotation would be expensive.

There are two representation questions. In an **orthogonal configuration space**, select $`K`$ orthonormal Gaussian vectors $`g_1,\ldots,g_K`$ and allow every normalized vector in their span. Configurations from one orbital-rotated occupation basis are a special case. An arbitrary sum

```math
|\psi\rangle=\sum_{\ell=1}^{K}c_\ell|g_\ell\rangle
```

is more permissive when the $`g_\ell`$ need not be orthogonal. It can use different orbitals for each term and large cancelling coefficients. The two cases require different proofs and have different certified energy thresholds.

A pure fermionic **Gaussian state** is an occupation-state image under a unitary generated by quadratic fermionic operators. Allowing particle-pair creation and annihilation in the quadratic generator enlarges the class beyond number-preserving orbital rotations. It includes both parity sectors; parity records whether the particle number is even or odd. Slater determinants are included. Physical states may still be restricted to a definite particle number or parity in the problem. See the precise [Gaussian-class definition](../science/gaussian_rank.md#definitions-and-conventions).

“Gaussian” here describes a many-body state class. It does not refer to the spatial shape of a one-particle basis function, a different use of the word in chemistry basis sets. A choice of Gaussian-shaped orbitals does not make an arbitrary correlated many-electron state Gaussian.

The **Gaussian rank** $`\chi_G(\psi)`$ is the smallest number $`K`$ in such a general sum. Its **border rank** $`\underline\chi_G(\psi)`$ is the smallest $`K`$ for which rank-at-most-$`K`$ vectors can approach $`\psi`$ arbitrarily closely in vector norm, at fixed system size. Border rank allows limiting cancellations and therefore strengthens the obstruction. Neither quantity is the ordinary matrix rank of a density operator.

A classical mixture is different again: it selects states with probabilities rather than adding their amplitudes coherently. Section 12 states the exact mixed-state conclusion instead of assigning an unspecified “rank” to a mixed state.

<a id="local-hamiltonian"></a>

## 4. One block: a pair coherence with a simple energy cost

Suppress the block index and write

```math
|L\rangle=|1100\rangle,\qquad |R\rangle=|0011\rangle,
\qquad |M\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2}.
```

There are always two particles, but the pair is coherently shared between two occupation patterns. Define

```math
A=a_1^\dagger a_2^\dagger a_4a_3,
\qquad B=A+A^\dagger,
\qquad N=\sum_{i=1}^4n_i,
```

and choose

```math
h=I-B+(N-2)^2.
```

The paired occupations also appear in the review's four-mode expansion, Eq. (54), p. 22. Setting their amplitudes equal and the other amplitudes to zero gives this block state. That identifies the notation; the Hamiltonian chosen here is a separate construction.

The operator $`A`$ takes $`R`$ to $`L`$ with positive sign, and $`A^\dagger`$ reverses that transfer. The $`-B`$ term lowers the energy when the two amplitudes add coherently. The number penalty favors two particles in the block.

On the span of $`L,R`$, the Hamiltonian is simply

```math
h\big|_{\mathrm{span}\{L,R\}}
=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
```

Its symmetric state $`M`$ has energy zero, and the antisymmetric state $`(L-R)/\sqrt2`$ has energy two. Every other occupation string has energy $`1+(N-2)^2`$. The remaining two-particle strings therefore have energy one; the one- and three-particle strings have energy two; the empty and full strings have energy five. This proves a unique ground state and a gap of one.

This is an at-most-two-body **fermionic** Hamiltonian because

```math
h=5I-3\sum_i n_i+2\sum_{i\lt k}n_in_k-B
```

contains no term with more than two creation and two annihilation operators. Pair hopping can nevertheless involve four modes. The construction is not a claim that the corresponding qubit Hamiltonian is two-local, or that these coefficients arise from a particular molecule. It is a deliberately explicit local family.

Let $`P=\vert M\rangle\langle M\vert `$. The operator $`I-P`$ returns zero on the desired block state and one on its orthogonal complement. Since every excited energy is at least one,

```math
h\ge I-P\ge0.
```

For $`m`$ blocks, define

```math
H_0=\sum_jh_j,\qquad
D_m=\sum_j(I-P_j),\qquad
|\Omega_m\rangle=|M\rangle^{\otimes m}.
```

The symbol $`\otimes`$ combines block states. The product $`\Omega_m`$ has energy zero. The commuting operator $`D_m`$ counts block defects in its joint eigenbasis, and $`H_0\ge D_m`$. The project uses $`D_m`$ to prove the bound; it measures the physical two-body operators $`h_j`$. [Canonical model and spectrum](../science/model.md).

<a id="two-block-example"></a>

## 5. Two blocks: the difference between a product and its expansion

For two blocks the exact state is

```math
|\Omega_2\rangle
=\frac{|LL\rangle+|LR\rangle+|RL\rangle+|RR\rangle}{2}.
```

Each term is one global occupation determinant. Describing the state as two identical factors uses a short expression; expanding those factors produces four terms. With $`m`$ blocks the same expansion has $`2^m`$ terms. This count in one basis is an illustration, not yet a proof that orbital optimization cannot compress it.

The energy makes the role of the missing terms concrete. Every configuration in the displayed four-dimensional space has diagonal energy two. A matrix element of $`-1`$ connects two configurations that differ by one block flip. In $`\Omega_2`$, the four edges each contribute $`-1/2`$ to the expectation, cancelling the diagonal contribution and giving energy zero.

Compare the normalized two-term state

```math
|C_2\rangle=\frac{|LL\rangle+|RR\rangle}{\sqrt2}.
```

No single-block flip connects its two occupied configurations. Hence $`\langle B_1+B_2\rangle_{C_2}=0`$, and its energy is two. Each block has an equal probability of being $`L`$ or $`R`$, but it lacks the local coherence that makes $`M`$ low energy. Equality of local occupation probabilities is therefore insufficient.

A cluster parametrization keeps the required products automatically. Put $`S_j=A_j^\dagger`$, which changes $`L`$ to $`R`$ on block $`j`$, and use the reference $`\vert \Phi_0\rangle=\vert L\rangle^{\otimes m}`$. Because $`S_j^2=0`$ and disjoint even operators commute,

```math
e^{T_{\mathrm{cl}}}|\Phi_0\rangle
=\prod_j(I+S_j)|\Phi_0\rangle,
\qquad T_{\mathrm{cl}}=\sum_jS_j.
```

Multiplying by $`2^{-m/2}`$ gives $`\Omega_m`$. On two blocks, the factor $`S_1S_2`$ generates $`RR`$. A global linear truncation $`I+S_1+S_2`$ omits that term even though both local pair excitations were retained. This illustrates the product-completion issue behind size consistency. It does not say every CI truncation fails identically or that general coupled-cluster equations solve the perturbed model exactly.

The compact cluster identity, a product of geminals, and a constant-bond-dimension tensor description all remain available here. The theorem constrains an explicit global linear Gaussian expansion, not those other descriptions. [Algorithmic scope](../science/algorithmic_scope.md#easy-preparation-and-classical-alternatives).

<a id="energy-versus-fidelity"></a>

## 6. Small energy density need not mean a large ground-state overlap

For normalized pure states, squared overlap $`\vert \langle\phi\vert \psi\rangle\vert ^2`$ is a probability and lies between zero and one. It is one for the same state up to phase and zero for orthogonal states. Energy density asks a different question: how much local excitation energy is present on average?

For an exact example, let $`\vert v\rangle=\vert 1010\rangle`$. It is orthogonal to $`M`$ and has block energy one. Define, for $`0\le e\le1`$,

```math
|u_e\rangle=\sqrt{1-e}\,|M\rangle+\sqrt e\,|v\rangle.
```

The two components are orthogonal eigenstates of $`h`$, so $`\langle h\rangle_{u_e}=e`$. The product of $`m`$ such blocks has

```math
\frac{\langle H_0\rangle_{u_e^{\otimes m}}}{m}=e,
\qquad
|\langle\Omega_m|u_e^{\otimes m}\rangle|^2=(1-e)^m.
```

At any fixed positive $`e`$, the global overlap tends to zero even though the energy per block stays small. An even simpler state with exactly one block replaced by $`v`$ is orthogonal to $`\Omega_m`$ and has total energy one. Thus a theorem about approximating only $`\Omega_m`$ at a fixed small vector error cannot, by itself, constrain every low-energy state.

The project addresses that gap by controlling overlaps with the desired state on **every subset of blocks**, then combining those controls into an energy statement. The proof imposes no product assumption on the low-energy state being bounded. The products above only illustrate the distinction between the two accuracy criteria.

<a id="imported-ingredients"></a>

## 7. The research ingredients beyond the review

The block $`M`$ is Gaussian-unitarily equivalent to $`G=(\vert 0000\rangle+\vert 1111\rangle)/\sqrt2`$. For example, with Majorana operators $`\gamma_1=a_1+a_1^\dagger`$ and $`\gamma_4=i(a_2^\dagger-a_2)`$, the Gaussian unitary $`W=-i\gamma_1\gamma_4`$ maps $`G`$ to $`M`$. It changes particle number but preserves Gaussian rank. This mathematical change of variables does not make the physical preparation free. The [model](../science/model.md#exact-equivalence-to-the-standard-fermionic-magic-state) checks the signs.

The load-bearing imported statements are:

| Research input | Exact role |
| --- | --- |
| [RS24, Lemma 1, Eqs. (10)–(12)](https://arxiv.org/html/2407.20934v1) | The maximal squared overlap of a pure Gaussian with $`M^{\otimes s}`$ is $`2^{-s}`$. |
| [RS26, Theorem 2, Eqs. (5)–(7), and §IV](https://arxiv.org/html/2610.03699v1) | A uniform approximate Gaussian-rank bound, including unnormalized approximants and errors approaching one. |
| [Bravyi05, Gaussian operations](../references/related_work.md#Bravyi05) | Occupation postselection preserves a pure Gaussian branch, up to normalization and removal of measured modes. |
| [WWLL26, Theorem 12, Eq. (74)](https://arxiv.org/html/2610.02172v1) | A stronger inherited asymptotic rank input, with an unspecified absolute constant. |

These specialized theorems are not made elementary by the review's introduction. The following sections explain how this project uses them. [The source audit](../references/related_work.md) records exact versions and boundaries.

<a id="orthogonal-bound"></a>

## 8. From subset fidelity to an orthogonal configuration bound

First take a single pure Gaussian state $`g`$ on all $`4m`$ modes. Retain a subset $`S`$ of $`s`$ complete blocks and measure all complementary modes in the occupation basis. In each nonzero branch, the retained normalized state is Gaussian. The imported fidelity identity bounds its squared overlap with $`M^{\otimes s}`$ by $`2^{-s}`$. Averaging over the branch probabilities gives

```math
\langle g|P_S|g\rangle\le2^{-s},
\qquad P_S=\prod_{j\in S}P_j.
```

The Gaussian state may have correlations across all blocks. Conditioning is what makes a global target theorem applicable to each subset.

Introduce a nonnegative parameter $`\beta`$ and the positive operator $`e^{-\beta D_m}`$. An eigenstate with $`d`$ defects receives weight $`e^{-\beta d}`$, so fewer defects receive larger weight. This is a proof device; no filtering circuit, imaginary-time evolution, or postselection success probability is being assumed as a computational resource.

The block projectors commute, and therefore

```math
e^{-\beta D_m}
=e^{-\beta m}\prod_{j=1}^{m}[I+(e^\beta-1)P_j].
```

Every coefficient is nonnegative. Applying the subset bound to every term in the expansion yields

```math
\langle g|e^{-\beta D_m}|g\rangle
\le\left(\frac{1+e^{-\beta}}2\right)^m.
```

Now let $`\psi`$ lie in a span of $`K`$ orthonormal Gaussian vectors. A positive operator's expectation in one normalized vector cannot exceed its trace over a containing subspace. Summing the preceding bound over the orthonormal basis gives

```math
\langle e^{-\beta D_m}\rangle_\psi
\le K\left(\frac{1+e^{-\beta}}2\right)^m.
```

If $`\langle D_m\rangle_\psi\le em`$, scalar convexity supplies the other side:

```math
e^{-\beta em}
\le e^{-\beta\langle D_m\rangle_\psi}
\le\langle e^{-\beta D_m}\rangle_\psi.
```

The last step is Jensen's inequality applied to the ordinary probability distribution of defect eigenvalues. It is not a claim about the matrix exponential preserving order for noncommuting operators.

Combining the inequalities and optimizing $`\beta\ge0`$ gives

```math
\boxed{\ln K\ge m[\ln2-h_{\mathrm{bin}}(e)]},
\quad
h_{\mathrm{bin}}(e)=-e\ln e-(1-e)\ln(1-e),
\quad 0\le e\lt \tfrac12.
```

For $`0\lt e\lt 1/2`$, the choice is $`\beta=\ln[(1-e)/e]`$. At $`e=0`$, take a limit. All logarithms are natural, and $`0\ln0=0`$. The rate vanishes at $`e=1/2`$; this proof gives no positive rate above it.

The threshold has a concrete meaning. The determinant

```math
|g_\star\rangle
=\frac{(a_1^\dagger+a_3^\dagger)(a_2^\dagger+a_4^\dagger)}2|\mathrm{vac}\rangle
```

has two particles and $`\langle B\rangle=1/2`$, so its energy is $`1/2`$ per block. Its product is a single global determinant. The $`K=1`$ lower bound shows it is optimal among all Gaussian states. More generally,

```math
\frac{E_{\mathcal S}(H_0)}m
\ge\frac12-\sqrt{\frac{\ln K}{2m}}.
```

Thus if $`\ln K=o(m)`$, meaning that $`\ln K/m`$ tends to zero, the best orthogonal expansion still has energy density tending to $`1/2`$. Recovering a fixed positive fraction of the correlation energy below that determinant floor requires exponentially many configurations. When the displayed lower bound becomes negative, it is simply weaker than the nonnegative-energy bound. The exact theorem permits any orthonormal Gaussian basis, not just one common orbital rotation. [Proof and sharp endpoints](../science/orthogonal_configurations.md).

<a id="weak-overlap"></a>

## 9. Why very weak overlap is the key to nonorthogonal sums

The trace step above fails for a nonorthogonal list. Its vectors are not an orthonormal basis for its span, and orthogonalizing them usually produces non-Gaussian vectors. Large cancelling coefficients make a simple term-by-term overlap estimate inadequate.

Instead import the following approximate-rank statement. Set

```math
R=\frac{27(8+2\sqrt7)}{256},
\qquad c_s=\frac{8R^s}{9(s+1)}.
```

If a sum of $`K`$ Gaussian terms approximates $`M^{\otimes s}`$ with vector error less than $`r`$, where $`0\lt r\lt 1`$, RS26 gives $`K\ge(1-r^2)c_s`$. The approximating sum need not be normalized, and the factor is uniform as $`r`$ approaches one.

To see why those qualifications matter, let $`\chi`$ be any normalized rank-at-most-$`K`$ state and define $`z=\langle\chi\vert M^{\otimes s}\rangle`$. The vector $`z\chi`$ has the same rank bound. It is the projection of the target onto the line through $`\chi`$, so Pythagoras gives

```math
\|M^{\otimes s}-z\chi\|_2^2=1-|z|^2.
```

If $`z=0`$, the overlap bound below is immediate. Otherwise choose an error radius $`r`$ with $`\sqrt{1-\vert z\vert ^2}\lt r\lt 1`$, apply the imported theorem, and let $`r`$ decrease to $`\sqrt{1-\vert z\vert ^2}`$. Unit overlap is covered by taking $`r`$ down to zero. The result is

```math
|\langle M^{\otimes s}|\chi\rangle|^2
\le\frac{K}{c_s}
=\frac98K(s+1)R^{-s}.
```

Even an exponentially small overlap is now controlled. For such an overlap, the residual error is very close to one; a theorem valid only at one fixed small approximation error would not support the argument. Normalizing $`z\chi`$ would also destroy the residual formula. This is the precise bridge from global approximation to weak overlap, not an assumption that every low-energy state resembles the exact ground state. [Canonical lemma](../science/gaussian_rank.md#rank-controls-even-very-small-target-overlap).

<a id="rank-energy"></a>

## 10. From weak overlap to every low-energy state

Measure complementary occupations as before, now starting from a $`K`$-term nonorthogonal Gaussian sum. Each branch remains a sum of at most $`K`$ Gaussian terms because the measurement acts linearly on every summand. Normalizing a nonzero branch does not change that count. If branch $`y`$ has probability $`p_y`$, its normalized overlap bound is multiplied by $`p_y`$ when the branches are averaged. Consequently,

```math
\langle P_S\rangle_\psi
\le\frac98K(|S|+1)R^{-|S|}.
```

No rare branch receives a free amplification factor. The same positive expansion, using $`\vert S\vert +1\le m+1`$, gives

```math
\langle e^{-\beta D_m}\rangle_\psi
\le\frac98K(m+1)[(1-q)+qe^{-\beta}]^m,
\qquad q=1-R^{-1}\approx0.286650896.
```

The binomial-shaped expression follows from summing subsets. It does not assert that the blocks of $`\psi`$ are independent or that its defects follow a binomial distribution.

For a normalized $`\psi`$ satisfying $`\langle\psi\vert D_m\vert \psi\rangle\le em`$ with $`0\le e\lt q`$, combine this upper bound with Jensen's lower bound and optimize to obtain

```math
\boxed{\underline\chi_G(\psi)\ge B_m(e)
:=\frac8{9(m+1)}\exp[m\,d(e\|q)]},
\qquad 0\le e\lt q,
```

where

```math
d(e\|q)=e\ln\frac e q+(1-e)\ln\frac{1-e}{1-q}.
```

This binary relative entropy is positive for fixed $`e\lt q`$. It quantifies the mismatch between the demanded low defect density and the positive-filter bound. The optimizing parameter is $`\beta=\ln[q(1-e)/(e(1-q))]`$ for $`0\lt e\lt q`$. At zero energy the formula reduces to the imported target bound. At or above $`q`$, this optimization supplies no positive exponential rate; one cannot continue the positive relative-entropy expression into that region.

The derivation first treats exact rank. To include border rank, take a convergent sequence of rank-at-most-$`K`$ vectors at fixed $`m`$. After normalization, expectations of each bounded filter converge. The same filter inequality therefore holds in the limit. This is continuity at each fixed system size, not a promise that an arbitrary nonzero global approximation error leaves energy unchanged.

The WWLL26 input yields the analogous bound $`c\exp[m\,d(e\Vert 100/343)]`$ for $`e\lt 100/343`$, with an unspecified absolute $`c>0`$. Its stronger exponent is inherited; the energy argument is the same. The explicit $`B_m(e)`$ is convenient for finite-size certificates. Neither threshold is asserted to be the optimal unrestricted-rank frontier. Near a threshold or at small $`m`$, the finite bound can be trivial. [Full proof and endpoints](../science/gaussian_rank.md#low-energy-theorem).

<a id="connected-family"></a>

## 11. Connecting the blocks without changing the accuracy comparison

A disconnected product is useful for proving the mechanism. The result also applies to a finite-range connected family. Add nearest-block hopping,

```math
V_\lambda=\lambda\sum_{j=1}^{m-1}
(a_{4j}^\dagger a_{4j+1}+a_{4j+1}^\dagger a_{4j}),
\qquad H_\lambda=H_0+V_\lambda.
```

Each link has norm one, so $`\Vert V_\lambda\Vert \le\vert \lambda\vert (m-1)`$. For nonzero $`\lambda`$ and $`m\ge2`$, the interaction graph is connected. The links conserve total particle number and do not commute with $`H_0`$.

More generally, suppose $`H=H_0+V`$ and $`\Vert V\Vert \le\delta m`$. The norm bound means that $`V`$ changes any normalized state's mean energy by at most $`\delta m`$. Since the unperturbed ground energy is zero,

```math
-\delta m\le E_0(H)\le\delta m.
```

A state meeting $`\langle H\rangle\le E_0(H)+\epsilon m`$ therefore obeys

```math
\langle D_m\rangle\le\langle H_0\rangle
=\langle H\rangle-\langle V\rangle
\le(\epsilon+2\delta)m.
```

The explicit trial $`\Omega_m`$ also satisfies

```math
\langle H\rangle_{\Omega_m}-E_0(H)\le2\delta m.
```

Choose $`2\delta\le\epsilon\lt q-2\delta`$. Then this easy trial meets the requested error $`\epsilon m`$, while every Gaussian expansion meeting the same error needs at least $`B_m(\epsilon+2\delta)`$ terms. For example, $`\delta=1/32`$ and $`\epsilon=1/8`$ give $`e=3/16\lt q`$. The orthogonal theorem instead requires $`\epsilon+2\delta\lt 1/2`$ and has its stronger exponent.

The interaction strength is fixed as $`m`$ grows. The comparison does not assume a perturbed spectral gap, high ground-state fidelity, or efficient exact preparation of the perturbed ground state. For the displayed hopping, the product trial's hopping expectation is zero and its error guarantee improves to $`\vert \lambda\vert (m-1)`$; the uniform $`2\delta m`$ estimate already establishes the common target. [Perturbation proof](../science/perturbations.md).

<a id="local-certification"></a>

## 12. Learning a representation bound from local measurements

Suppose a physical source supplies independent copies of the same state $`\rho`$. A density operator describes a pure state or a statistical mixture; its expectation of $`H`$ is $`\mathrm{Tr}(\rho H)`$, where the trace sums diagonal matrix entries. For each copy, choose a block $`J`$ uniformly using classical randomness and measure $`h_J`$. The outcome $`X`$ belongs to $`\{0,1,2,5\}`$, and

```math
\mathbb E[X]=\frac1m\sum_j\mathrm{Tr}(\rho h_j)
=\frac{\mathrm{Tr}(\rho H_0)}m=:e_\rho.
```

One observation estimates the density, not the total energy. Its range stays five as the system grows. With sample mean $`\widehat e`$, choose

```math
T_{\mathrm{copies}}\ge
\left\lceil\frac{25}{2\eta^2}\ln\frac1\alpha\right\rceil.
```

The one-sided Hoeffding bound then gives $`e_\rho\le e_U:=\widehat e+\eta`$ with confidence at least $`1-\alpha`$. Here $`\eta`$ is a statistical margin and $`\alpha`$ is the permitted failure probability. [Hoeffding's original theorem](../references/related_work.md#Hoeffding63) supplies this confidence statement; the review's energy-averaging discussion motivates the measurement setting but does not state this project-specific formula.

For a known pure source, $`e_U\lt q`$ certifies $`\underline\chi_G(\psi)\ge\lceil B_m(e_U)\rceil`$ on that confidence event. An upper confidence bound $`e_U\ge q`$ produces no positive exponential certificate through this formula; it is not evidence of low rank. The four-mode measurement can be implemented by undoing the pair rotation and then measuring occupations. Its non-Gaussian local gate is charged.

For a concrete confidence-to-density conversion, suppose the copy count satisfies the bound with $`\eta=0.05`$ and $`\alpha=0.05`$, and the observed mean is at most $`0.10`$. Then $`e_U\le0.15\lt q`$: the pure-state certificate is at least $`\lceil B_m(0.15)\rceil`$ with confidence at least $`95\%`$. It uses the upper margin $`0.15`$, not the smaller observed mean, and it certifies a positive asymptotic rate without promising a nontrivial finite-size value for every $`m`$.

For a mixed source, define $`\mathcal C_{m,K}`$ to be the **closed convex hull** of pure states with Gaussian border rank at most $`K`$: mixtures of such states, including limits. Linearity extends the filter upper bound to this class. Jensen applies to the probability distribution obtained by measuring $`D_m`$ in $`\rho`$. Thus

```math
e_U\lt q,\quad K\lt B_m(e_U)
\quad\Longrightarrow\quad
\rho\notin\mathcal C_{m,K}
```

with the same confidence. This excludes a representation entirely built from low-rank pure components. It does not say that every component in every decomposition has large rank, or that $`\rho`$ has large ordinary matrix rank. [Precise statistical and mixed-state guarantees](../science/local_certification.md).

Quadratic data alone cannot replace this energy measurement. For $`m\ge2`$, the product $`\Omega_m`$ and the two-determinant state

```math
|C_m\rangle=(|L\rangle^{\otimes m}+|R\rangle^{\otimes m})/\sqrt2
```

both have $`\langle a_r^\dagger a_s\rangle=\delta_{rs}/2`$ and $`\langle a_ra_s\rangle=0`$. Yet their $`H_0`$ energies are zero and $`m`$, respectively. The cat state's global coherence disappears from a single block when other blocks are ignored, while the product retains the pair coherence in every block. The cat has Gaussian rank at most two, whereas the product's rank grows exponentially. The local two-body energy accesses the missing coherence. At $`m=1`$ the states coincide, so the restriction matters.

Measuring $`H_0`$ certifies this representation property. It does not by itself determine the ground energy of $`H_\lambda`$ or establish proximity to its ground state; that comparison uses the deterministic inequalities in Section 11.

<a id="resource-contract"></a>

## 13. Preparation, copies, and explicit output size

The known trial needs no variational search. From $`\vert L\rangle`$ on each block apply

```math
U_j=\exp\!\left[\frac\pi4(A_j^\dagger-A_j)\right],
```

which produces $`M`$. This is one fixed four-mode, quartic, number-conserving gate per block. Alternatively, from four empty occupation qubits, one Hadamard, three CNOTs, and two $`X`$ gates prepare the same block exactly. That Clifford circuit may leave the fixed-particle sector during its intermediate steps. Both constructions use $`O(m)`$ gates and constant parallel block depth on $`4m`$ modes or qubits, with local routing charged when needed.

The unitary excitation form resembles the review's Eq. (69), but the present gate count follows from the explicit disjoint-block construction. It does not assume arbitrary unitary coupled-cluster states are easy to simulate classically or prepare exactly at no cost.

| Resource | Contract in this project |
| --- | --- |
| Hamiltonian input | $`O(m)`$ explicit bounded-support terms with specified coefficients; no arbitrary amplitude loading. |
| State source | One full $`4m`$-mode copy per observation; an unknown source's preparation cost is additional. |
| Known trial preparation | $`O(m)`$ gates per copy; $`O(T_{\mathrm{copies}}m)`$ gates for all copies. |
| Measurement | One fixed four-mode operation per copy under direct block access; routing is additional. |
| Classical work for the certificate | Generate a block index and accumulate bounded outcomes; no reconstruction of the full wavefunction. |
| Successful explicit Gaussian expansion | At least the proved number $`K`$ of global terms, plus their orbital/coefficient descriptions and precision costs. |
| Coherent access | No inverse preparation, controlled preparation, amplitude oracle, or QRAM is assumed free or required by this certificate. |

A copy count independent of $`m`$ at fixed $`\eta,\alpha`$ is compatible with extensive total preparation work. Conversely, an exponential number of required configurations is not automatically an exponential shot lower bound: recovery or product completion can create configurations that were not individually sampled. It also does not automatically prove quadratic matrix storage or cubic solver time, because implicit and iterative methods may avoid those operations.

QSCI, SQD, or nonorthogonal determinant methods are constrained when their final successful output belongs to the stated global linear representation. Granting exact sampling, optimal orbitals, and exact projected diagonalization cannot overcome an obstruction already present in that output class. Keeping a compact product, cluster expression, geminal description, or tensor network changes the representation being counted. The [algorithmic scope](../science/algorithmic_scope.md) states these boundaries precisely.

<a id="scope"></a>

## 14. The integrated conclusion and routes to the proofs

The result establishes a local energy criterion that forces a large global Gaussian expansion. The physical state can still be prepared with a small circuit and described by compact correlated factors. The orthogonal theorem gives a sharp asymptotic energy floor of one half per block for subexponential configuration spaces. The unrestricted theorem handles arbitrary nonorthogonal terms and border rank, with a smaller certified density threshold. Weak fixed couplings preserve the comparison at the same requested accuracy, and local measurements can certify the representation obstruction under stated source and measurement assumptions.

This is a worst-case theorem for an explicit family and a specified representation class. It is not a proof of general classical hardness, an unrestricted quantum advantage, failure of every chemistry instance, or a circuit-depth lower bound. The supplied examples are classically tractable when their product structure is retained. The distinction between easy preparation and costly linear representation is the scientific content.

| To inspect | Canonical project document |
| --- | --- |
| Signs, spectrum, Gaussian equivalence, and exact preparation | [Model](../science/model.md) |
| Subset fidelity, orthogonal trace bound, and optimal determinant | [Orthogonal configurations](../science/orthogonal_configurations.md) |
| Uniform rank input, weak overlap, conditioning, and energy lift | [Gaussian rank](../science/gaussian_rank.md) |
| Equal accuracy and a connected noncommuting family | [Perturbations](../science/perturbations.md) |
| Finite confidence, mixtures, and the covariance counterexample | [Local certification](../science/local_certification.md) |
| Algorithms and charged resources | [Algorithmic scope](../science/algorithmic_scope.md) |
| Exact primary versions and prior-work distinctions | [Related work](../references/related_work.md) |

The selected review supplies the common language for entering this account. The specialized imported results remain attributed, and the proofs linked here establish the additional local-energy conclusion.
