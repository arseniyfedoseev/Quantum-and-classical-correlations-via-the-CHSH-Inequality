# Quantum and Classical Correlations via the CHSH Inequality

This project studies the difference between classical local correlations and quantum correlations using the CHSH inequality.

The goal is to compare two cases:

1. A **classical local hidden-variable model**, where measurement outcomes are predetermined by a shared hidden variable.
2. A **quantum model**, where Alice and Bob share an entangled Bell state and measure it using different detector angles.

The main result is that local classical models satisfy the CHSH bound

$$
|S|\le 2,
$$

while quantum mechanics can reach

$$
S=2\sqrt{2}\approx2.828,
$$

which violates the classical CHSH inequality.

This project was developed as an assignment for the **Complex Systems** course at UGR.

---

## 1. Physical Setup

Alice and Bob share an entangled two-qubit state. Each of them chooses one of two possible measurement settings:

$$
A_1,\ A_2
$$

for Alice, and

$$
B_1,\ B_2
$$

for Bob.

Each measurement returns a binary outcome:

$$
a_i,b_j\in\{+1,-1\}.
$$

The correlation between Alice's and Bob's outcomes is

$$
E(A_i,B_j)=\langle a_i b_j\rangle.
$$

The CHSH parameter used in this implementation is

$$
S=
E(A_1,B_1)-
E(A_1,B_2)+
E(A_2,B_1)+
E(A_2,B_2).
$$

A local classical model must satisfy

$$
|S|\le 2.
$$

Quantum mechanics can violate this bound.

---

## 2. Repository Structure

```text
.
├── main.py                 # Main entry point for the quantum simulations
├── chsh.py                 # Direct CHSH correlation calculation
├── operators.py            # Measurement bases, observables, and expectation values
├── simulation.py           # Density matrix / probability-based simulation
├── plotting.py             # Plotting S as a function of the relative angle phi
├── montecarlo.py           # Classical local hidden-variable Monte Carlo simulation
├── classical_universe.py   # Script for running the classical Monte Carlo model
└── .gitattributes
```

---

## 3. Requirements

The project uses Python with:

```text
numpy
matplotlib
```

Install the dependencies with:

```bash
pip install numpy matplotlib
```

A virtual environment is recommended:

```bash
python -m venv venv
```

On macOS / Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install numpy matplotlib
```

---

## 4. How to Run the Project

### 4.1 Run the quantum simulation

The main quantum simulation starts from:

```bash
python main.py
```

This script performs the quantum part of the project:

1. Builds the measurement operators for Alice and Bob.
2. Computes the CHSH value directly from the Bell state.
3. Constructs the density matrix.
4. Estimates the CHSH value using probabilities.
5. Plots the CHSH value as a function of the relative detector angle.

The expected output is similar to:

```text
S = 2.828 + 0.000j
S_estimated = 2.828 + 0.000j
```

The script also displays a plot of

$$
S(\phi)
$$

as a function of the relative angle $\(\phi\)$.

---

### 4.2 Run the classical Monte Carlo simulation

The classical local hidden-variable simulation starts from:

```bash
python classical_universe.py
```

This script calls the Monte Carlo simulation from `montecarlo.py`.

The default local deterministic function is

```python
def default(theta, lam):
    return 1 if np.cos(theta - lam) >= 0 else -1
