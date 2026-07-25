from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

#Oracle blackbox
def create_oracle(function_choice):
    if function_choice == 0:
        return
    elif function_choice == 1:
        qc.cx(0,1)
    elif function_choice == 2:
        qc.cx(0,1)
        qc.x(1)
    else:
        qc.x(1)

def print_function_type(circuit_output): #Argument of this function is known to the user but not to the algorithm
    return "constant" if circuit_output == {'0': 1024} else "balanced"

#Build quantum circuit
qc = QuantumCircuit(2,1)
qc.h(0)
qc.x(1)
qc.h(1)

create_oracle(2) 

#Last stage of circuit
qc.h(0)
qc.measure(0,0)

#Run simulated version of the quantum circuit just built
#Deutsch's algorithm returns function type with probability 1. So one measurement is enough (one shot)
result = AerSimulator().run(qc, shots = 1).result() 

print(result.get_counts())
print("The function is", print_function_type(result.get_counts()))
qc.draw('mpl')
plt.show()