"""
L3obs.py

Get initial conditions of the Lorenz System. This can be done using either 
the matlab sample file or from a uniform distribution

Written by Godwin Madho
"""

import csv
import os
import numpy as np
from .config import Obsfile,r,ensure_data_files
import random

def L3Obs(tcur,n):
    ensure_data_files()
    obs=open(Obsfile,'r')
    da=csv.reader(obs,delimiter=';')
    y=np.zeros([n])
    for line in da:
        # when the 1st column in the file is time
        fline=line[0]
        
        if str(fline)==str(tcur):
           
            i=1
            while i<len(line):
                y[i-1]=float(line[i])+random.uniform(-r,r)
                i=i+1
            break
    if n >= 4:
        y[3]=(10.0+random.uniform(-2.0,2.0))
    if n >= 5:
        y[4]=(28.0+random.uniform(-4.0,4.0))
    if n >= 6:
        y[5]=(8.0/3.0+random.uniform(-0.5,0.5))
    obs.close()
      
    #print(y)
    return(y)
    
if __name__ == '__main__':
    # LorEns.py executed as script
    L3Obs()
