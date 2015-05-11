from __future__ import division
import numpy as np

if __name__ == '__main__':
    NR = NB = 26
    
    V = np.zeros((NR, NB))
    A = np.chararray((NR, NB));
    A[:] = 'h'

    for nb in range(1, NB):
        V[0, nb] = nb
        A[0, nb] = 'h'

    for nr in range(1, NR):
        for nb in range(0, NB):
            Vhold = nb - nr
            Vdraw = (nr * V[nr-1, nb] + nb * V[nr, nb-1]) / (nr + nb)
            V[nr, nb] = max(Vhold, Vdraw)
            A[nr, nb] = 'h' if Vhold >= Vdraw else 'd'

    # print V[NR-1, NB-1]
    print A
