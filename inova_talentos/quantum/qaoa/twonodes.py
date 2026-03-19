'''
Quantum Approximate Optimization Algorithm (QAOA)

--> Define o Hamiltoniano do problema (MaxCut)
--> Escolhe um otimizador clássico
--> Define o sampler quântico
--> Cria o algoritmo QAOA
--> Executa a otimização
--> Retorna a energia mínima e os parâmetros ótimos
'''

import numpy as np

from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorSampler

from qiskit_algorithms.minimum_eigensolvers import QAOA
from qiskit_algorithms.optimizers import COBYLA

import warnings
warnings.filterwarnings("ignore")

# --------------------------------------
# 1. Hamiltoniano for MaxCut (2 nodes)
# --------------------------------------

# Hamiltoniano de custo.
cost_hamiltonian = SparsePauliOp.from_list([
    ("ZZ", 1.0)
])


# --------------------------------------
# 2. Classical optimizer
# --------------------------------------

# O algoritmo clássico utilizado é COBYLA.
optimizer = COBYLA(maxiter=200) 


# --------------------------------------
# 3. Sampler primitive
# --------------------------------------
# O Sampler executa o circuito e retorna probabilidades de medição.
sampler = StatevectorSampler()


# --------------------------------------
# 4. QAOA algorithm
# --------------------------------------

qaoa = QAOA(
    sampler=sampler,
    optimizer=optimizer,
    reps=1
)


# --------------------------------------
# 5. Run QAOA
# --------------------------------------

result = qaoa.compute_minimum_eigenvalue(cost_hamiltonian)


# --------------------------------------
# 6. Output
# --------------------------------------

print("\nMinimum energy found:")
print(result.eigenvalue)

print("\nOptimal parameters:")
print(result.optimal_point)