# An explicit number-conserving two-body model

This document defines the Hamiltonian used in the configuration lower bounds, proves its spectrum, and specifies the cost of preparing its ground state. The [orthogonal configuration theorem](orthogonal_configurations.md) and the [general Gaussian-rank theorem](gaussian_rank.md) concern representations of low-energy states of this same model. [Perturbations](perturbations.md) connect the blocks while preserving the energy-accuracy comparison.

## Conventions and locality

There are $`4m`$ fermionic modes, arranged in $`m`$ consecutive blocks of four. The creation and annihilation operators satisfy

```math
\{a_i,a_j^\dagger\}=\delta_{ij}I,\qquad
\{a_i,a_j\}=0,
\qquad n_i=a_i^\dagger a_i.
```

Within a block, the occupation basis is

```math
\lvert x_1x_2x_3x_4\rangle
=(a_1^\dagger)^{x_1}(a_2^\dagger)^{x_2}
(a_3^\dagger)^{x_3}(a_4^\dagger)^{x_4}\lvert 0\rangle.
```

The verification code uses this convention, with the first mode as the most significant bit. Operators below are even in the fermionic operators, so operators on disjoint blocks commute. All block target states have even parity, making their tensor products unambiguous in this ordered Fock-space identification.

Here **two-body fermionic** means at most two creation and two annihilation operators in a term. A pair-hopping term can involve four distinct modes. The construction is therefore a bounded-range two-body fermionic model, rather than a two-local qubit model. Under the Jordan–Wigner representation with the indicated mode order, every block term still has bounded qubit support.

Energies are reported per four-mode block. Dividing an energy density by four converts it to energy per mode.

## The four-mode Hamiltonian

On one block, set

```math
N=\sum_{i=1}^4n_i,
\qquad A=a_1^\dagger a_2^\dagger a_4a_3,
\qquad T=A+A^\dagger,
```

and define

```math
h=I-T+(N-2)^2
=5I-3\sum_i n_i+2\sum_{i\lt j}n_in_j-T.
```

**Equation (1).**

The second equality uses $`n_i^2=n_i`$. Thus the nonconstant terms are one-body densities, two-body density interactions, and number-conserving pair hopping. In particular, $`[h,N]=0`$.

Define the correlated pair

```math
\lvert M\rangle
=\frac{\lvert1100\rangle+\lvert0011\rangle}{\sqrt2},
\qquad P=\lvert M\rangle\langle M\rvert,
\qquad d=I-P.
```

**Equation (2).**

### Proposition 1: spectrum and defect comparison

The state $`M`$ is the unique zero-energy state of $`h`$. The gap is one, the operator norm is five, and

```math
h\ge d\ge0.
```

**Equation (3).**

**Proof.** The occupation convention fixes the transfer sign:

```math
A\lvert0011\rangle=\lvert1100\rangle,
\qquad
A^\dagger\lvert1100\rangle=\lvert0011\rangle.
```

Both operators annihilate every other occupation vector. On the span of these two vectors, the number penalty vanishes and the matrix of $`h`$ is

```math
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
```

Its symmetric and antisymmetric eigenvectors have energies zero and two. On every remaining vector, the energy is $`1+(N-2)^2`$. Hence the complete spectrum is:

| Eigenspace | Multiplicity | Energy |
| --- | ---: | ---: |
| Symmetric correlated pair $`M`$ | 1 | 0 |
| Other two-particle occupation vectors | 4 | 1 |
| Antisymmetric pair | 1 | 2 |
| One-particle and three-particle sectors | 8 | 2 |
| Empty and fully occupied sectors | 2 | 5 |

The operator $`d`$ is zero on $`M`$ and one on its orthogonal complement. The displayed spectrum proves (3), uniqueness, the gap, and the norm. In particular, $`h`$ and $`d`$ commute. $`\square`$

## The many-block model

For copies on disjoint consecutive blocks, define

```math
H_0=\sum_{j=1}^m h_j,
\qquad D_m=\sum_{j=1}^m(I-P_j),
\qquad
\lvert\Omega_m\rangle=\lvert M\rangle^{\otimes m}.
```

**Equation (4).**

The local spectra add. Consequently $`H_0`$ has unique ground state $`\Omega_m`$, ground energy zero, gap one, and full-Fock-space norm $`5m`$. Moreover,

```math
0\le D_m\le H_0,
\qquad [D_m,H_0]=0.
```

**Equation (5).**

The ground state has exactly $`2m`$ particles. The uniqueness and gap-one statements remain true when the Hilbert space is restricted to that total-particle-number sector: a one-block excitation to another two-particle configuration already has energy one. The full-space norm bound $`\Vert H_0\Vert \le5m`$ also remains a valid bound after restriction.

The projector operator $`D_m`$ is an analytical comparison operator. The physical Hamiltonian in the construction is the two-body operator $`H_0`$, not a proposed implementation of the four-mode projector $`P_j`$ as a two-body interaction.

