from qiskit import QuantumCircuit

def mcx_decomposed(qc, controls, target):
    num_controls = len(controls)

    if num_controls == 1:
        # Base case: single control is just a regular CX gate
        qc.cx(*controls, target)

        return

    # Recursive case: break down into smaller gates
    last = controls[-1]
    
    # Create a balanced tree of gates
    mcx_decomposed(qc, controls[:-1], last)

    # Use the last qubit to control an X on the target
    qc.cx(last, target)

    # "Uncompute" the tree of gates to reset the last qubit
    mcx_decomposed(qc, controls[:-1], last)

# Example usage:
qc = QuantumCircuit(5)

# Create a 4-controlled X gate
mcx_decomposed(qc, [0, 1, 2, 3], 4)

print(qc.draw())