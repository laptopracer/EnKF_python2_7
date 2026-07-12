"""
calcH.py

Calculate matrix to line up simulation to observation

Written by Godwin Madho
"""
import numpy as np
from . import config


def calc_H():
    
    H=np.zeros([len(config.p), config.n])

    i=0
    while i<len(config.p):
        pp=config.p[i]
        H[i,pp]=1
        i=i+1
    #print(H)
    return(H)
    
if __name__ == '__main__':
    # LorEns.py executed as script
    calc_H()
