"""
L3rk4model.py

Solve the Lorenz model using rk4.

Written by Godwin Madho
"""
import numpy as np
from param import m,dt,Eavg
#import random

def lorenz(xE,dt,sig,r,b):
    Xdot=np.zeros([3])
    Xdot[0] = sig*xE[1]-sig*xE[0]
    Xdot[1] = r*xE[0]-xE[1]-xE[0]*xE[2]
    Xdot[2] = xE[0]*xE[1]-b*xE[2]
    return Xdot
    
def rk4(xE,dt,sig,r,b):

    Rk1=lorenz(xE,dt,sig,r,b)
    Rk2=lorenz(xE+(Rk1*dt/2),dt,sig,r,b)
    Rk3=lorenz(xE+(Rk2*dt/2),dt,sig,r,b)
    Rk4=lorenz(xE+(Rk3*dt),dt,sig,r,b)
    x_new=xE+(dt/6.0)*(Rk1+(2.0*Rk2)+(2.0*Rk3)+Rk4)
    return x_new

def L3Ens(tcur,x):
  
  # constants
    sig=10.0 #10.0
    r=28.0 #28.0
    b=8.0/3.0 #8.0/3.0
    t=tcur
    
    Enum=0 #Ensemble number
    while Enum<m:
        xE=0.0
        x_new=0.0
        xE=x[:,Enum]
        x_new=rk4(xE,dt,sig,r,b)
        x[:,Enum]=x_new
                            
        Enum=Enum+1

    
    # Writing the current data in files
    i=0
    while i<m:
        en=open('en%s.txt' % (str(i)),'a')
        en.write(str(t))
        j=0
        while j<len(x[:,1]):
            en.write(';'+str(x[j,i]))
            j=j+1
            
        en.write('\n')
        en.close()
        i=i+1
     
    # Writing the average in a file to be used later
    Enavg=x.mean(1)
    avgsave=open(Eavg,'a')
    i=0
    avgsave.write(str(t))
    while i<len(Enavg):
        avgsave.write(';' + str(Enavg[i]))
        i=i+1
    avgsave.write('\n')    
    avgsave.close()
    
    return(tcur,x)
    
if __name__ == '__main__':
    # LorEns.py executed as script
    L3Ens()