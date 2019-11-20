"""
Created on Mon Dec 14 10:39:16 2015

@author: py09gm

Solve the Lorenz model using the inbuilt python rk4 code
"""
import numpy as np
from param import m,dt,Eavg

def lorenz(xE,dt):
    Xdot=np.zeros([6])
    Xdot[0] = xE[3]*xE[1]-xE[3]*xE[0]
    Xdot[1] = xE[4]*xE[0]-xE[1]-xE[0]*xE[2]
    Xdot[2] = xE[0]*xE[1]-xE[5]*xE[2]
    Xdot[3] = 0.0
    Xdot[4] = 0.0
    Xdot[5] = 0.0
    return Xdot
    
def rk4(xE,dt):

    Rk1=lorenz(xE,dt)
    Rk2=lorenz(xE+(Rk1*dt/2),dt)
    Rk3=lorenz(xE+(Rk2*dt/2),dt)
    Rk4=lorenz(xE+(Rk3*dt),dt)
    x_new=xE+(dt/6.0)*(Rk1+(2.0*Rk2)+(2.0*Rk3)+Rk4)
    return x_new

def L3Ens(tcur,x):
    
    # Constants
    t=tcur
    
    Enum=0
    while Enum < m:
        xE=0.0
        x_new=0.0
        xE=x[:,Enum]
        x_new=rk4(xE,dt)
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