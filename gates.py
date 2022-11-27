import numpy as np

ID = np.identity(2)
PAULY_X = np.matrix('0 1; 1 0')
PAULY_Y = 1j * np.matrix('0 -1; 1 0')
PAULY_Z = np.matrix('1 0; 0 -1')

H = (1 / np.sqrt(2)) * np.matrix('1 1; 1 -1')

h = np.matrix('1 1; 1 -1') # h without 1/sqrt(2)

CNOT = np.matrix('1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0')
CNOT2 = np.matrix('1 0 0 0; 0 0 0 1; 0 0 1 0; 0 1 0 0')  # CNOT but controlled swapped
CZ = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 -1')


def apply(gates: [np.matrix]):
    r = np.identity(gates[0].shape[0])
    for g in gates:
        r = r.dot(g)
    return r