## Exact equivalence to the standard fermionic magic state

The Gaussian-fidelity and Gaussian-rank results used in this repository are commonly stated for

```math
\lvert G\rangle
=\frac{\lvert0000\rangle+\lvert1111\rangle}{\sqrt2}.
```

An exact Gaussian change of variables relates this state to (2). Define Majorana operators

```math
\gamma_1=a_1+a_1^\dagger,
\qquad
\gamma_4=i(a_2^\dagger-a_2),
\qquad W=-i\gamma_1\gamma_4.
```

**Equation (6).**

Direct use of the anticommutation relations gives

```math
W\lvert0000\rangle=\lvert1100\rangle,
\qquad
W\lvert1111\rangle=\lvert0011\rangle.
```

Thus $`W\lvert G\rangle=\lvert M\rangle`$, with the plus signs as written. Since $`(\gamma_1\gamma_4)^2=-I`$,

```math
W=-i\exp\!\left(\frac\pi2\gamma_1\gamma_4\right),
```

so $`W`$ is Gaussian up to a global phase and preserves parity. It need not preserve particle number; it is a mathematical equivalence used to import theorems for the larger Gaussian class. The physical state preparation below can preserve particle number throughout.

The imported squared-fidelity identity is [RS24, Lemma 1, Eqs. (10)–(12)](../references/README.md#rs24), in the [versioned primary text](https://arxiv.org/html/2407.20934v1). The imported approximate-rank theorem is [RS26, Theorem 2, Eqs. (5)–(7)](../references/README.md#rs26), in its [versioned primary text](https://arxiv.org/html/2610.03699v1). Gaussian unitaries preserve both representation classes, so both apply to $`M`$.

## Exact preparation and charged resources

There are two explicit ways to prepare each block.

**Number-conserving fermionic preparation.** Initialize the known occupation vector $`\lvert1100\rangle`$ and use

```math
Y_{\rm pair}=i(A^\dagger-A),
\qquad
U_{\rm pair}=\exp\!\left(-i\frac\pi4Y_{\rm pair}\right)
=\exp\!\left(\frac\pi4(A^\dagger-A)\right).
```

**Equation (7).**

On the ordered pair $`\lvert1100\rangle,\lvert0011\rangle`$, the generator is the Pauli $`Y`$ matrix. Therefore

```math
U_{\rm pair}\lvert1100\rangle
=\frac{\lvert1100\rangle+\lvert0011\rangle}{\sqrt2}.
```

This charges one fixed four-mode, quartic, number-conserving gate per block. It is a non-Gaussian gate; it is not counted as a free orbital rotation.

**Qubit preparation.** From $`\lvert0000\rangle`$, apply a Hadamard on the first qubit, then CNOTs from that qubit to each of the other three, and then $`X`$ on the first two qubits. This is an exact six-gate Clifford preparation of $`M`$ in the occupation encoding. Intermediate states in this qubit implementation need not have fixed particle number. Routing within a block costs only a constant number of additional gates if only adjacent qubits can interact.

Applying either block preparation in parallel uses $`4m`$ system modes or qubits, $`O(m)`$ gates, and constant depth. The initial occupation pattern is known explicitly. There is no unknown classical data to load, QRAM assumption, variational optimization, or state-preparation oracle in this resource statement. The exact Clifford construction also avoids an accumulation of synthesis error with the number of blocks.

The Hamiltonian is specified by $`O(m)`$ constant-size local terms. Preparing the state and estimating a fixed energy density therefore require polynomial physical resources; the local-observable protocol and its copy/error accounting are given in [local certification](local_certification.md). For the unperturbed Hamiltonian, the trial energy is already exactly known from the construction.

## What a different basis changes

Let $`U_M=\bigotimes_jU_{{\rm pair},j}`$. In the basis obtained by applying $`U_M`$ to occupation configurations, one configuration represents $`\Omega_m`$ exactly. This basis change is itself number conserving and has constant depth, but uses the explicitly charged non-Gaussian pair gates.

In contrast, [the orthogonal configuration theorem](orthogonal_configurations.md) allows every Gaussian orbital change and still requires exponentially many configurations to improve the energy density by a fixed amount below the best one-determinant value. Under the perturbations in [the next document](perturbations.md), the same single transformed configuration remains a certified trial at the stated fixed accuracy.

This distinction concerns the allowed basis transformations and the size of a global configuration expansion. The product state has an efficient classical geminal or tensor-product description. The model is not a claim of hardness for every classical method or a quantum computational advantage over all classical representations.

## Finite validation

[The reproducible checks](../verification/README.md) construct the CAR matrices directly, verify the complete spectrum and (3), check both exact preparation signs and the Gaussian equivalence (6), and test the connected hopping convention. The recorded floating-point results support these algebraic conventions; the proofs above establish the statements for all $`m`$.
