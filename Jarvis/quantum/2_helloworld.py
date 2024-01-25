from qiskit import *
import matplotlib.pyplot as plt

qr=QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)

# Inorder to create quantum entanglement, hadamard gate on 1st qubit
circuit.h(qr[0])

#controlled gate
circuit.cx(qr[0],qr[1])

#measuring
circuit.measure(qr,cr)

circuit.draw()
circuit.draw(output='mpl')
#Show the figure
plt.show()



