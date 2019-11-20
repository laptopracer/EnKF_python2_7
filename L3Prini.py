"""
L3ini.py

Get initial conditions of the Lorenz System for parameter estimation

Written by Godwin Madho
"""
import scipy.io
import numpy as np
import random

def ini(m):
    x=np.zeros([6,m])
    
    mat = scipy.io.loadmat('L3_samples.mat')
    S=mat['S']
    
    # Getting the number of columns and shuffling them
    P=range(1,10000)
    random.seed()
    random.shuffle(P)
    
    i=0
    while i<m:
        # Getting the number for the column
        K=P[i]
        # Passing the data in the column be added to the ensemble
        L=S[:,K]
        
        j=0
        while j<3:
            x[j,i]=L[j]
            j+=1
        i+=1
    
    i=0
    while i<m:
	"""
    	x[0,i]=random.uniform(-20.0,20.0)
    	x[1,i]=random.uniform(-20.0,20.0)
    	x[2,i]=random.uniform(0.0,40.0)
    	"""
        x[3,i]=10.0+random.uniform(-4.0,4.0)
        x[4,i]=28.0+random.uniform(-5.0,5.0)
        x[5,i]=8.0/3.0+random.uniform(-0.5,0.5)
        i=i+1
    
    # writing the initial conditions in saperate files
    t=0.0
    i=0
    while i<m:
        en=open('en%s.txt' % (str(i)),'w')
        en.write(str(t))
        j=0
        while j<len(x[:,1]):
            en.write(';'+str(x[j,i]))
            j=j+1
        en.write('\n')
        en.close()
                
        i=i+1
        
    return(x)
    
if __name__ == '__main__':
    ini()
