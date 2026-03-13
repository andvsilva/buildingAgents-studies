# Variational Quantum Eigensolver (VQE) – Example in Python

## Overview

This repository contains a simple implementation of the **Variational Quantum Eigensolver (VQE)** using **Python** and the **Qiskit** framework.

The goal of this example is to demonstrate how a **variational quantum algorithm** can estimate the **ground state energy of a Hamiltonian** using a hybrid **quantum-classical optimization loop**.

VQE is one of the most important algorithms in **near-term quantum computing** because it is designed to run on **NISQ (Noisy Intermediate-Scale Quantum) devices**, which have:

* limited number of qubits
* noisy quantum operations
* restricted circuit depth

Instead of performing a full quantum computation, VQE splits the work between:

* a **quantum computer** (state preparation and measurement)
* a **classical optimizer** (parameter optimization)

---

# The Problem

The objective of VQE is to find the **minimum eigenvalue** of a Hamiltonian:

$$
H |\psi\rangle = E |\psi\rangle
$$

The smallest eigenvalue (E_0) corresponds to the **ground state energy** of the system.

Using the **variational principle of quantum mechanics**, we know that:

$$
E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle \ge E_0
$$

Therefore, by minimizing the expectation value of the Hamiltonian, we can approximate the ground state energy.

---

# Hamiltonian Used in This Example

In this example we use a simple **two-qubit Hamiltonian**:

$$
H = Z_1 + Z_2 + 0.5 X_1 X_2
$$

where

* (X) and (Z) are **Pauli operators**
* the system has **two qubits**

This Hamiltonian is defined in the code using:

```python
hamiltonian = SparsePauliOp.from_list([
    ("ZI", 1.0),
    ("IZ", 1.0),
    ("XX", 0.5)
])
```

This representation expresses the Hamiltonian as a **sum of Pauli strings**, which is the standard form used in quantum computing frameworks.

---

# Structure of the Algorithm

The VQE algorithm works through an iterative hybrid loop.

1. **Prepare a parameterized quantum state**
2. **Measure the expectation value of the Hamiltonian**
3. **Use a classical optimizer to update parameters**
4. **Repeat until convergence**

---

# Code Explanation

## 1. Importing Libraries

The implementation relies mainly on the **Qiskit ecosystem**.

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator
from qiskit.circuit import Parameter

from qiskit_algorithms.minimum_eigensolvers import VQE
from qiskit_algorithms.optimizers import COBYLA
```

Key components:

* `QuantumCircuit` → build the quantum circuit
* `SparsePauliOp` → define the Hamiltonian
* `StatevectorEstimator` → compute expectation values
* `VQE` → the variational algorithm implementation
* `COBYLA` → classical optimization algorithm

---

# 2. Defining the Hamiltonian

The Hamiltonian represents the physical system being simulated.

```python
hamiltonian = SparsePauliOp.from_list([
    ("ZI", 1.0),
    ("IZ", 1.0),
    ("XX", 0.5)
])
```

Each tuple corresponds to:

```
(Pauli string, coefficient)
```

Examples:

* `"ZI"` → Z acting on qubit 0
* `"IZ"` → Z acting on qubit 1
* `"XX"` → interaction between the two qubits

---

# 3. Creating Variational Parameters

VQE requires a **parameterized quantum circuit**.

We define symbolic parameters:

```python
theta1 = Parameter("θ1")
theta2 = Parameter("θ2")
theta3 = Parameter("θ3")
theta4 = Parameter("θ4")
```

These parameters will be optimized during the algorithm.

---

# 4. Building the Ansatz Circuit

The **ansatz** is a parameterized circuit that prepares the quantum state.

```python
ansatz = QuantumCircuit(2)

ansatz.ry(theta1, 0)
ansatz.ry(theta2, 1)

ansatz.cx(0, 1)

ansatz.ry(theta3, 0)
ansatz.ry(theta4, 1)
```

Circuit structure:

```
q0 ──RY(θ1)──■──RY(θ3)──
             │
q1 ──RY(θ2)──X──RY(θ4)──
```

Explanation:

* `RY` gates create **superposition states**
* `CX` (CNOT) creates **entanglement between qubits**

This combination allows the circuit to represent a wide range of quantum states.

---

# 5. Expectation Value Estimation

The expectation value of the Hamiltonian is computed using:

```python
estimator = StatevectorEstimator()
```

This primitive simulates the quantum circuit and computes:

$$
\langle \psi(\theta) | H | \psi(\theta) \rangle
$$

---

# 6. Classical Optimization

The parameters are optimized using the **COBYLA algorithm**.

```python
optimizer = COBYLA(maxiter=200)
```

COBYLA is commonly used in VQE because:

* it does not require gradients
* it performs well for noisy functions

---

# 7. Running the VQE Algorithm

The algorithm is constructed as:

```python
vqe = VQE(
    estimator=estimator,
    ansatz=ansatz,
    optimizer=optimizer
)
```

Then executed with:

```python
result = vqe.compute_minimum_eigenvalue(hamiltonian)
```

The algorithm repeatedly:

1. selects parameters
2. runs the quantum circuit
3. measures the energy
4. updates parameters

until convergence.

---

# Output

Typical output looks like:

```
Energia fundamental estimada:
(-1.52+0j)

Parâmetros ótimos:
[1.23, -0.44, 2.01, -0.91]
```

This means:

* the algorithm approximated the **ground state energy**
* the optimizer found a set of parameters that minimizes the energy

---

# Why VQE is Important

VQE is widely used in quantum research because it enables:

* **quantum chemistry simulations**
* **materials science**
* **optimization problems**
* **variational quantum machine learning**

It is one of the most practical algorithms for **near-term quantum hardware**.

---

# Possible Extensions

This example can be extended in several ways:

* simulate **molecules such as H₂ or LiH**
* design more expressive **ansatz circuits**
* experiment with different **optimizers**
* visualize the **energy landscape**

---

# References

* Qiskit Documentation
* Variational Quantum Eigensolver original paper (Peruzzo et al., 2014)

---

# Summary

This project demonstrates how a **hybrid quantum-classical algorithm** can estimate the **ground state energy of a quantum system** using a parameterized circuit and classical optimization.

Even though the example uses a simple Hamiltonian, the same structure is used in **real quantum simulations and research applications**.
