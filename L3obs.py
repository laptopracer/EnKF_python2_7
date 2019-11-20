"""
L3obs.py

Get initial conditions of the Lorenz System. This can be done using either 
the matlab sample file or from a uniform distribution

Written by Godwin Madho
"""

import csv
import numpy as np
from param import Obsfile,r
import random

def L3Obs(tcur,n):
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
                
    obs.close()
      
    
    return(y)
    
if __name__ == '__main__':
    L3Obs()
