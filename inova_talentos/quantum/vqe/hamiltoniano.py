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
# Hamiltoniano:
# - Modelos de spins.
# ---------------------------------

# Fisicamente isso representa um modelo simples de interação 
# entre dois qubits.
hamiltonian = SparsePauliOp.from_list([
    ("ZI", 1.0), # energia do qubit 1
    ("IZ", 1.0), # energia do qubit 2
    ("XX", 0.5)  # interação entre os qubits
])


# ---------------------------------
# Parâmetros variacionais
# - Esses parâmetros controlam as rotações quânticas.
# - Otimizados pelo algoritmo clássico.
# ---------------------------------

theta1 = Parameter("θ1")
theta2 = Parameter("θ2")
theta3 = Parameter("θ3")
theta4 = Parameter("θ4")


# ---------------------------------
# Ansatz parametrizado
# ---------------------------------

ansatz = QuantumCircuit(2)

# Camada 1 — rotações
ansatz.ry(theta1, 0)
ansatz.ry(theta2, 1)

# emaranhamento entre os qubits.
ansatz.cx(0, 1)

ansatz.ry(theta3, 0)
ansatz.ry(theta4, 1)

print("Circuito Ansatz:")
print(ansatz.draw())


# ---------------------------------
# Estimator
# ---------------------------------

# simulação exata do vetor de estado.
estimator = StatevectorEstimator()


# ---------------------------------
# Otimizador
# ---------------------------------
# O COBYLA é um método de otimização sem derivadas.
# E(θ) ajustando os parâmetros.
optimizer = COBYLA(maxiter=200)

# ---------------------------------
# VQE
# ---------------------------------

vqe = VQE(
    estimator=estimator, # calcula energia
    ansatz=ansatz,  # estado quântico
    optimizer=optimizer # minimiza energia
)


# ---------------------------------
# Executar
# ---------------------------------
# O algoritmo executa o loop variacional:
result = vqe.compute_minimum_eigenvalue(hamiltonian)

# Retorna a energia fundamental aproximada.
print("\nEnergia fundamental estimada:")
print(result.eigenvalue)

# Retorna os parâmetros ótimos:
# que produzem o estado de menor energia.
print("\nParâmetros ótimos:")
print(result.optimal_point)