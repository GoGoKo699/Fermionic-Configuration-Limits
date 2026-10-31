# Orthogonal Gaussian configurations at fixed energy density

For the [explicit Hamiltonian $H_0$](model.md), no subexponential orthogonal Gaussian expansion can improve the limiting energy density below the best single Slater determinant. This remains true after arbitrary global orbital optimization and arbitrary selection of the configurations.

The assumption that the configurations are orthogonal is used explicitly. [The general Gaussian-rank theorem](gaussian_rank.md) covers nonorthogonal expansions, with a smaller energy threshold. The threshold $1/2$ proved here must not be transferred to that larger representation class.

## Representation and accuracy

A selected configuration space has the form

$$
\mathcal S=\operatorname{span}\{U_G\lvert x\rangle:x\in X\},
\qquad K=\#X,
\tag{1}
$$

where $U_G$ is any orbital rotation on all $4m$ modes and $X$ is any selected set of occupation strings. Its variational energy is

$$
E_{\mathcal S}(H_0)
=\min_{\substack{\psi\in\mathcal S\\\langle\psi\vert\psi\rangle=1}}
\langle\psi\vert H_0\vert\psi\rangle.
\tag{2}
$$

The theorem allows the more general case in which $\mathcal S$ has any orthonormal basis $g_1,\ldots,g_K$ of pure fermionic Gaussian states. They need not share one orbital transformation. Both parity sectors and general Bogoliubov transformations are allowed, so the result also covers the narrower fixed-particle Slater-determinant model.

There is no restriction on how the orbitals or configurations are chosen. They may be optimized with complete knowledge of $H_0$ and the exact ground state. Sampling can be perfect, amplified, or replaced by an omniscient selector. The parameter $K$ counts the final explicit variational configurations, including configurations added by classical augmentation or Cartesian-product reconstruction. It is not merely the number of raw quantum samples.

The target is energy at most $em$, with a constant density $e$. Since every block contains four modes, this is a fixed energy-per-mode accuracy, not a total-energy tolerance that vanishes as the system grows.

## The imported Gaussian-fidelity identity

For a normalized fixed-parity state $\phi$, write

$$
F_G(\phi)=\max_{g\ {m pure\ Gaussian}}
\bigl|\langle g\vert\phi\rangle\bigr|^2.
$$

