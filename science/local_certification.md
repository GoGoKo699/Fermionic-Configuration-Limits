# Certifying a representation obstruction from local energy

A measurement on one classically chosen four-mode block per copy suffices to estimate the energy density of the [model Hamiltonian](model.md). Combining that estimate with the [Gaussian-rank theorem](gaussian_rank.md#low-energy-theorem) certifies an exponential representation requirement at fixed energy slack. The full-state copy count is independent of system size at fixed precision and confidence; preparing those full states is a separate, extensive resource.

## Measurement model

The source supplies $`T`$ independent copies of the same density operator $`\rho`$ on the $`4m`$ modes. The block Hamiltonians are known and have the form

```math
H_0=\sum_{j=1}^{m}h_j,
\qquad
h_j=I-B_j+(N_j-2)^2,
```

where $`B_j=A_j+A_j^\dagger`$ swaps $`\vert 1100\rangle_j`$ and $`\vert 0011\rangle_j`$ with positive amplitude; this is the operator denoted $`T_j`$ on the model page. Their spectra are contained in $`\{0,1,2,5\}`$, so $`0\le h_j\le5I`$. The [model page](model.md) fixes signs and proves this spectrum.

On each fresh copy:

1. Choose a block index $`J`$ uniformly from $`\{1,\ldots,m\}`$ using classical randomness, independently of the source and earlier outcomes.
2. Perform the projective measurement of $`h_J`$ on that block.
3. Record its eigenvalue $`X\in\{0,1,2,5\}`$ and discard the copy.

This measurement is a fixed constant-size operation. To make the implementation explicit, suppress the block index and set

```math
A=a_1^\dagger a_2^\dagger a_4a_3,
\qquad
U=\exp\!\left[\frac\pi4(A-A^\dagger)\right].
```

The unitary $`U`$ takes the symmetric combination of $`\vert 1100\rangle`$ and $`\vert 0011\rangle`$ to $`\vert 1100\rangle`$, and the antisymmetric combination to $`-\vert 0011\rangle`$; it fixes the other occupation states. Apply $`U`$, measure occupations, and assign energy $`0`$ to $`\vert 1100\rangle`$, $`2`$ to $`\vert 0011\rangle`$, and the appropriate remaining diagonal eigenvalues. This is exactly a measurement of $`h`$. The basis change preserves the block's particle number and can be implemented as a fixed four-mode gate or compiled into a constant number of local gates in a universal gate model. Its cost is charged; it is not assumed to be a free Gaussian operation.

The mathematical measurement model is trusted and ideal, and the copies are independent and identically distributed. The confidence statements below concern finite sampling under these assumptions. They are not device-independent statements or bounds on unmodeled preparation and readout errors.

Define the energy density per four-mode block by

```math
e_\rho=\frac{\mathrm{Tr}(\rho H_0)}m.
```

Then each outcome satisfies

```math
0\le X\le5,
\qquad
\mathbb E[X]
=\frac1m\sum_{j=1}^{m}\mathrm{Tr}(\rho h_j)
=e_\rho.
```

No factor of $`m`$ appears in the outcome range. This follows from estimating the density by uniformly sampling a term, rather than treating one measurement as an estimator of the unnormalized total energy.

## Statistical guarantee

Let

```math
\widehat e=\frac1T\sum_{t=1}^{T}X_t.
```

Theorem 2, Eq. (2.6), of [Hoeffding63](../references/README.md#hoeffding63) ([original article, p. 16](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf)) gives, for every $`\eta>0`$,

```math
\Pr\{e_\rho>\widehat e+\eta\}
\le \exp\!\left(-\frac{2T\eta^2}{25}\right).
```

Thus for any failure probability $`0\lt \alpha\lt 1`$, the sufficient integer sample count

```math
\boxed{
T\ge
\left\lceil\frac{25}{2\eta^2}\ln\frac1\alpha\right\rceil
}
```

ensures the one-sided upper confidence bound

```math
e_\rho\le e_U:=\widehat e+\eta
```

with probability at least $`1-\alpha`$. Equivalently, for a prescribed $`T\ge1`$, use

```math
\eta=\sqrt{\frac{25}{2T}\ln\frac1\alpha}.
```

If a two-sided estimate is desired, the corresponding inequality is

```math
\Pr\{|\widehat e-e_\rho|>\eta\}
\le 2\exp\!\left(-\frac{2T\eta^2}{25}\right),
```

and replacing $`\ln(1/\alpha)`$ by $`\ln(2/\alpha)`$ gives sufficient sample size. A rank certificate only needs the one-sided upper bound.

### Pure-state certificate

Suppose the source is known to be pure, $`\rho=\vert \psi\rangle\langle\psi\vert `$. Write

```math
q=1-\frac{256}{27(8+2\sqrt7)},
\qquad
B_m(e)=\frac{8}{9(m+1)}\exp[m\,d(e\|q)],
```

with $`d`$ the binary relative entropy defined on the [proof page](gaussian_rank.md#low-energy-theorem). If the observed upper confidence bound satisfies $`0\le e_U\lt q`$, then, with probability at least $`1-\alpha`$,

```math
\boxed{
\underline\chi_{\mathrm G}(\psi)
\ge\left\lceil B_m(e_U)\right\rceil.
}
```

Indeed, $`D_m\le H_0`$ gives $`\langle D_m\rangle\le e_Um`$ on the confidence event, so the deterministic theorem applies. The same statement holds for exact Gaussian rank. An observed $`e_U\ge q`$ supplies no positive exponential rate through this explicit bound; it is not evidence that the state actually has small rank.

If an orthogonal Gaussian configuration representation is the resource under consideration, the same energy measurement may instead be combined with the [orthogonal-span theorem](orthogonal_configurations.md), using its threshold $`1/2`$ and its distinct exponent. That stronger formula does not certify arbitrary nonorthogonal Gaussian rank.

## Mixed-state guarantee

Purity is not required for a meaningful representation certificate, but the claim must specify the class excluded. For an integer $`K\ge1`$, define

```math
\mathcal C_{m,K}
=\overline{\mathrm{conv}}\left\{
|\psi\rangle\langle\psi|:
\|\psi\|_2=1,
\quad\underline\chi_{\mathrm G}(\psi)\le K
\right\}.
```

This is the closed convex hull of pure states of Gaussian border rank at most $`K`$. Its definition permits different Gaussian decompositions and different orbital choices for different mixture components. It does not identify a density matrix's ordinary matrix rank with a Gaussian resource.

The [heat-kernel bound](gaussian_rank.md#low-energy-theorem) extends to every $`\rho\in\mathcal C_{m,K}`$ by linearity and continuity:

```math
\mathrm{Tr}(\rho e^{-\beta D_m})
\le\frac98K(m+1)
\big[(1-q)+qe^{-\beta}\big]^m
\quad(\beta\ge0).
```

Jensen's inequality also holds for the spectral probability distribution induced by a density operator. If $`e_\rho\le e\lt q`$, then

```math
e^{-\beta em}
\le e^{-\beta\mathrm{Tr}(\rho D_m)}
\le\mathrm{Tr}(\rho e^{-\beta D_m}).
```

The same optimization therefore implies the deterministic restriction

```math
\rho\in\mathcal C_{m,K},\quad e_\rho\le e\lt q
\quad\Longrightarrow\quad K\ge B_m(e).
```

Consequently the observed conditions

```math
e_U\lt q,
\qquad K\lt B_m(e_U)
```

certify, with confidence at least $`1-\alpha`$, that

```math
\boxed{\rho\notin\mathcal C_{m,K}.}
```

The strict inequality on $`K`$ is necessary for this exclusion test. The conclusion says that the state cannot be represented as a mixture supported entirely on pure states with border rank at most $`K`$, even allowing limits of such mixtures. It does not assert that every pure state in every decomposition has large rank, and it does not silently choose an alternative definition of mixed-state Gaussian rank.

For either the pure-state or mixed-state procedure, the probability of reporting an invalid certificate is at most $`\alpha`$. This is the finite-sampling guarantee provided by the common upper-confidence event.

## Covariance does not certify this resource

For $`m\ge2`$, compare

```math
|\Phi_m\rangle=|M\rangle^{\otimes m}
```

with

```math
|C_m\rangle
=\frac{|1100\rangle^{\otimes m}
       +|0011\rangle^{\otimes m}}{\sqrt2}.
```

The two components of $`C_m`$ are occupation-basis Slater determinants, so

```math
\chi_{\mathrm G}(C_m)\le2.
```

Both states have fixed total particle number $`2m`$ and identical two-point data:

```math
\gamma_{rs}=\langle a_r^\dagger a_s\rangle
=\frac12\delta_{rs},
\qquad
\kappa_{rs}=\langle a_ra_s\rangle=0.
```

Every mode is occupied with probability $`1/2`$. Off-diagonal one-body terms cannot connect the relevant occupation strings, and fixed particle number makes anomalous pair expectations vanish. Thus the full fermionic covariance data agree.

Their energies nevertheless differ extensively:

```math
\langle\Phi_m|H_0|\Phi_m\rangle=0,
\qquad
\langle C_m|H_0|C_m\rangle=m.
```

For $`m\ge2`$, tracing out the other blocks of $`C_m`$ eliminates its global coherence, leaving each block in the equal incoherent mixture of $`\vert 1100\rangle`$ and $`\vert 0011\rangle`$. That mixture has $`N_j=2`$, $`\langle B_j\rangle=0`$, and $`\langle h_j\rangle=1`$. In $`\Phi_m`$, each block instead retains $`\langle B_j\rangle=1`$ and has zero energy.

The zero-energy state has exponential Gaussian border rank by the proved bound, whereas $`C_m`$ uses only two Gaussian terms. Any certificate based only on these identical two-point data must treat the states identically; it cannot certify the exponential bound from those data alone. The four-mode energy measurement accesses the necessary two-body coherence. At $`m=1`$ the states coincide, so the restriction $`m\ge2`$ is essential.

## Resource accounting and limits

At fixed $`\eta`$ and $`\alpha`$, the protocol consumes a number of independent full-state copies that is independent of $`m`$. Each copy still contains $`4m`$ fermionic modes. For the explicit state $`\Phi_m`$, one copy requires $`O(m)`$ preparation gates, with constant depth when disjoint blocks can be prepared in parallel. Preparing all $`T`$ copies therefore costs $`O(Tm)`$ gates. The sample bound is not a constant-total-cost preparation claim.

Each copy uses one fixed four-mode measurement circuit and a classical uniformly random block index. With direct access to the selected block, the measurement gate count is $`O(T)`$, in addition to state preparation. Classical index generation costs $`O(\log m)`$ random bits per copy up to constant expected overhead; a running outcome sum and the current index need only $`O(\log T+\log m)`$ classical bits. A physical architecture that requires routing to the selected block must additionally charge that routing. There is no coherent address register, QRAM, or amplitude-loading assumption.

The confidence analysis requires independent copies of the same state and trusted measurements of the stated local terms. It certifies a representation obstruction for that source. It does not certify computational hardness, an advantage over compact product or coupled-cluster descriptions, or a limitation on algorithms that solve fragments separately. Transfer to near-ground states of a connected perturbed Hamiltonian uses the deterministic energy comparison on the [perturbations page](perturbations.md); measuring $`H_0`$ is not by itself a certificate of proximity to the perturbed ground state.
