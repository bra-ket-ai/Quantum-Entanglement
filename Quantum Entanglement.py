# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT gate with the first qubit as control and the second as target
qc.cx(0, 1)

# Visualize the circuit
qc.draw(output='mpl', filename='/app/code/images/output_circuit_1.png')

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()

# Plot the statevector on a Bloch sphere
from qiskit.visualization import plot_bloch_multivector
plot_bloch_multivector(statevector, filename='/app/code/images/output_bloch_1.png')

# Execute the circuit on a simulator to get the measurement outcomes
simulator = Aer.get_backend('qasm_simulator')
qc.measure_all()
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# Plot the measurement outcomes
plot_histogram(counts, filename='/app/code/images/output_histogram_1.png')