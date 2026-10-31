# Connected perturbations and equal energy accuracy

The configuration obstruction is stable under an extensive, sufficiently weak perturbation. The comparison uses the same fixed energy-density target for the easy trial state and the restricted configuration representation. It does not require a claim about the perturbed spectral gap or the preparation complexity of the exact perturbed ground state.

## A uniform perturbation theorem

Let $`H_0`$, $`D_m`$, and $`\Omega_m`$ be as in [the model](model.md), and let

```math
H=H_0+V,\qquad V=V^\dagger,\qquad \|V\|\le\delta m.
```

**Equation (1).**

The energy minimum $`E_0(H)`$ may be taken over the full Fock space or over the fixed total-particle-number sector containing $`\Omega_m`$. Use the same space throughout a comparison. The estimates below hold in either case.

### Proposition 1: transfer of energy accuracy

The ground energy obeys

```math
-\delta m\le E_0(H)\le\delta m.
```

**Equation (2).**

Every normalized state with

```math
\langle H\rangle\le E_0(H)+\epsilon m
```

satisfies

```math
\boxed{\langle D_m\rangle\le\langle H_0\rangle\le(\epsilon+2\delta)m.}
```

**Equation (3).**

The fixed trial state $`\Omega_m`$ satisfies

```math
\boxed{\langle H\rangle_{\Omega_m}-E_0(H)\le2\delta m.}
```

**Equation (4).**

**Proof.** Since $`H_0\ge0`$, $`H\ge-\delta mI`$. Evaluating $`H`$ on $`\Omega_m`$ gives an energy at most $`\delta m`$, proving (2). For the low-energy state,

```math
\langle D_m\rangle
\le\langle H_0\rangle
=\langle H\rangle-\langle V\rangle
\le E_0(H)+\epsilon m+\delta m
\le(\epsilon+2\delta)m.
```

Finally $`\langle H\rangle_{\Omega_m}\le\delta m`$ and $`E_0(H)\ge-\delta m`$ prove (4). $`\square`$

The argument does not assume that $`V`$ commutes with $`H_0`$. It also holds for density operators, with all expectations interpreted as traces.

## Consequences for configuration size

Set

```math
e=\epsilon+2\delta.
```

