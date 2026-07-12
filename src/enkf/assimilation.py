"""
assimilation.py

File containing the assimilation step

Written by Godwin Madho
"""
import numpy as np
from pathlib import Path
from . import config

m = config.m
p = config.p
Eavg = config.Eavg
inf = config.inf
r = config.r
preA = config.preA
obsA = config.obsA

def PertG():
    #creating a random distribution for the observed state
    np.random.RandomState()
    Anew=np.random.normal(size=(config.n,m))#scale=0.4
    return(Anew)
    
def PertK(A,K):
    np.random.RandomState()
    obs_dim = len(p)
    dis=np.random.normal(size=(obs_dim,m))*np.sqrt(2)
    Dmean=dis.mean(1)
    Dmean=(np.tile(Dmean,(m,1))).T
    Dnew=np.sqrt(m/(m-1.0))*(dis-Dmean)
    Anew=A + np.dot(K, Dnew)
    return(Anew)
    
def EnKF(x,y,tcur,H):
    
    Enavg=x.mean(1)
    
    #print(x)
    # Saving variables before correction
    pre_path = Path(preA)
    pre_path.parent.mkdir(parents=True, exist_ok=True)
    with pre_path.open('a') as avgsave:
        i=0
        avgsave.write(str(tcur))
        while i<len(Enavg):
            avgsave.write(';' + str(Enavg[i]))
            i=i+1
        avgsave.write('\n')
    
    # Saving variables before correction
    obs_path = Path(obsA)
    obs_path.parent.mkdir(parents=True, exist_ok=True)
    with obs_path.open('a') as avgsave:
        i=0
        avgsave.write(str(tcur))
        while i<len(y):
            avgsave.write(';' + str(y[i]))
            i=i+1
        avgsave.write('\n')
    
    A=(x-np.tile(Enavg,(m,1)).T)*inf
    
    HA=np.dot(H,A)
        
    HPHT=np.dot(HA,HA.T)/(m-1)
    
    PHT=np.dot(A,HA.T)/(m-1)
    
    R=np.identity(len(p))*r
    
    Ino=np.linalg.inv(HPHT+R)
    
    K=np.dot(PHT,Ino)
        
    # Innovation in observation space using the observation operator.
    dy = y - np.dot(H, Enavg)
    dx = np.dot(K, dy) 
    
    # New initial state
    Xa=Enavg+dx
    
    #creating a random distribution for the observed state
    #Anew=PertG()
    Anew=PertK(A,K)
    
    # Creating the new ensemble            
    x=(Anew+(np.tile(Xa,(m,1))).T)
    
    # Saving the average
    Enavg=x.mean(1)
    i=0
    avg_path = Path(Eavg)
    avg_path.parent.mkdir(parents=True, exist_ok=True)
    with avg_path.open('a') as avgsave:
        avgsave.write(str(tcur))
        while i<len(Enavg):
            avgsave.write(';' + str(Enavg[i]))
            i=i+1
        avgsave.write('\n')
    
    # Writing the current data in files
    i=0
    while i<m:
        output_path = Path(config.get_output_path(f'en{i}.txt'))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open('a') as en:
            en.write(str(tcur))
            j=0
            while j<len(x[:,1]):
                en.write(';'+str(x[j,i]))
                j=j+1
                
            en.write('\n')
        i=i+1
        
    return(x)
   
if __name__ == '__main__':
    # assimilation.py executed as script
    EnKF()