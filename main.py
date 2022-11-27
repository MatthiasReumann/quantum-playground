import numpy as np
import gates as g

def exercise5_2():
    l = np.matrix('1 0; 0 1j')
    v = g.apply([g.h, l, g.h])
    v2 = np.dot(v, v)
    print(v)
    print(1/4 * v2) # factors are missing bc. of g.h (instead of g.H)

if __name__ == "__main__":
    exercise5_2()