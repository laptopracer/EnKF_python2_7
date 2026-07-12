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
from src.enkf import config as enkf_config
from src.enkf import L3Prini, L3Prmodel, L3Probs, calcH, assimilation, plotting
from src.enkf.utils import clear_output_files, save_series

m = enkf_config.m
n = enkf_config.n
n_obs = 3
dt = enkf_config.dt
tend = enkf_config.tend
nstep = enkf_config.nstep
enkf_config.n = 6
enkf_config.Eavg = str(enkf_config.PARAMETER_OUTPUT_DIR / 'Eavg.txt')
enkf_config.preA = str(enkf_config.PARAMETER_OUTPUT_DIR / 'preA.txt')
enkf_config.obsA = str(enkf_config.PARAMETER_OUTPUT_DIR / 'obsA.txt')
enkf_config.stat = str(enkf_config.PARAMETER_OUTPUT_DIR / 'STD.txt')
Eavg = enkf_config.Eavg
stat = enkf_config.stat
#import stats

if __name__ == '__main__':
    enkf_config.set_output_mode("parameter")

    times=time.perf_counter()
    clear_output_files(["en*.txt", "preA.txt", "obsA.txt"], base_dir=enkf_config.PARAMETER_OUTPUT_DIR)
        
    plt.close('all')
    # Getting the initial ensemble
    print('Getting initial conditions')
    initial=L3Prini.ini(m)
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
        model=L3Prmodel.L3Ens(tcur,x)
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
            O=L3Probs.L3Obs(tcur,n)
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
        
        
        
    plotting.plotavg()
    plotting.plotens(m)
    plotting.STD()
    plotting.Prplot()
    timee=time.perf_counter()
    print("Time taken for the simulation =",timee-times)
    
    #gc.collect()