```

Here, `lam` is the shared hidden variable sampled randomly from

$$
[0,2\pi].
$$

The simulation estimates the four correlations

$$
E(A_1,B_1),\quad
E(A_1,B_2),\quad
E(A_2,B_1),\quad
E(A_2,B_2),
$$

and combines them into

$$
S=
E(A_1,B_1)-
E(A_1,B_2)+
E(A_2,B_1)+
E(A_2,B_2).
$$

The script prints a value of the form:

```text
Default S = ...
```

For any local classical hidden-variable model, the CHSH value must remain bounded by

$$
|S|\le 2.
$$

---

## 5. Important Note About Angle Conventions

The project uses the CHSH convention

$$
S=
E(A_1,B_1)-
E(A_1,B_2)+
E(A_2,B_1)+
E(A_2,B_2).
$$

In the quantum simulation in `main.py`, the optimal angles are

$$
\theta_{A_1}=0,\qquad
\theta_{A_2}=\frac{\pi}{4},
$$

$$
\theta_{B_1}=\frac{\pi}{8},\qquad
\theta_{B_2}=\frac{3\pi}{8}.
$$

These angles give

$$
S=2\sqrt{2}\approx2.828.
$$

The classical Monte Carlo default currently uses

$$
\theta_{B_2}=-\frac{\pi}{8},
$$

which corresponds to a different but related angle/sign convention. This does not change the classical conclusion: any local hidden-variable model must satisfy

$$
|S|\le2.
$$

---

## 6. Mathematical Background

### 6.1 Classical local hidden-variable bound

In a local hidden-variable model, the measurement outcomes are predetermined by a hidden variable $\(\lambda\)$:

$$
A_1(\lambda),A_2(\lambda),B_1(\lambda),B_2(\lambda)\in\{+1,-1\}.
$$

For one value of $\(\lambda\)$, the CHSH expression is

$$
S(\lambda)=
A_1B_1-A_1B_2+A_2B_1+A_2B_2.
$$

This can be rewritten as

$$
S(\lambda)=
A_1(B_1-B_2)+A_2(B_1+B_2).
$$

Since

$$
B_1,B_2\in\{+1,-1\},
$$

one of the brackets is always zero and the other is equal to \($\pm$ 2\). Therefore,

$$
|S(\lambda)|\le2.
$$

Averaging over many values of $\(\lambda\)$ cannot increase the bound:

$$
|S|\le2.
$$

This is the classical CHSH inequality.

---

### 6.2 Quantum Bell state

The quantum part uses the Bell state

$$
|\Phi^+\rangle=
\frac{1}{\sqrt{2}}\left(|00\rangle+|11\rangle\right).
$$

This state contains strong correlations between Alice's and Bob's measurement outcomes.

---

### 6.3 Quantum measurement basis

Each detector angle $\(\theta\)$ defines a rotated measurement basis:

$$
|0_\theta\rangle=
\cos\theta|0\rangle+\sin\theta|1\rangle,
$$

$$
|1_\theta\rangle=
-\sin\theta|0\rangle+\cos\theta|1\rangle.
$$

The two basis states correspond to outcomes \(+1\) and \(-1\):

$$
|0_\theta\rangle\rightarrow +1,
\qquad
|1_\theta\rangle\rightarrow -1.
$$

The corresponding observable is

$$
O(\theta)=
|0_\theta\rangle\langle0_\theta|-
|1_\theta\rangle\langle1_\theta|.
$$

Alice's and Bob's observables are

$$
A_i=O(\theta_{A_i}),
\qquad
B_j=O(\theta_{B_j}).
$$

---

## 7. Direct State-Vector Computation

The direct quantum calculation uses the Bell state and the tensor product of Alice's and Bob's observables.

For each pair of settings,

$$
M_{ij}=A_i\otimes B_j.
$$

The correlation is computed as the expectation value

$$
E(A_i,B_j)=
\langle\Phi^+|
A_i\otimes B_j
|\Phi^+\rangle.
$$

The CHSH value is then

$$
S=
E(A_1,B_1)-
E(A_1,B_2)+
E(A_2,B_1)+
E(A_2,B_2).
$$

For the optimal quantum angles used in `main.py`, the correlations are

$$
E(A_1,B_1)=+\frac{\sqrt{2}}{2},
$$

$$
E(A_1,B_2)=-\frac{\sqrt{2}}{2},
$$

$$
E(A_2,B_1)=+\frac{\sqrt{2}}{2},
$$

$$
E(A_2,B_2)=+\frac{\sqrt{2}}{2}.
$$

Therefore,

$$
S=
\frac{\sqrt{2}}{2}-
\left(-\frac{\sqrt{2}}{2}\right)+
\frac{\sqrt{2}}{2}+
\frac{\sqrt{2}}{2}=
2\sqrt{2}
\approx2.828.
$$

Since

$$
2\sqrt{2}>2,
$$

the CHSH inequality is violated.

---

## 8. Density Matrix / Probability-Based Simulation

The project also implements a probability-based simulation using the density matrix.

The Bell state is converted into the density matrix

$$
\rho=
|\Phi^+\rangle\langle\Phi^+|.
$$

For each measurement angle, the projectors for the two possible outcomes are

$$
P_+(\theta)=|0_\theta\rangle\langle0_\theta|,
$$

$$
P_-(\theta)=|1_\theta\rangle\langle1_\theta|.
$$

The joint probability of Alice obtaining outcome \(a\) and Bob obtaining outcome \(b\) is

$$
P(a,b|\theta_A,\theta_B)=
\mathrm{Tr}
\left[
\rho
\left(
P_a(\theta_A)\otimes P_b(\theta_B)
\right)
\right].
$$

For each pair of settings, the simulation computes the four probabilities

$$
P_{++},\quad P_{+-},\quad P_{-+},\quad P_{--}.
$$

The correlation is reconstructed as

$$
E(A_i,B_j)=
P_{++}-P_{+-}-P_{-+}+P_{--}.
$$

The CHSH value is then

$$
S_{\mathrm{probability}}=
E_{11}-E_{12}+E_{21}+E_{22}.
$$

The probability-based simulation reproduces the direct state-vector result:

$$
S_{\mathrm{probability}}=
S_{\mathrm{direct}}=
2\sqrt{2}.
$$

---

## 9. Plotting \(S\) as a Function of the Relative Angle

The function `plot_relative` plots the CHSH value as a function of the relative detector angle $\(\phi\$.

The angle parametrization is

$$
\theta_{A_1}=0,
\qquad
\theta_{A_2}=2\phi,
$$

$$
\theta_{B_1}=\phi,
\qquad
\theta_{B_2}=3\phi.
$$

For this convention, the CHSH value is

$$
S(\phi)=3\cos(2\phi)-\cos(6\phi).
$$

At

$$
\phi=\frac{\pi}{8},
$$

the value is

$$
S\left(\frac{\pi}{8}\right)=
2\sqrt{2}
\approx2.828.
$$

The plot shows:

- the classical bound $\(S=\pm2\)$;
- the quantum bound $\(S=\pm2\sqrt{2}\)$;
- the optimal point $\(\phi=\pi/8\)$.

---

## 10. Classical Monte Carlo Simulation

The classical Monte Carlo part tests local deterministic functions of the form

$$
a(\theta,\lambda),\quad b(\theta,\lambda)\in\{+1,-1\}.
$$

The default function is

```python
def default(theta, lam):
    return 1 if np.cos(theta - lam) >= 0 else -1
