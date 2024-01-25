from qiskit import *
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor

qr=QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)

# Inorder to create quantum entanglement, hadamard gate on 1st qubit
circuit.h(qr[0])

#controlled gate
circuit.cx(qr[0],qr[1])

#measuring
circuit.measure(qr,cr)

#running in quantum computer
IBMQ.load_account()
provider = IBMQ.get_provider(hub = 'ibm-q')
qcomp = provider.get_backend('ibmq')
job = execute(circuit, backend=qcomp)
job_monitor(job)
result = job.result()

plot_histogram(result.get_counts(circuit))
plt.show()
