from qiskit import *
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

qr=QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)

# Inorder to create quantum entanglement, hadamard gate on 1st qubit
circuit.h(qr[0])

#controlled gate
circuit.cx(qr[0],qr[1])

#measuring
circuit.measure(qr,cr)

#Running on a simulator

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()

plot_histogram(result.get_counts(circuit))
plt.show()
