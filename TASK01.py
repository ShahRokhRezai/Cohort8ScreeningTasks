from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit import execute, Aer

def controlled_z_sum(number_1, number_2):
  circuit = QuantumCircuit(len(number_2))
  for i in range(len(number_2)):
    circuit.h(i)
  for i in range(len(number_2)):
    if number_2[i] + number_2[(i + 1) % len(number_2)] == number_1:
      circuit.cz(i, (i + 1) % len(number_2))
  return circuit

def grover_oracle(number_1, number_2):
  circuit = QuantumCircuit(len(number_2) + 1) # Here we add 1 to the circuit size
  cz_gate = controlled_z_sum(number_1, number_2).to_gate()
  circuit.append(cz_gate.control(1), range(len(number_2) + 1)) # Here we add 1 to range
  return circuit

def find_the_primes_numbers(number_1, number_2):
  qreg = QuantumRegister(len(number_2) + 1) # Here we add 1 to quantum register
  creg = ClassicalRegister(len(number_2) + 1) # Here we add 1 to classical register
  circuit = QuantumCircuit(qreg, creg)
  
  # Apply the Grover oracle
  circuit.append(grover_oracle(number_1, number_2), range(len(number_2) + 1)) # Here we add 1 to range
  
  for i in range(len(number_2)):
    circuit.h(qreg[i])
    circuit.z(qreg[i])
    circuit.h(qreg[i])
  
  print(circuit.draw()) # Draw the circuit here
  
  # Measure all qubits.
  circuit.measure(qreg, creg)
  
  result = execute(circuit, Aer.get_backend('qasm_simulator')).result()
  
  counts = result.get_counts()
  
  primes = []
  
  for key, value in counts.items():
    index = int(key)
    if value == max(counts.values()) and index < len(number_2):
      primes.append(number_2[index])
  
  return primes

number_1 = 18
number_2 = [1, 3, 5, 7, 11, 13, 15]
primes = find_the_primes_numbers(number_1, number_2)
print(primes)