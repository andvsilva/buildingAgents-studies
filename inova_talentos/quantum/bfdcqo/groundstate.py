'''
Bias-Field Digitized Counterdiabatic Quantum Optimization (BF-DCQO)

BF-DCQO is a quantum optimization method related to digitized adiabatic 
quantum computing, where counterdiabatic terms and bias fields are 
introduced to suppress non-adiabatic transitions and guide the system 
toward the ground state of a problem Hamiltonian.
'''

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, Statevector

# -----------------------------------------
# Problem Hamiltonian (MaxCut-like example)
# H_problem = Z1 Z2
# -----------------------------------------

H_problem = SparsePauliOp.from_list([
    ("ZZ", 1.0)
])

# -----------------------------------------
# Mixer Hamiltonian
# H_mixer = X1 + X2
# -----------------------------------------

H_mixer = SparsePauliOp.from_list([
    ("XI", 1.0),
    ("IX", 1.0)
])

# -----------------------------------------
# Counterdiabatic term
# H_cd = Y1 Z2 + Z1 Y2
# -----------------------------------------

H_cd = SparsePauliOp.from_list([
    ("YZ", 0.5),
    ("ZY", 0.5)
])

# -----------------------------------------
# Bias field
# -----------------------------------------

bias_strength = 0.3

# -----------------------------------------
# Digitized evolution parameters
# -----------------------------------------

steps = 10
gamma = 0.5
beta = 0.7

# -----------------------------------------
# Build BF-DCQO circuit
# -----------------------------------------

qc = QuantumCircuit(2)

# initial superposition
qc.h([0,1])

for step in range(steps):

    # Problem Hamiltonian evolution
    qc.rzz(2 * gamma / steps, 0, 1)

    # Mixer evolution
    qc.rx(2 * beta / steps, 0)
    qc.rx(2 * beta / steps, 1)

    # Counterdiabatic correction
    qc.ry(0.1 / steps, 0)
    qc.ry(0.1 / steps, 1)

    # Bias field
    qc.rz(bias_strength / steps, 0)
    qc.rz(bias_strength / steps, 1)

qc.measure_all()

print("BF-DCQO Circuit:")
print(qc)

# -----------------------------------------
# Simulate statevector
# -----------------------------------------

state = Statevector.from_instruction(qc.remove_final_measurements(inplace=False))

print("\nFinal quantum state:")
print(state)