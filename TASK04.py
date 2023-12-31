# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G2_ja5b8iDgUvauWkt7wWgam5gy4lz6_
"""

!pip install qiskit

!pip install qiskit-aer

from qiskit import QuantumCircuit, execute, Aer
from qiskit.providers.aer.noise import NoiseModel, depolarizing_error

def swap_test_success_probability(depolarization_error_probability):
  # Create a quantum circuit
  circuit = QuantumCircuit(4)

  # Create a Bell state
  circuit.h(0)
  circuit.cx(0, 1)

  # Create a noise model with a depolarizing error
  noise_model = NoiseModel()
  error = depolarizing_error(depolarization_error_probability, 2) # Change this line
  noise_model.add_all_qubit_quantum_error(error, ['cx']) # And this line

  # Apply the SWAP test
  circuit.cx(0, 2)
  circuit.cx(1, 3)
  circuit.cx(0, 2)

  # Measure the qubits in the Z basis
  circuit.measure_all()

  # Simulate the circuit with the noise model
  simulator = Aer.get_backend('qasm_simulator')
  results = execute(circuit, simulator, noise_model=noise_model).result()

  # Calculate the success probability
  success_probability = results.get_counts().get('0001', 0) / sum(results.get_counts().values())

  return success_probability



import numpy as np
import matplotlib.pyplot as plt

depolarization_error_probabilities = np.linspace(0.3, 0.7)
success_probabilities = []
for depolarization_error_probability in depolarization_error_probabilities:
  success_probability = swap_test_success_probability(depolarization_error_probability)
  success_probabilities.append(success_probability)

plt.plot(depolarization_error_probabilities, success_probabilities, 'o-')
plt.xlabel('Depolarization error probability')
plt.ylabel('Success probability of the SWAP test')
plt.title('Success probability of the SWAP test as a function of the depolarization error probability')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

depolarization_error_probabilities = np.linspace(0.6, 0.4)
success_probabilities = []
for depolarization_error_probability in depolarization_error_probabilities:
  success_probability = swap_test_success_probability(depolarization_error_probability)
  success_probabilities.append(success_probability)

plt.plot(depolarization_error_probabilities, success_probabilities, 'o-')
plt.xlabel('Depolarization error probability')
plt.ylabel('Success probability of the SWAP test')
plt.title('Success probability of the SWAP test as a function of the depolarization error probability')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, execute, Aer

# Normalize the state vector
state_vector = np.array([0.1, 0.2, 0.6, 0.1])
normalized_state_vector = state_vector / np.linalg.norm(state_vector)

# Create a quantum circuit
circuit = QuantumCircuit(3, 1)

# Prepare the normalized state on the first two qubits
circuit.initialize(normalized_state_vector.tolist(), [0, 1])

# Apply the SWAP test
circuit.h(2)
circuit.cswap(2, 0, 1)
circuit.h(2)

# Measure the first qubit in the Z basis
circuit.measure(2, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
results = execute(circuit, simulator).result()

# Calculate the success probability of the SWAP test
counts = results.get_counts()
success_probability = counts.get('0', 0) / sum(counts.values())

# Print the success probability
print('Success probability:', success_probability)

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, execute, Aer
from qiskit.providers.aer.noise import NoiseModel, depolarizing_error

# Normalize the state vector
state_vector = np.array([0, 0.5, 0.1, 0.4])
normalized_state_vector = state_vector / np.linalg.norm(state_vector)

# Create a quantum circuit
circuit = QuantumCircuit(3, 1)

# Prepare the normalized state on the first two qubits
circuit.initialize(normalized_state_vector.tolist(), [0, 1])

# Apply the SWAP test
circuit.h(2)
circuit.cswap(2, 0, 1)
circuit.h(2)

# Measure the first qubit in the Z basis
circuit.measure(0, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
results = execute(circuit, simulator).result()

# Calculate the success probability of the SWAP test
counts = results.get_counts()
success_probability = counts.get('0', 0) / sum(counts.values())

# Print the success probability
print('Success probability:', success_probability)

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, execute, Aer

# Normalize the state vector
state_vector = np.array([0.01, 0.10, 0.12, 0.13, 0.04, 0, 0.35, 0.25])
normalized_state_vector = state_vector / np.linalg.norm(state_vector)

# Create a quantum circuit
circuit = QuantumCircuit(4, 1)

# Prepare the normalized state on the first three qubits
circuit.initialize(normalized_state_vector.tolist(), [0, 1, 2])

# Apply the SWAP test
circuit.h(3)
circuit.cswap(3, 0, 1)
circuit.cswap(3, 1, 2)
circuit.h(3)

# Measure the first qubit in the Z basis
circuit.measure(3, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
results = execute(circuit, simulator).result()

# Calculate the success probability of the SWAP test
counts = results.get_counts()
success_probability = counts.get('0', 0) / sum(counts.values())

# Print the success probability
print('Success probability:', success_probability)

from qiskit import QuantumCircuit, execute, Aer
from qiskit.providers.aer.noise import NoiseModel, depolarizing_error

# Normalize the state vector
state_vector = np.array([0.01, 0.10, 0.12, 0.13, 0.04, 0, 0.35, 0.25])
normalized_state_vector = state_vector / np.linalg.norm(state_vector)

# Create a quantum circuit
circuit = QuantumCircuit(4, 1)

# Prepare the normalized state on the first three qubits
circuit.initialize(normalized_state_vector.tolist(), [0, 1, 2])

# Apply the SWAP test
circuit.h(3)
circuit.cswap(3, 0, 1)
circuit.cswap(3, 1, 2)
circuit.h(3)

# Measure the first qubit in the Z basis
circuit.measure(3, 0)

# Create a noise model with depolarizing error
noise_model = NoiseModel()
for i in range(4):
    error = depolarizing_error(0.01, 1) # Change this value for different error rates
    noise_model.add_quantum_error(error, ['u1', 'u2', 'u3'], [i])

# Simulate the circuit with the noise model
simulator = Aer.get_backend('qasm_simulator')
results = execute(circuit, simulator, noise_model=noise_model).result()

# Calculate the success probability of the SWAP test
counts = results.get_counts()
success_probability = counts.get('0', 0) / sum(counts.values())

# Print the success probability
print('Success probability:', success_probability)

import numpy as np
from math import ceil, log2
from qiskit import QuantumCircuit, execute, Aer
from qiskit.providers.aer.noise import NoiseModel, depolarizing_error

# Your state vector
state_vector = np.array([0, 0.2, 0.2, 0.1, 0.2, 0.05, 0.05, 0.2, 0, 0])

# Calculate the next power of 2
next_power_of_2 = 2**ceil(log2(len(state_vector)))

# Pad the state vector with zeros
padded_state_vector = np.pad(state_vector, (0, next_power_of_2 - len(state_vector)))

# Normalize the state vector
normalized_state_vector = padded_state_vector / np.linalg.norm(padded_state_vector)

# Create a quantum circuit
circuit = QuantumCircuit(5, 1)

# Prepare the normalized state on the first four qubits
circuit.initialize(normalized_state_vector.tolist(), [0, 1, 2, 3])

# Apply the SWAP test
circuit.h(4)
circuit.cswap(4, 0, 1)
circuit.cswap(4, 1, 2)
circuit.cswap(4, 2, 3)
circuit.h(4)

# Measure the first qubit in the Z basis
circuit.measure(4, 0)

# Create a noise model with depolarizing error
noise_model = NoiseModel()
for i in range(5):
    error = depolarizing_error(0.01, 1) # Change this value for different error rates
    noise_model.add_quantum_error(error, ['u1', 'u2', 'u3'], [i])

# Simulate the circuit with the noise model
simulator = Aer.get_backend('qasm_simulator')
results = execute(circuit, simulator, noise_model=noise_model).result()

# Calculate the success probability of the SWAP test
counts = results.get_counts()
success_probability = counts.get('0', 0) / sum(counts.values())

# Print the success probability
print('Success probability:', success_probability)