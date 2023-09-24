from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
import numpy as np

# Define the parameters
teta = Parameter('teta')
phi = Parameter('phi')
lam = Parameter('lambda')

# Create a quantum circuit
qc = QuantumCircuit(4)

# Define the U gate
def U_gate(qc, qubit, teta, phi, lam):
    qc.u(teta, phi, lam, qubit)

# CCX Gate
U_gate(qc, 2, np.pi/2, phi, lam)
qc.cx(1, 2)
U_gate(qc, 2, -np.pi/2, phi, lam)
qc.cx(0, 2)
U_gate(qc, 2, np.pi/2, phi + lam, lam)
qc.cx(1, 2)
U_gate(qc, 2, -np.pi/2, phi + lam, lam)
qc.cx(0, 2)
U_gate(qc, 1, np.pi/2, phi + lam, lam)
U_gate(qc, 0, np.pi/2, phi + lam, lam)

# CCCX Gate
U_gate(qc, 3, np.pi/2, phi + lam, lam)
qc.cx(2, 3)
U_gate(qc, 3, -np.pi/2, phi + lam, lam)
qc.cx(1, 3)
U_gate(qc, 3, np.pi/2, phi + lam + np.pi/4 ,lam + np.pi/4 )
qc.cx(0 ,3)
U_gate(qc ,3 ,-np.pi/2 ,phi +lam+np.pi/4 ,lam+np.pi/4 )
qc.cx(1 ,3)
U_gate(qc ,3 ,np.pi/2 ,phi+lam+np.pi/4 ,lam+np.pi/4 )
qc.cx(0 ,3)
U_gate(qc ,3 ,-np.pi/2 ,phi+lam+np.pi/4 ,lam+np.pi/4 )
qc.cx(1 ,3)
U_gate(qc ,3 ,np.pi/2 ,phi+lam+np.pi/4 ,lam+np.pi/4 )
qc.cx(0 ,3)
U_gate(qc ,3 ,-np.pi/2 ,phi+lam+np.pi/4 ,lam+np.pi/4 )
qc.cx(1 ,3)

# Draw the circuit
print(qc)
