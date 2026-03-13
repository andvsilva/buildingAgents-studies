'''
Quantum Approximate Optimization Algorithm (QAOA)
'''

import numpy as np

from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorSampler

from qiskit_algorithms.minimum_eigensolvers import QAOA
from qiskit_algorithms.optimizers import COBYLA

import warnings
warnings.filterwarnings("ignore")

# --------------------------------------
# 1. Hamiltonian for MaxCut (2 nodes)
# --------------------------------------

cost_hamiltonian = SparsePauliOp.from_list([
    ("ZZ", 1.0)
])


# --------------------------------------
# 2. Classical optimizer
# --------------------------------------

optimizer = COBYLA(maxiter=200)


# --------------------------------------
# 3. Sampler primitive
# --------------------------------------

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