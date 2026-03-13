'''
Variational Quantum Eigensolver (VQE)
'''

import numpy as np

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator
from qiskit.circuit import Parameter

from qiskit_algorithms.minimum_eigensolvers import VQE
from qiskit_algorithms.optimizers import COBYLA


# ---------------------------------
# Hamiltoniano
# ---------------------------------

hamiltonian = SparsePauliOp.from_list([
    ("ZI", 1.0),
    ("IZ", 1.0),
    ("XX", 0.5)
])


# ---------------------------------
# Parâmetros variacionais
# ---------------------------------

theta1 = Parameter("θ1")
theta2 = Parameter("θ2")
theta3 = Parameter("θ3")
theta4 = Parameter("θ4")


# ---------------------------------
# Ansatz parametrizado
# ---------------------------------

ansatz = QuantumCircuit(2)

ansatz.ry(theta1, 0)
ansatz.ry(theta2, 1)

ansatz.cx(0, 1)

ansatz.ry(theta3, 0)
ansatz.ry(theta4, 1)

print("Circuito Ansatz:")
print(ansatz.draw())


# ---------------------------------
# Estimator
# ---------------------------------

estimator = StatevectorEstimator()


# ---------------------------------
# Otimizador
# ---------------------------------

optimizer = COBYLA(maxiter=200)


# ---------------------------------
# VQE
# ---------------------------------

vqe = VQE(
    estimator=estimator,
    ansatz=ansatz,
    optimizer=optimizer
)


# ---------------------------------
# Executar
# ---------------------------------

result = vqe.compute_minimum_eigenvalue(hamiltonian)


print("\nEnergia fundamental estimada:")
print(result.eigenvalue)

print("\nParâmetros ótimos:")
print(result.optimal_point)