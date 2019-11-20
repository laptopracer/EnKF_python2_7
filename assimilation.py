"""
assimilation.py

File containing the assimilation step

Written by Godwin Madho
"""
import numpy as np
from param import m,n,p,Eavg,inf,r,preA,obsA

def PertG():
    #creating a random distribution for the observed state
    np.random.RandomState()
    Anew=np.random.normal(size=(n,m))#scale=0.4
    return(Anew)
    
def PertK(A,K):
    np.random.RandomState()
    dis=np.random.normal(size=(n,m))*np.sqrt(2)
    Dmean=dis.mean(1)
    Dmean=(np.tile(Dmean,(m,1))).T
    Dnew=np.sqrt(m/(m-1.0))*(dis-Dmean)
    Anew=A+np.dot(K,Dnew-A)
    return(Anew)
    
def EnKF(x,y,tcur,H):
    
    Enavg=x.mean(1)
    
    #print(x)
    # Saving variables before correction
    avgsave=open(preA,'a')
    i=0
    avgsave.write(str(tcur))
    while i<len(Enavg):
        avgsave.write(';' + str(Enavg[i]))
        i=i+1
    avgsave.write('\n')
    avgsave.close()
    
    # Saving variables before correction
    avgsave=open(obsA,'a')
    i=0
    avgsave.write(str(tcur))
    while i<len(y):
        avgsave.write(';' + str(y[i]))
        i=i+1
    avgsave.write('\n')
    avgsave.close()
    
    A=(x-np.tile(Enavg,(m,1)).T)*inf
    
    HA=np.dot(H,A)
        
    HPHT=np.dot(HA,HA.T)/(m-1)
    
    PHT=np.dot(A,HA.T)/(m-1)
    
    R=np.identity(len(p))*r
    
    Ino=np.linalg.inv(HPHT+R)
    
    K=np.dot(PHT,Ino)
        
    dy=(y.T-Enavg)
    
    # Making sure the structure of the observation matches our simulation
    dy=np.dot(H,dy)
    dx=np.dot(K,dy.T) 
    
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
    avgsave=open(Eavg,'a')
    avgsave.write(str(tcur))
    while i<len(Enavg):
        avgsave.write(';' + str(Enavg[i]))
        i=i+1
    avgsave.write('\n')    
    avgsave.close()
    
    # Writing the current data in files
    i=0
    while i<m:
        en=open('en%s.txt' % (str(i)),'a')
        en.write(str(tcur))
        j=0
        while j<len(x[:,1]):
            en.write(';'+str(x[j,i]))
            j=j+1
            
        en.write('\n')
        en.close()
        i=i+1
        
    return(x)
   
if __name__ == '__main__':
    # assimilation.py executed as script
    EnKF()