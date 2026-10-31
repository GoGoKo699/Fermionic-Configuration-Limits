# Gaussian rank at fixed energy density

Every pure state with sufficiently small energy density in the [block model](model.md) requires exponentially many pure fermionic Gaussian terms, even when the terms are nonorthogonal and use different orbitals. This page proves that statement by lifting an existing approximate-rank theorem from a particular tensor-power target to all pure states of low extensive energy.

The imported exponential rank bounds are due to [RS26](../references/README.md#rs26) and [WWLL26](../references/README.md#wwll26). The contribution proved here is the conditional-overlap and positive heat-kernel argument that converts those inputs into an energy-density obstruction. The threshold obtained by this argument is not claimed to be optimal.

## Definitions and conventions

There are $`4m`$ fermionic modes, divided into $`m\ge1`$ consecutive four-mode blocks. We use the occupation convention

```math
|n_1\cdots n_{4m}\rangle
=(a_1^\dagger)^{n_1}\cdots(a_{4m}^\dagger)^{n_{4m}}|\mathrm{vac}\rangle.
```

A normalized pure fermionic Gaussian state is a Gaussian-unitary image of an occupation-basis state. This definition includes both parities and includes particle-number-preserving Slater determinants as a special case. The Gaussian unitary may mix creation and annihilation operators; it need not preserve particle number. Physical pure states can be restricted to a definite parity throughout.

Let $`\mathcal G_n`$ denote the normalized pure Gaussian states on $`n`$ modes. For a nonzero, possibly unnormalized vector $`v`$, its Gaussian rank is

```math
\chi_{\mathrm G}(v)
=\min\left\{K:
v=\sum_{i=1}^{K}a_i g_i,
\quad a_i\in\mathbb C,\quad g_i\in\mathcal G_n
\right\}.
```

We set $`\chi_{\mathrm G}(0)=0`$. No orthogonality, common orbital basis, coefficient bound, or condition-number bound is imposed. Nonzero rescaling leaves the rank unchanged. Gaussian border rank is the corresponding closure notion:

```math
\underline\chi_{\mathrm G}(v)
=\min\left\{K:
v\in\overline{\{w:\chi_{\mathrm G}(w)\le K\}}
\right\},
```

where closure is in the vector $`2`$-norm at fixed mode number. In particular, a border-rank-$`K`$ vector may be a limit of ill-conditioned $`K`$-term sums without itself having an exact $`K`$-term decomposition. Gaussian-unitary invariance holds for both ranks. These conventions agree with Definitions 6–9 in Appendix A.3 of [WWLL26](https://arxiv.org/html/2610.02172v1).

For each block define

```math
|M\rangle=\frac{|1100\rangle+|0011\rangle}{\sqrt2},
\qquad P_j=|M\rangle\langle M|_j,
\qquad D_m=\sum_{j=1}^{m}(I-P_j).
```

Each $`P_j`$ acts as the identity outside its block. The projectors commute and have even fermion parity. The energy parameter below is per four-mode block: $`\langle D_m\rangle/m=e`$. The corresponding density per fermionic mode is $`e/4`$.

The [two-body Hamiltonian](model.md) satisfies $`H_0\ge D_m\ge0`$. Consequently an upper bound on $`\langle H_0\rangle/m`$ is also an upper bound on the defect density used here.

## Uniform approximate-rank input

Set

```math
R=\frac{27(8+2\sqrt7)}{256}
\simeq1.40183816718,
\qquad
c_s=\frac{8R^s}{9(s+1)}.
```

Theorem 2, Eqs. (5)–(7), of [RS26](https://arxiv.org/html/2610.03699v1) states the following for every integer $`s\ge1`$. Put $`\vert G\rangle=(\vert 0000\rangle+\vert 1111\rangle)/\sqrt2`$. If

```math
\left\|G^{\otimes s}-\sum_{i=1}^{K}a_i g_i\right\|_2\lt \delta,
```

then

```math
K\ge (1-\delta^2)c_s.
```

The approximating sum is not required to be normalized. The factor is uniform for $`0\lt \delta\lt 1`$, including $`\delta`$ arbitrarily close to $`1`$. Section IV, Eqs. (81)–(87), verifies this directly: the target flattening has unit singular values, the squared Frobenius error equals its number of columns times the squared vector error, and a $`K`$-term Gaussian sum has bounded flattening rank. No normalization or error-dependent hidden constant enters.

The source's strict-error condition is handled below by taking a limit from larger $`\delta`$; no assertion at a strict radius of zero is needed. If an approximant contains odd-parity Gaussian summands, projection onto the target's even parity discards them, does not increase its error, and does not increase its rank.

### Exact map to the fixed-particle-number block

The source target and our block are Gaussian-unitarily equivalent. Define two Majorana operators on a block by

```math
\gamma_1=a_1+a_1^\dagger,
\qquad
\gamma_4=i(a_2^\dagger-a_2),
\qquad
W=-i\gamma_1\gamma_4.
```

They square to the identity and anticommute, so $`W`$ is unitary. Up to its global phase,

```math
\gamma_1\gamma_4
=\exp\!\left(\frac\pi2\gamma_1\gamma_4\right)
```

is a Gaussian unitary. With the stated occupation convention,

```math
W|0000\rangle=|1100\rangle,
\qquad
W|1111\rangle=|0011\rangle,
\qquad
W|G\rangle=|M\rangle.
```

Applying $`W`$ on every block preserves norm errors and Gaussian ranks. The imported bound therefore holds with $`M^{\otimes s}`$ in place of $`G^{\otimes s}`$. This use of a particle-hole transformation does not assert that the original and transformed states have the same particle number; it establishes their Gaussian-rank equivalence.

## Rank controls even very small target overlap

**Lemma 1.** For every $`s\ge1`$ and every normalized vector $`\chi`$ with $`\chi_{\mathrm G}(\chi)\le K`$,

```math
|\langle M^{\otimes s}|\chi\rangle|^2
\le\frac{K}{c_s}
=\frac98 K(s+1)R^{-s}.
```

**Proof.** Write $`z=\langle\chi\vert M^{\otimes s}\rangle`$. The unnormalized vector $`z\chi`$ has Gaussian rank at most $`K`$, and

```math
\|M^{\otimes s}-z\chi\|_2^2=1-|z|^2.
```

If $`z=0`$, the conclusion is immediate. Otherwise choose any $`\delta`$ strictly between $`\sqrt{1-\vert z\vert ^2}`$ and $`1`$, apply the imported theorem, and let $`\delta`$ decrease to $`\sqrt{1-\vert z\vert ^2}`$. This yields $`K\ge c_s\vert z\vert ^2`$. For unit overlap, take $`\delta\downarrow0`$. The same argument allows a parity projection of the approximant if needed. ∎

Uniformity as $`\delta\to1`$ is essential: the target overlap in this lemma can itself be exponentially small. A theorem limited to a fixed global approximation error would not justify this step.

## Conditioning on complementary modes

Occupation measurements are fermionic Gaussian measurements: conditioning a pure Gaussian state on definite occupations of some modes gives either zero or a scalar multiple of a pure Gaussian state on the remaining modes. This closure property includes removal of the measured modes. See [Bravyi05](../references/README.md#bravyi05) and the discussion preceding Lemma 2 of [RS26](https://arxiv.org/html/2610.03699v1), which explicitly includes computational-basis projectors among the rank-nonincreasing Gaussian operations.

For a block subset $`S\subseteq\{1,\ldots,m\}`$, let $`s=\vert S\vert `$ and

```math
P_S=\prod_{j\in S}P_j,
\qquad P_\varnothing=I.
```

**Lemma 2.** Every normalized $`\psi`$ with $`\chi_{\mathrm G}(\psi)\le K`$ satisfies

```math
\langle\psi|P_S|\psi\rangle
\le\frac98 K(s+1)R^{-s}
\quad\text{for every }S.
```

**Proof.** First suppose $`s\ge1`$. Measure every mode outside $`S`$ in the occupation basis. A Gaussian permutation can bring the selected complete blocks first if they are noncontiguous. Because each target block has even parity, the projector $`P_S`$ acquires no ordering-dependent sign.

For an outcome $`y`$, write the unnormalized conditional vector as

```math
\psi_y=(I_S\otimes\langle y|)\psi,
\qquad p_y=\|\psi_y\|_2^2.
```

Applying this linear contraction term by term to any $`K`$-Gaussian decomposition of $`\psi`$ gives at most $`K`$ nonzero Gaussian terms. If $`p_y>0`$, the normalized conditional vector $`\chi_y=\psi_y/\sqrt{p_y}`$ therefore has Gaussian rank at most $`K`$. Lemma 1 and completeness of the occupation measurement give

```math
\begin{aligned}
\langle\psi|P_S|\psi\rangle
&=\sum_{y:p_y>0}p_y
  |\langle M^{\otimes s}|\chi_y\rangle|^2\\
&\le\sum_y p_y\frac98 K(s+1)R^{-s}\\
&=\frac98 K(s+1)R^{-s}.
\end{aligned}
```

No division by a small branch probability appears in the final bound. If the input has definite parity, each conditional vector also has definite parity. Odd conditional vectors have zero overlap with the even target. More generally, projecting onto the target parity discards wrong-parity Gaussian terms without increasing their number. Zero-probability branches are omitted.

For $`S=\varnothing`$, the left side is $`1`$ and the right side is $`9K/8\ge1`$. This establishes the bound uniformly, including the empty subset. ∎

The lemma treats arbitrary nonorthogonal decompositions. It does not replace their span by a trace over an orthonormal Gaussian basis, which need not exist.

## Low-energy theorem

Define

```math
q=1-\frac1R\simeq0.28665089636
```

and the binary relative entropy, using natural logarithms, by

```math
d(e\|q)
=e\ln\frac e q+(1-e)\ln\frac{1-e}{1-q},
```

with $`0\ln0=0`$.

**Theorem.** Let $`m\ge1`$, let $`\psi`$ be normalized, and let $`0\le e\lt q`$. If

```math
\langle\psi|D_m|\psi\rangle\le em,
```

then

```math
\boxed{
\underline\chi_{\mathrm G}(\psi)
\ge B_m(e)
:=\frac{8}{9(m+1)}\exp\!\big[m\,d(e\|q)\big].
}
```

In particular, the same lower bound holds for exact Gaussian rank. Since the ranks are integers, the right side may be rounded upward. The premise holds whenever $`\langle H_0\rangle\le em`$. Thus the theorem applies in the fixed total-particle-number $`2m`$ sector of the [number-conserving model](model.md), as well as on the full Fock space.

**Proof for exact rank.** Suppose $`\chi_{\mathrm G}(\psi)\le K`$. For every real $`\beta\ge0`$, commutation of the block projectors gives

```math
e^{-\beta D_m}
=e^{-\beta m}\prod_{j=1}^{m}
\big[I+(e^\beta-1)P_j\big].
```

All coefficients in the expansion into $`P_S`$ are nonnegative. Lemma 2 and $`s+1\le m+1`$ imply

```math
\begin{aligned}
\langle e^{-\beta D_m}\rangle_\psi
&\le\frac98 K(m+1)e^{-\beta m}
\sum_{s=0}^{m}\binom ms
\left(\frac{e^\beta-1}{R}\right)^s\\
&=\frac98 K(m+1)
\big[R^{-1}+(1-R^{-1})e^{-\beta}\big]^m\\
&=\frac98 K(m+1)
\big[(1-q)+qe^{-\beta}\big]^m.
\end{aligned}
```

Scalar Jensen's inequality applied to the spectral probability distribution of $`D_m`$ gives

```math
e^{-\beta em}
\le e^{-\beta\langle D_m\rangle_\psi}
\le\langle e^{-\beta D_m}\rangle_\psi.
```

Consequently

```math
\ln K\ge
-\ln\!\left(\frac98(m+1)\right)
+m\left[-\beta e-\ln\big((1-q)+qe^{-\beta}\big)\right].
```

For $`0\lt e\lt q`$, the maximizing nonnegative parameter is

```math
\beta_*=\ln\frac{q(1-e)}{e(1-q)}>0.
```

Substitution makes the expression in square brackets equal to $`d(e\Vert q)`$. At $`e=0`$, let $`\beta\to\infty`$ to obtain the same formula with $`d(0\Vert q)=\ln R`$. This proves the exact-rank bound. ∎

## Border rank and endpoints

If $`\underline\chi_{\mathrm G}(\psi)\le K`$, choose rank-at-most-$`K`$ vectors converging in norm to $`\psi`$. Because $`\psi`$ is normalized, the approximants are eventually nonzero and may be normalized without changing rank. At fixed $`m`$, every operator $`P_S`$ and $`e^{-\beta D_m}`$ is bounded. Their expectations therefore converge. Passing to the limit in Lemma 2 or in the heat-kernel bound proves exactly the same inequalities for border rank. Jensen and the optimization above then apply directly to the limiting state's energy. No uniform-in-$`m`$ continuity assumption is needed.

At zero energy, the theorem reduces to the inherited target bound $`8R^m/[9(m+1)]`$, as expected. At $`e=q`$, optimization over $`\beta\ge0`$ gives $`\beta=0`$ and exponential rate zero. For $`e>q`$, the best nonnegative $`\beta`$ remains zero. Although $`d(e\Vert q)>0`$ again when $`e>q`$, that expression is **not** a valid positive rate from this proof in that regime.

For each fixed $`e\lt q`$, $`d(e\Vert q)>0`$, so the bound is exponential in $`m`$. The finite-size prefactor can make the numerical bound trivial at small $`m`$ or close to $`q`$. Neither $`q`$ nor the exponential rate is asserted to be the exact energy frontier of Gaussian rank.

Border rank concerns limits at fixed system size. It should not be confused with approximating an arbitrary low-energy target to a specified nonzero vector error: that separate claim must also account for the approximant's possible energy change.

## Stronger inherited asymptotic bound

Theorem 12, Eq. (74), of [WWLL26](https://arxiv.org/html/2610.02172v1) supplies an absolute constant $`c>0`$, independent of both $`s\ge1`$ and $`0\le\delta\lt 1`$, for which

```math
\underline\chi_{\mathrm G}^{(\delta)}(G^{\otimes s})
\ge c(1-\delta^2)
\left(\frac{343}{243}\right)^s.
```

Its approximation convention explicitly permits unnormalized vectors; see Appendix A.3, immediately before Definitions 8–9, Eqs. (35)–(36). Decreasing $`c`$ if necessary, take $`0\lt c\le1`$ so that the empty-subset estimate is also valid. Repeating Lemmas 1 and 2 gives

```math
\langle P_S\rangle_\psi
\le\frac Kc\left(\frac{243}{343}\right)^{|S|}.
```

The same heat-kernel proof therefore yields

```math
\boxed{
\underline\chi_{\mathrm G}(\psi)
\ge c\exp\!\left[m\,d\!\left(e\middle\|\frac{100}{343}\right)\right]
\quad\text{if }0\le e\lt \frac{100}{343}.
}
```

This version has a larger certified threshold and no polynomial prefactor, but the cited statement does not specify the absolute constant $`c`$. The fully explicit $`B_m(e)`$ is therefore convenient for finite-size certificates. The improvement in the imported rank exponent belongs to WWLL26; the energy-density lifting step is unchanged. The numerical threshold $`100/343`$ is not claimed optimal either.

## Scope and neighboring results

The [orthogonal-configuration theorem](orthogonal_configurations.md) has the stronger explicit exponent $`\ln2-h(e)`$ for $`e\lt 1/2`$, under its orthogonal-span hypothesis. That hypothesis must not be dropped while retaining its exponent. The present page handles arbitrary nonorthogonal Gaussian decompositions and their limits.

[Local certification](local_certification.md) turns an observed energy density into a finite-confidence rank certificate and states the precise mixed-state extension. [Perturbations](perturbations.md) transfers the result to near-ground states of bounded extensive perturbations by controlling their $`H_0`$ energy.

The obstruction concerns a global linear expansion in Gaussian states. The model also has compact product, tensor-network, and coupled-cluster descriptions. Nothing here is a general classical-computation lower bound, a circuit-depth lower bound, or an obstruction to solving fragments separately.
