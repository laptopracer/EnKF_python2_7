"""
L3ini.py

Get initial conditions of the Lorenz System. This can be done using either 
the matlab sample file or from a uniform distribution

Written by Godwin Madho
"""
import scipy.io
import numpy as np
import random
from pathlib import Path
from .config import m,n,L3_samples_file, ensure_data_files, get_output_path

def ini(n,m):
    ensure_data_files()
    x=np.zeros([n,m])
    
    mat = scipy.io.loadmat(L3_samples_file)
    S=mat['S']
    
    '''
    # Getting ensembles sequentially
    i=0
    while i<n:
        j=0
        while j<m:
            x[i,j]=S[i,j+1]
            j=j+1
        i=i+1
    '''
    
    # Getting the number of columns and shuffling them
    P=list(range(1,10000))
    random.seed()
    random.shuffle(P)
    
    i=0
    while i<m:
        K=0
        # Getting the number for the column
        K=P[i]
        # Passing the data in the column be added to the ensemble
        L=S[:,K]
        
        j=0
        while j<n:
            x[j,i]=L[j]
            j+=1
        i+=1
    
    """
    # Gaussian distribution to obtain random initial conditions
    i=0
    while i<m:
        x[0,i]=random.uniform(-20.0,20.0)
        x[1,i]=random.uniform(-20.0,20.0)
        x[2,i]=random.uniform(0.0,40.0)
        i=i+1
    """
    
    # writing the initial conditions in saperate files
    t=0.0
    i=0
    while i<m:
        output_path = Path(get_output_path(f'en{i}.txt'))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open('w') as en:
            en.write(str(t))
            j=0
            while j<len(x[:,1]):
                en.write(';'+str(x[j,i]))
                j=j+1
            en.write('\n')
                
        i=i+1
        
    return(x)
    
if __name__ == '__main__':
    ini()