```

For each trial:

1. A hidden variable $\(\lambda\)$ is sampled uniformly from $\([0,2\pi]\)$.
2. Alice's outcomes are computed from $\(a(\theta_A,\lambda)\)$.
3. Bob's outcomes are computed from $\(b(\theta_B,\lambda)\)$.
4. The products $\(A_iB_j\)$ are accumulated.
5. The averages are used to estimate the four correlations.
6. The CHSH value is calculated.

The default number of Monte Carlo trials is

$$
N=10^5.
$$

The estimated classical CHSH value is

$$
S_{\mathrm{MC}}=
E(A_1,B_1)-
E(A_1,B_2)+
E(A_2,B_1)+
E(A_2,B_2).
$$

For any local classical model, the result should satisfy

$$
|S_{\mathrm{MC}}|\le2.
$$

---

## 11. Code Reading Guide

If you are reading the code for the first time, use this order.

### 1. `main.py`

Start here. This is the main entry point for the quantum part of the project.

It:

- defines the optimal quantum angles;
- creates the Bell state;
- computes the direct CHSH value;
- builds the density matrix;
- estimates \(S\) using probabilities;
- plots $\(S(\phi)\)$.

Run it with:

```bash
python main.py
```

---

### 2. `operators.py`

This file defines the basic quantum measurement tools:

- computational basis;
- Alice's rotated basis;
- Bob's rotated basis;
- observable construction;
- expectation value computation;
- creation of the full operator set $\(A_1,A_2,B_1,B_2\)$.

This is the best file to read if you want to understand how detector angles become measurement operators.

---

### 3. `chsh.py`

This file computes the direct CHSH value.

It takes:

- the quantum state;
- the four measurement operators;

and returns

$$
S=
E(A_1,B_1)-
E(A_1,B_2)+
E(A_2,B_1)+
E(A_2,B_2).
$$

---

### 4. `simulation.py`

This file implements the probability-based density matrix simulation.

It contains the logic for:

- measurement projectors;
- joint probabilities;
- reconstruction of correlations from probabilities;
- estimation of the CHSH value for a given relative angle $\(\phi\)$.

---

### 5. `plotting.py`

This file plots

$$
S(\phi)
$$

for a range of relative angles.

It also shows the classical and quantum bounds and marks the optimal point

$$
\phi=\frac{\pi}{8}.
$$

---

### 6. `montecarlo.py`

This file implements the classical local hidden-variable Monte Carlo simulation.

It defines:

- the default local deterministic function;
- the Monte Carlo loop;
- the averaging of correlations;
- the classical CHSH value.

---

### 7. `classical_universe.py`

This is the entry point for the classical Monte Carlo simulation.

Run it with:

```bash
python classical_universe.py
```

It calls `montecarlo()` and prints the default classical CHSH value.

---

## 12. Main Results

The project demonstrates the following:

1. Local classical hidden-variable models obey

$$
|S|\le2.
$$

2. The Bell state with optimal quantum measurements gives

$$
S=2 \sqrt{2} \approx 2.828.
$$

3. The direct state-vector calculation and the probability-based density matrix simulation agree.

4. The CHSH violation shows that quantum correlations cannot be explained by any local classical hidden-variable model.

---

## 13. Authors

- Alexander Chernykh Rohulska
- Arseniy Fedoseev
