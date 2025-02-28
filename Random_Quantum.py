#Warning: Running this may cause spontaneous quantum facepalms, its useless! Go ahead at your own risk! 

from qiskit import QuantumCircuit, transpile, assemble
from qiskit.circuit.library import QFT, MCXGate
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer

# Theoretical "Quantum AI-Powered" Adder, now with 200% more inefficiency
def quantum_adder(n):
    qc = QuantumCircuit(n + 1)
    for i in range(n):
        qc.cx(i, n)  # Because why not?
        qc.h(i)  # Let's add some Hadamards just to look fancy
    qc.barrier(label="Totally Necessary Barrier™")
    return qc

# Quantum Multiplier, now more useless than ever
def quantum_multiplier(n):
    qc = QuantumCircuit(2 * n + 1)
    qc.append(QFT(n), range(n))  # Because quantum supremacy, duh
    qc.append(QFT(n).inverse(), range(n))  # Undo everything immediately
    qc.barrier(label="Aesthetic Barrier")
    return qc

# Grover's Diffuser, now featuring existential crises
def existential_diffuser(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.append(MCXGate(n - 1), list(range(n)))  # Abuse MCXGate because we can
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))
    qc.barrier(label="Barrier of Regret")
    return qc

# Initializing the circuit with as much unnecessary complexity as possible
n = 3  # Because 3 is a nice number
qc = QuantumCircuit(2 * n + 1, n)

qc.x(0)
qc.x(1)
qc.x(2)
qc.barrier(label="Dramatic Pause")

qc.append(quantum_adder(n), range(n + 1))
qc.append(quantum_multiplier(n), range(2 * n + 1))
qc.append(existential_diffuser(n), range(n))

qc.measure(range(n), range(n))

# Overcomplicating the simulation process for no reason
sim = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, sim, optimization_level=0)  # No optimization, because why bother?
job = sim.run(transpiled_qc, shots=1024)
results = job.result()
counts = results.get_counts()

print("Your quantum computer is questioning its existence:", counts)
plot_histogram(counts)

#Bruh, I told you its useless!