For a normalized state in an orthogonal $`K`$-dimensional Gaussian configuration space, [Theorem 3 of the orthogonal analysis](orthogonal_configurations.md#the-orthogonal-configuration-theorem) and (3) imply

```math
\boxed{K\ge\exp\{m[\log2-h(\epsilon+2\delta)]\}}
\quad\text{if }\epsilon+2\delta\lt \frac12.
```

**Equation (5).**

In particular, the variational error of any such space obeys

```math
\frac{E_{\mathcal S}(H)-E_0(H)}m
\ge\frac12-2\delta-\sqrt{\frac{\log K}{2m}}.
```

**Equation (6).**

For an unrestricted Gaussian expansion, including border rank, [the general-rank theorem](gaussian_rank.md#low-energy-theorem) gives

```math
\boxed{K\ge\frac8{9(m+1)}
\exp\!\left[mD_{\rm KL}(\epsilon+2\delta\Vert q)\right]}
\quad\text{if }\epsilon+2\delta\lt q,
```

**Equation (7).**

where

```math
R=\frac{27(8+2\sqrt7)}{256},\qquad q=1-R^{-1}\approx0.286650896.
```

The imported rank input and its exact hypotheses are given in [RS26, Theorem 2](../references/README.md#rs26), [primary text](https://arxiv.org/html/2610.03699v1), and the companion proof. Equation (7) is not extended to densities at or above $`q`$.

### Equal-accuracy comparison

Choose fixed constants satisfying

```math
2\delta\le\epsilon\lt \frac12-2\delta
```

for the orthogonal theorem. Such an interval exists whenever $`0\le\delta\lt 1/8`$. Then the explicit constant-depth preparation of $`\Omega_m`$ meets error $`\epsilon m`$ by (4), while any orthogonal Gaussian configuration space meeting that same error requires exponentially many configurations by (5).

For unrestricted Gaussian rank, use

```math
2\delta\le\epsilon\lt q-2\delta,
```

which is possible whenever $`0\le\delta\lt q/4`$. This is the stronger representation scope, with its appropriately smaller allowed density.

These are fixed physical accuracies as $`m`$ grows. The interaction strength need not tend to zero with system size.

For example, take $`\delta=1/32`$ and $`\epsilon=1/8`$, so $`e=3/16`$. The easy trial is within $`m/16`$ of the ground energy and therefore meets the requested $`m/8`$ error. The respective lower bounds are

```math
K_{\rm orth}\ge2^{0.303787739874854\,m},
```

and

```math
K_{\rm general}\ge\frac8{9(m+1)}
2^{0.037728829677828\,m}.
```

**Equation (8).**

The decimal exponents simply evaluate (5) and (7); they are not fitted numerical scaling laws.

## An explicit connected, noncommuting family

Place the modes in the order $`1,\ldots,4m`$ and join adjacent blocks by

```math
V_\lambda=\lambda\sum_{j=1}^{m-1}C_j,
\qquad
C_j=a_{4j}^\dagger a_{4j+1}
+a_{4j+1}^\dagger a_{4j},
\qquad\lambda\in\mathbb R.
```

**Equation (9).**

Each $`C_j`$ is a number-conserving one-body hopping term. On its two participating modes, it swaps the one-particle occupations and annihilates the empty and fully occupied vectors. Its eigenvalues are $`1,-1,0,0`$, so

```math
\|C_j\|=1,
\qquad
\|V_\lambda\|\le|\lambda|(m-1)\le|\lambda|m.
```

**Equation (10).**

Thus $`\delta=\vert \lambda\vert `$ suffices in the uniform theorem. For every $`\lambda\ne0`$ and $`m\ge2`$, the interaction graph is connected. All supports have bounded range and each mode participates in only a constant number of terms. The Hamiltonian remains number conserving and at most two-body in the fermionic sense.

The links genuinely fail to commute with $`H_0`$. For a given link, $`C_j\Omega_m`$ is nonzero and has one and three particles on the adjacent blocks, rather than two on each. Both affected blocks then have energy two under their local $`h`$, so

```math
H_0C_j\Omega_m=4C_j\Omega_m,
\qquad H_0\Omega_m=0.
```

In fact $`\Vert C_j\Omega_m\Vert ^2=1/2`$, giving an explicit nonzero witness to $`[H_0,C_j]`$. Consequently the example is not merely a collection of independently shifted commuting block energies.

Because $`\Omega_m`$ has exactly two particles on each block,

```math
\langle C_j\rangle_{\Omega_m}=0,
\qquad
\langle H_0+V_\lambda\rangle_{\Omega_m}=0.
```

For this explicit family, the trial guarantee improves to

```math
0\le\langle H_0+V_\lambda\rangle_{\Omega_m}
-E_0(H_0+V_\lambda)
\le|\lambda|(m-1).
```

**Equation (11).**

The general $`2\delta m`$ guarantee remains useful because it covers arbitrary allowed perturbations without using this cancellation. Bounds (5)–(8) deliberately use that common uniform comparison.

More generally, any known finite-range, number-conserving, at-most-two-body perturbation $`V=\sum_Xv_X`$ satisfying

```math
\sum_X\|v_X\|\le\delta m
```

falls under the same theorem. Strict versions of this coefficient bound provide a neighborhood of perturbations, rather than only one finely tuned Hamiltonian.

## What is certified, and what is not asserted

The simple source is a certified trial at the displayed fixed energy density. The argument does not prove a uniform gap for the perturbed family, a constant-depth preparation of its exact ground state, or high global fidelity between that ground state and $`\Omega_m`$.

Nor does the lower bound apply to every classical representation. A product of correlated pairs can be kept as a product instead of materializing its exponentially many occupation configurations. A constant-depth non-Gaussian block basis change makes the same trial one configuration. The result constrains global Gaussian configuration expansions and the algorithms that explicitly use them; [algorithmic scope](algorithmic_scope.md) describes the allowed escapes.

[The finite checks](../verification/README.md) verify the hopping signs, link norm, noncommutativity witness, and the perturbation inequalities on two blocks. The uniform proofs above are independent of those finite calculations.
