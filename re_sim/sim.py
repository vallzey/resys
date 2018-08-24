import numpy as np


def euclidSim(inA, inB):
    return 1.0/(1.0 + np.linalg.norm())

def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    return 0.5+0.5*np.corrcoef(inA, inB, rowvar=0)[0][1]

def cosSim(inA, inB):
    num = float(inA.T*inB)
    denom = np.linalg.norm(inA)*np.linalg.norm(inB)
    return 0.5+0.5*(num/denom)