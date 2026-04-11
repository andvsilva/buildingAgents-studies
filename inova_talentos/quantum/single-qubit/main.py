import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit import QuantumCircuit # to build the quantum circuit
from qiskit_aer import AerSimulator # simulator backend (no real quantum hardware)
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# salvar imagem
import os
os.makedirs("images", exist_ok=True)

# Parameter
theta = -np.pi / 4  # you can change this value

# Create circuit
qc = QuantumCircuit(1, 1)

# Apply Ry rotation
qc.ry(theta, 0)

# Measurement
qc.measure(0, 0)

# Simulator
simulator = AerSimulator()
result = simulator.run(qc, shots=10000).result()
counts = result.get_counts()

# Print results
print("Measurement counts:", counts)

# Plot histogram
plot_histogram(counts)

# save the plot
plt.savefig("images/qiskit-measurements.png")
#plt.show()

# estado sem medição (IMPORTANTE!)
qc_state = QuantumCircuit(1)
qc_state.ry(theta, 0)

# obter vetor de estado
state = Statevector.from_instruction(qc_state)

# plot Bloch sphere
plot_bloch_multivector(state)

plt.savefig("images/bloch-sphere.png")

# mostrar (opcional)
# plt.show()


# Theoretical probabilities
p1 = np.sin(theta/2)**2
p0 = np.cos(theta/2)**2

print(f"Theoretical P(1): {p1:.4f}")
print(f"Theoretical P(0): {p0:.4f}")