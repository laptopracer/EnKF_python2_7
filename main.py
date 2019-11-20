"""
main.py

Main program which calls different programs for EnKF.

Written by Godwin Madho
"""
import os
import time
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from param import m,n,dt,tend,nstep,Eavg,stat
import L3ini
import L3rk4model
import L3obs
import calcH
import assimilation
import plotting


if __name__ == '__main__':
    times=time.clock()
    for filename in glob("en*.txt"):
        os.remove(filename)
    for filename in glob("preA.txt"):
        os.remove(filename)
    for filename in glob("obsA.txt"):
        os.remove(filename)
        
    plt.close('all') # closes all open figures
    7
    # Getting the initial ensemble
    print('Getting initial conditions')
    initial=L3ini.ini(n,m)
    x=initial[:]
    tcur=0.0
    
    # Saving the average
    Enavg=x.mean(1)
    avgsave=open(Eavg,'w')
    i=0
    avgsave.write(str(tcur))
    while i<len(Enavg):
        avgsave.write(';' + str(Enavg[i]))
        i=i+1
    avgsave.write('\n')
    avgsave.close()
    
    # Saving initial standard deviation
    SD=(np.std(x,axis=1))
    statsave=open(stat,'w')
    i=0
    statsave.write(str(tcur))
    while i<len(SD):
        statsave.write(';' + str(SD[i]))
        i=i+1
    statsave.write('\n')
    statsave.close()
    
    # Running the main code
    print('Running the main code')
    step=1
    
    while tcur<=tend:
        tcur=step*dt
        model=L3rk4model.L3Ens(tcur,x)
        x=model[1]
        
        # Saving standard deviation
        SD=(np.std(x,axis=1))
        statsave=open(stat,'a')
        i=0
        statsave.write(str(tcur))
        while i<len(SD):
            statsave.write(';' + str(SD[i]))
            i=i+1
        statsave.write('\n')
        statsave.close()
    
        # Assimilation
        
        if step%nstep==0:
            
            print(tcur),
            #Obtaining observations
            O=L3obs.L3Obs(tcur,n)
            y=O[:]
            #print(y),
            H=calcH.calc_H()
            Assim=assimilation.EnKF(x,y,tcur,H)
            x=Assim
            
            # Saving standard deviation
            SD=(np.std(x,axis=1))
            statsave=open(stat,'a')
            i=0
            statsave.write(str(tcur))
            while i<len(SD):
                statsave.write(';' + str(SD[i]))
                i=i+1
            statsave.write('\n')
            statsave.close()
        
        step=step+1
        
        
    # Calling the different plotting functions
    plotting.plotavg()
    plotting.plotens(m)
    plotting.STD()
    timee=time.clock()
    print("Time taken for the simulation =",timee-times)