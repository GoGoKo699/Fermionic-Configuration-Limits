# Algorithmic scope and resource accounting

The result constrains algorithms whose successful output is a small **global linear expansion of fermionic Gaussian states**. It applies to selected determinant spaces and to nonorthogonal sums with separately optimized orbitals. The explicit local family also has an easily prepared trial state and compact classical representations. The conclusion is therefore a representation obstruction at a specified energy accuracy, rather than a lower bound for unrestricted quantum or classical computation.

The [model](model.md), [orthogonal theorem](orthogonal_configurations.md), [general Gaussian-rank theorem](gaussian_rank.md#low-energy-theorem), and [perturbation proof](perturbations.md) contain the mathematical statements. [Related work](../references/related_work.md) identifies the imported results and the existing size-extensivity limitation of configuration interaction.

## Input and accuracy contract

There are $4m$ fermionic modes in a one-dimensional order. The Hamiltonian is supplied as an explicit list of $O(m)$ bounded-range, constant-size terms with specified coefficients. There is no arbitrary amplitude-loading task, coherent data oracle, or QRAM assumption. For the displayed family, the term pattern and fixed coefficients are known analytically.

Each four-mode block has

$$
h_j=I-(A_j+A_j^\dagger)+(N_j-2)^2,
\qquad
A_j=a_{4j-3}^\dagger a_{4j-2}^\dagger a_{4j}a_{4j-1}.
$$

It is number conserving and at most two-body in the fermionic sense: its monomials contain at most two creation and two annihilation operators. This does not mean two-qubit support. Its unique ground state is

$$
|M\rangle_j=(|1100\rangle_j+|0011\rangle_j)/\sqrt2,
$$

and $H_0=\sum_jh_j$ has ground state $\Omega_m=M^{\otimes m}$. The physical comparison uses the energy tolerance

$$
\langle\psi|H|\psi\rangle-E_0(H)\le\epsilon m,
$$

with fixed $\epsilon>0$. Energies are per four-mode block; the tolerance per mode is $\epsilon/4$. This is an additive density target, not a relative-error definition that depends on the choice of energy origin. The full Fock space or the fixed-$2m$-particle sector can be used, provided the same space defines the ground energy and the variational task.

An explicit connected family is

$$
H_\lambda=H_0+\lambda\sum_{j=1}^{m-1}
\left(a_{4j}^\dagger a_{4j+1}+a_{4j+1}^\dagger a_{4j}\right).
$$

For $\lambda\ne0$ and $m\ge2$, its interaction graph is connected and the added links do not commute with $H_0$. Each link has norm one. Thus $\|H_\lambda-H_0\|\le|\lambda|(m-1)$, and the coupling need not decrease with system size. More generally, the transfer proof applies to $H=H_0+V$ with $\|V\|\le\delta m$; a sum of local terms satisfying $\sum_X\|v_X\|\le\delta m$ is sufficient.

Every state meeting the stated accuracy has defect density at most $e=\epsilon+2\delta$. The explicit trial $\Omega_m$ has error at most $2\delta m$. Consequently, choosing

$$
2\delta\le\epsilon<q-2\delta,
\qquad
q=1-\frac{256}{27(8+2\sqrt7)}\approx0.28665,
$$

gives the same energy target for the easy trial and the unrestricted-rank lower bound. The orthogonal result permits the larger upper endpoint $1/2-2\delta$. For example, the fixed values $\delta=1/32$ and $\epsilon=1/8$ meet both conditions. For the displayed hopping perturbation, the product trial has zero hopping expectation and an even sharper error guarantee, but the common $2\delta$ comparison suffices.

This reasoning does not assert a uniform gap of $H_\lambda$, efficient exact preparation of its ground state, or high global fidelity between its ground state and the trial. None is needed for the fixed-density comparison.

## Which output representations are constrained?

| Output contract | Allowed optimization | Applicable conclusion |
| --- | --- | --- |
| A span of $K$ configurations from one globally rotated occupation basis | Any global orbital rotation and any choice of configurations | Orthogonal bound for $e<1/2$. |
| A span admitting $K$ orthonormal pure Gaussian basis vectors | Even different Gaussian transformations, subject to mutual orthogonality | The same orthogonal bound. |
| A sum of $K$ Slater determinants with independent orbital choices | Nonorthogonality, arbitrary complex coefficients, and arbitrary conditioning | Unrestricted Gaussian-rank bound for $e<q$. |
| A sum of $K$ pure fermionic Gaussian states | Both parities and general Bogoliubov transformations; border-rank limits included | The same unrestricted bound, covering a class larger than fixed-particle determinants. |
| A product, tensor network, exponential cluster expression, or span of non-Gaussian block states | A different representation contract | No configuration-count lower bound is asserted. |

The quantitative bounds are

$$
K_{\rm orth}\ge\exp\{m[\log2-h(e)]\},\qquad e<1/2,
$$

and

$$
K_{\rm general}\ge\frac8{9(m+1)}
\exp\{mD_{\rm KL}(e\Vert q)\},\qquad e<q.
$$

Here $e=\epsilon+2\delta$ for the perturbed problem. The stronger inherited asymptotic input is recorded separately in [the Gaussian-rank analysis](gaussian_rank.md#stronger-inherited-asymptotic-bound). It does not change these distinctions between representation classes.

The general theorem counts Gaussian terms, not arbitrary subspace dimension. An arbitrary one-dimensional space can be spanned by $\Omega_m$ itself, which is not Gaussian. Also, orthogonalizing a nonorthogonal list usually produces non-Gaussian vectors, so it cannot justify applying the orthogonal exponent to that list.

In the unperturbed orthogonal problem, a single optimized determinant attains energy $m/2$, and every subexponential orthogonal Gaussian expansion has optimal energy density tending to $1/2$. Thus the obstruction can be expressed as failure to recover a fixed positive fraction of the extensive correlation energy beyond the best determinant. This sharp orthogonal floor is proved in [the corresponding section](orthogonal_configurations.md#the-best-determinant-and-the-sharp-asymptotic-floor); no equally sharp frontier is claimed for unrestricted rank.

## Consequences for selected-configuration workflows

[QSCI](../references/related_work.md#QSCI23) and [SQD](../references/related_work.md#SQD25) select configurations and solve a projected variational problem. If their final normalized state attains the target energy on this family, the final configuration span must satisfy the relevant bound. This conclusion grants ideal samples, exact projected matrix elements, exact diagonalization, and optimal orbitals. The loss is already present in the output class.

The statement also applies to a nonorthogonal determinant expansion such as the ansatz in [EIDOS](../references/related_work.md#EIDOS25), using the unrestricted bound. Each term can have its own orbitals. No lower bound on the Gram-matrix condition number, coefficient magnitude, or optimization quality is assumed; the border-rank formulation also includes limiting cancellations.

The quantity $K$ counts the final global terms, including terms added by recovery, deterministic augmentation, or Cartesian-product completion. It is not automatically the number of raw samples. In particular, the size-consistency procedure in [Sugisaki26](../references/related_work.md#Sugisaki26) illustrates why configurations can be added without observing each one independently. A special implementation that accepts only directly observed configurations needs at least as many shots as its number of distinct accepted strings, but that implementation-specific observation is not a universal quantum-query lower bound.

Similarly, a formal $K\times K$ projected matrix does not imply that every solver must store all $K^2$ entries or take cubic time: iterative and implicit methods may avoid those operations. What follows directly is an exponential number of terms in an explicit successful global Gaussian expansion. Keeping that expansion implicitly in a compact product or another structured representation changes the output contract.

These qualifications matter because the qualitative failure of truncated CI to achieve extensive accuracy at polynomial configuration cost is established background; see [Chan24](../references/related_work.md#Chan24). The result here supplies uniform quantitative bounds over the specified orbital and Gaussian classes on a local family. It is not a claim that every molecular or Hubbard instance has this behavior, or that the numerical results in existing SQD and nonorthogonal-CI studies are incorrect.

## Easy preparation and classical alternatives

The trial has an explicit linear-size preparation. On each block initialize $|1100\rangle$ and apply

$$
U_j=\exp\!\left[\frac\pi4(A_j^\dagger-A_j)\right].
$$

This is a fixed four-mode number-conserving **non-Gaussian** gate, counted once per block. With independent block operations, the construction uses $4m$ system modes, $O(m)$ gates, and constant parallel depth. It assumes the stated local gate primitive rather than treating a quartic gate as a free orbital rotation. The equivalent occupation-qubit construction uses one Hadamard, three CNOTs, and two $X$ gates per block; it is exact and Clifford, although its intermediate states need not preserve particle number. The [model document](model.md#exact-preparation-and-charged-resources) checks the signs and gate count.

The same state has several compact classical forms. In the prescribed mode order it is a product of geminals,

$$
|\Omega_m\rangle=2^{-m/2}
\prod_{j=1}^{m}
\left(a_{4j-3}^\dagger a_{4j-2}^\dagger+
a_{4j-1}^\dagger a_{4j}^\dagger\right)|\mathrm{vac}\rangle.
$$

Keeping these $m$ factors avoids expanding their $2^m$ occupation terms. It is also a product of four-mode tensors, or an occupation-qubit matrix-product state with bond dimension at most two within a block and one between blocks.

There is an exact compact doubles-cluster parametrization as well. Let $|\Phi_0\rangle=|1100\rangle^{\otimes m}$, $S_j=A_j^\dagger$, and $T=\sum_jS_j$. Each $S_j^2=0$ and disjoint even operators $S_j$ commute. Hence

$$
2^{-m/2}e^T|\Phi_0\rangle
=2^{-m/2}\prod_j(I+S_j)|\Phi_0\rangle
=|\Omega_m\rangle.
$$

This identity establishes a compact description for this trial; it is not a claim about general coupled-cluster convergence or exactness for the perturbed ground state. Local expectation values and samples of the explicit product trial can be generated classically. The trial energy for $H_\lambda$ is already known analytically. A non-Gaussian block basis transformation also makes this trial a single basis vector, as described in [the model](model.md#what-a-different-basis-changes).

These are substantive escapes from the constrained representation. The exponential count does not imply hard classical simulation of the displayed preparation, a quantum advantage for estimating its energy, or difficulty in finding some state meeting the stated energy tolerance.

## Physical data and local certification

If a physical source supplies independent copies of an unknown state $\rho$, the [local protocol](local_certification.md) samples a uniformly random block and measures $h_j$. The outcome lies in $\{0,1,2,5\}$. For additive energy-density margin $\eta$ and one-sided failure probability $\alpha$, it suffices to use

$$
T_{\rm copies}\ge
\left\lceil\frac{25}{2\eta^2}\log\frac1\alpha\right\rceil.
$$

This number is independent of $m$ at fixed $\eta,\alpha$, because one measures an average local energy. It does not make the supplied many-body copies free. The measurement uses a fixed four-mode basis change followed by occupations; this operation is charged and is not presumed Gaussian. The protocol assumes independent copies of the same state and trusted measurement, rather than deriving those properties from the data.

| Resource | What is charged or proved |
| --- | --- |
| Hamiltonian input | An explicit list of $O(m)$ constant-support terms; coefficient precision is part of the input. |
| System size | $4m$ modes or occupation qubits per supplied copy. |
| Known trial preparation | $O(m)$ gates per copy and constant block-parallel depth in the stated local model. |
| Unknown-source access | $T_{\rm copies}$ independent preparations; the source's preparation cost is an additional input cost. |
| Sampled-block measurement | Constant local operations per copy if the chosen block is directly accessible; any routing or addressing cost is additional. |
| Classical sampling and accumulation | $O(\log m)$ random bits per block index in expectation, and counters of size $O(\log T_{\rm copies}+\log m)$. |
| Explicit successful Gaussian expansion | At least the proved number $K$ of terms. An explicit list has $\Omega(K)$ records; orbital and coefficient descriptions add their own size and precision costs. |
| Coherent access | No inverse preparation, controlled preparation, amplitude oracle, or QRAM is required by the local protocol or assumed free. |

For the known product source, preparing every copy costs $O(T_{\rm copies}m)$ gates; local readout costs $O(T_{\rm copies})$ under direct block access. This separates sample complexity from total physical work. The certificate concerns rank or exclusion of the closed convex hull of bounded-rank pure states, precisely as defined in [the mixed-state statement](local_certification.md#mixed-state-guarantee). It is not an assertion that every pure state in every decomposition has large rank, nor a bound on the ordinary matrix rank of $\rho$.

Measuring $H_0$ certifies the representation property directly. It does not by itself estimate $E_0(H_\lambda)$ or certify closeness to the perturbed ground state. The latter energy-accuracy comparison uses the deterministic perturbation inequalities, not an unmeasured ground-energy assumption. The pure-state covariance counterexample in [local certification](local_certification.md#covariance-does-not-certify-this-resource) also explains why complete quadratic data alone cannot replace this model-specific energy witness.

The resulting distinction is operational: a state can be easy to prepare, easy to describe with correlated blocks, and easy to certify locally, while every accurate explicit global Gaussian expansion needs exponentially many terms. The representation class, accuracy criterion, and access costs are all part of that statement.