[RS24, Lemma 1, Eqs. (10)–(12)](../references/README.md#rs24) proves multiplication by $1/2$ when one appends the standard four-mode maximally non-Gaussian state. Iteration and the exact Gaussian equivalence in [the model](model.md#exact-equivalence-to-the-standard-fermionic-magic-state) give

$$
F_G(M^{\otimes s})=2^{-s}.
\tag{3}
$$

The [versioned primary source](https://arxiv.org/html/2407.20934v1) is the source of this identity. It is not a result proved here. Only this specific maximally non-Gaussian orbit is needed; no general multiplicativity claim for arbitrary Gaussian fidelities is assumed.

### Lemma 1: the same bound controls every retained block subset

For every pure Gaussian $g$ on all $4m$ modes and every subset $S$ of blocks,

$$
\left\langle g\left|\prod_{j\in S}P_j\right|g\right\rangle
\le 2^{-\#S}.
\tag{4}
$$

**Proof.** Move the retained blocks first by a fermionic mode permutation. Such a permutation is Gaussian. The target block projectors are even, so their expectation agrees with the ordinary product projector onto $M^{\otimes\#S}$ in this ordered factorization.

Measure every complementary mode in the occupation basis. In each nonzero branch, a pure Gaussian input becomes a pure Gaussian conditional state on the retained modes. This closure under occupation postselection is a standard fermionic-Gaussian property; see [Bravyi05](../references/README.md#bravyi05), or the explicit statement preceding Lemma 2 of [RS26](https://arxiv.org/html/2610.03699v1).

Equation (3) bounds the target overlap of every normalized branch by $2^{-\#S}$. Averaging over the branch probabilities proves (4). Odd-parity branches have zero overlap with the even target and satisfy the same bound. The empty subset gives equality one. $\square$

No spatial locality or block-product assumption is imposed on $g$; its Gaussian correlations can extend across all modes.

## A Gaussian heat-kernel bound

### Lemma 2

For every $\beta\ge0$ and every pure Gaussian $g$,

$$
\langle g\vert e^{-\beta D_m}\vert g\rangle
\le\left(\frac{1+e^{-\beta}}2\right)^m.
\tag{5}
$$

**Proof.** The projectors $P_j$ commute and $D_m=\sum_j(I-P_j)$. Hence

$$
e^{-\beta D_m}
=e^{-\beta m}\prod_{j=1}^m
\left[I+(e^\beta-1)P_j\right].
$$

Every coefficient in this product expansion is nonnegative. Applying (4) term by term gives

$$
\begin{aligned}
\langle g\vert e^{-\beta D_m}\vert g\rangle
&\le e^{-\beta m}
\sum_{S\subseteq[m]}\left(\frac{e^\beta-1}2\right)^{\#S}\\
&=\left(\frac{1+e^{-\beta}}2\right)^m.
\end{aligned}
$$

This proves (5). $\square$

The same bound holds with $H_0$ in place of $D_m$. Indeed, these two operators commute and $H_0\ge D_m$, so their common eigenbasis gives $e^{-\beta H_0}\le e^{-\beta D_m}$. This use of a common eigenbasis is essential; no operator-monotonicity claim for the exponential of arbitrary noncommuting matrices is needed.

## The orthogonal configuration theorem

### Theorem 3

Let $\mathcal S$ be spanned by $K$ orthonormal pure Gaussian states. If a normalized $\psi\in\mathcal S$ satisfies

$$
\langle\psi\vert H_0\vert\psi\rangle\le em,
\qquad 0\le e<\frac12,
$$

then

$$
\boxed{\log K\ge m[\log2-h(e)]},
\qquad
h(e)=-e\log e-(1-e)\log(1-e).
\tag{6}
$$

All logarithms are natural, with $0\log0=0$.

**Proof.** Since $D_m\le H_0$, the defect expectation is at most $em$. Scalar Jensen applied to the spectral probability distribution of $D_m$ yields

$$
e^{-\beta em}
\le e^{-\beta\langle D_m\rangle_\psi}
\le\langle\psi\vert e^{-\beta D_m}\vert\psi\rangle.
\tag{7}
$$

Let $\Pi_{\mathcal S}$ be the orthogonal projector onto the selected space. The operator $\Pi_{\mathcal S}-\lvert\psi\rangle\langle\psi\rvert$ is positive. Consequently, positivity of the heat kernel and (5) give

$$
\begin{aligned}
\langle\psi\vert e^{-\beta D_m}\vert\psi\rangle
&\le\operatorname{Tr}(\Pi_{\mathcal S}e^{-\beta D_m})\\
&=\sum_{i=1}^K\langle g_i\vert e^{-\beta D_m}\vert g_i\rangle\\
&\le K\left(\frac{1+e^{-\beta}}2\right)^m.
\end{aligned}
\tag{8}
$$

The equality in the second line uses an **orthonormal** Gaussian basis. An arbitrary nonorthogonal list cannot replace it.

Combining (7) and (8) gives, for every $\beta\ge0$,

$$
\log K\ge m\left[-\beta e-
\log\left(\frac{1+e^{-\beta}}2\right)\right].
$$

For $0<e<1/2$, choose $\beta=\log[(1-e)/e]$. The expression in brackets is $\log2-h(e)$. At $e=0$, take the limit $\beta\to\infty$. $\square$

At and above $e=1/2$, optimizing over nonnegative $\beta$ gives only exponential rate zero; the positive relative-entropy expression is not asserted there. At $e=0$, the bound is $K\ge2^m$, attained by the $2^m$ occupation configurations in the exact product-pair expansion.

The same proof holds for a density operator supported in $\mathcal S$: use scalar Jensen for its spectral probability distribution and $0\le\rho\le\Pi_{\mathcal S}$. This is a statement about one orthogonal configuration space. Statements about convex mixtures of general bounded-rank states are treated separately in [local certification](local_certification.md#mixed-state-guarantee).

### Corollary 4: an explicit energy floor

For every such space,

$$
\boxed{\frac{E_{\mathcal S}(H_0)}m
\ge\frac12-\sqrt{\frac{\log K}{2m}}.}
\tag{9}
$$

If the variational energy density is already at least $1/2$, this is immediate. Otherwise apply (6) and the binary Pinsker inequality

$$
\log2-h(e)=D_{\rm KL}(e\Vert1/2)
\ge2(1/2-e)^2.
$$

The right-hand side of (9) can be negative for large $K$; in that case it is simply a weak bound, compatible with $H_0\ge0$.

## The best determinant and the sharp asymptotic floor

The occupied orbitals

$$
b_1^\dagger=\frac{a_1^\dagger+a_3^\dagger}{\sqrt2},
\qquad
b_2^\dagger=\frac{a_2^\dagger+a_4^\dagger}{\sqrt2}
$$

are orthonormal. Their Slater determinant is

$$
\begin{aligned}
\lvert g_\star\rangle
&=b_1^\dagger b_2^\dagger\lvert0\rangle\\
&=\frac{\lvert1100\rangle+\lvert1001\rangle
-\lvert0110\rangle+\lvert0011\rangle}{2}.
\end{aligned}
\tag{10}
$$

Its particle number is two and $\langle T\rangle=1/2$, so $\langle h\rangle=1/2$. More explicitly,

$$
\lvert g_\star\rangle
=\frac{\lvert M\rangle+\lvert v\rangle}{\sqrt2},
\qquad
\lvert v\rangle=\frac{\lvert1001\rangle-\lvert0110\rangle}{\sqrt2},
\qquad h\lvert v\rangle=\lvert v\rangle.
$$

Thus

$$
\langle g_\star\vert e^{-\beta h}\vert g_\star\rangle
=\frac{1+e^{-\beta}}2.
\tag{11}
$$

The product of these determinants is a single global Slater determinant. It has energy $m/2$ and saturates the Gaussian heat-kernel bound for $H_0$ at every $\beta\ge0$. The $K=1$ case of (9) proves that no Gaussian state, including one with global orbital correlations, has lower energy.

Let $E_K^{\rm orth}(m)$ be the infimum of (2) over all admissible spaces of dimension $K$. A space can include this determinant, so $E_K^{\rm orth}(m)\le m/2$ for $K\ge1$. Therefore, for every sequence with $\log K_m=o(m)$,

$$
\lim_{m\to\infty}\frac{E_{K_m}^{\rm orth}(m)}m=\frac12.
\tag{12}
$$

The exact ground energy is zero. Hence no subexponential orthogonal Gaussian expansion recovers a fixed positive fraction of the extensive correlation energy beyond the best determinant. This concerns the optimum over all orbital choices and selections; a poorly chosen space can of course have higher energy.

Equations (11) and (12), and the zero-energy endpoint of (6), are sharp statements. No claim that (6) gives the optimal finite-$K$ frontier at every intermediate density is made.

## Relation to unrestricted Gaussian rank

A nonorthogonal Gaussian expansion can have arbitrary coefficient cancellations. Orthogonalizing its span generally produces non-Gaussian vectors, so (8) cannot be applied to its original number of terms.

[The companion theorem](gaussian_rank.md#low-energy-theorem) instead imports an approximate-rank lower bound and uses Gaussian conditioning before the heat-kernel step. With

$$
R=\frac{27(8+2\sqrt7)}{256},\qquad q=1-R^{-1},
$$

it proves exponential unrestricted Gaussian border rank at every fixed defect density below $q\approx0.28665$. The present orthogonal theorem has the stronger threshold $1/2$ and no polynomial prefactor, but applies to the smaller representation class.

Neither theorem rules out efficient product, geminal, tensor-network, or coupled-cluster descriptions, nor methods that compute observables without outputting a small global Gaussian expansion. The [algorithmic scope](algorithmic_scope.md) makes these boundaries explicit.
