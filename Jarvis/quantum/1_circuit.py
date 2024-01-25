from qiskit import *
import matplotlib.pyplot as plt

qr=QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)

circuit.draw()
circuit.draw(output='mpl')

# Show the figure
plt.show()

#IBMQ.save_account('7c33cd3bf7401730f46210c0f7b98eb6c08007747f4b76dc24ba19c4853d6372eb4e3c7cd6de391c9c84875ea4f606edd39f7e7f88da6c735e11eda6471a8ceb')