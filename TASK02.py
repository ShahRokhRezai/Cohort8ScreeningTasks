import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer

def encode_numbers(numbers):
    num_qubits = len(numbers).bit_length()
    circuit = QuantumCircuit(num_qubits)
    for i, number in enumerate(numbers):
        binary_string = format(i, f'0{num_qubits}b')
        for j in range(num_qubits):
            if binary_string[j] == '1':
                circuit.x(j)
    circuit.h(range(num_qubits))
    return circuit

def negative_number_oracle(numbers):
    num_qubits = len(numbers).bit_length()
    circuit = QuantumCircuit(num_qubits)
    for i, number in enumerate(numbers):
        if number < 0:
            binary_string = format(i, f'0{num_qubits}b')
            for j in range(num_qubits):
                if binary_string[j] == '1':
                    circuit.z(j)
    return circuit

def find_negative_numbers(numbers):
    circuit = encode_numbers(numbers)
    oracle = negative_number_oracle(numbers)
    circuit.append(oracle, range(len(numbers).bit_length()))
    print(circuit.draw())
    result = execute(circuit, Aer.get_backend('statevector_simulator')).result()
    for i, amplitude in enumerate(np.asarray(result.get_statevector())):
        if abs(amplitude) > 1e-6 and amplitude.real < 0:
            return True
    return False

A = find_negative_numbers([1,-3,2,15])
print(A)  # True

B = find_negative_numbers([1,4,8,11])
print(B)  # False

C = find_negative_numbers([-15,-14,2,-1])
print(C)  # True
