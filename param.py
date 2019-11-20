"""
param.py

The parameter file where settings can be changed

Written by Godwin Madho
"""

m=7 #ensemble size
n=3 #variables in simulation
p=[0,1,2] #observed variables
r=2.0 #observation error
tend=100.0 #time end
inf=1.00 #inflation
dt=0.01 #time step
nstep=100 #time steps before assimilation
#Observation file 
#Obsfile='x_truelen0.txt' #MATLAB FILE
Obsfile='lorenzdatahigh.txt'
Eavg='Eavg.txt' #Average save file
preA='preA.txt' #stores pre-corrected data point
obsA='obsA.txt' #stores the perturbed obervations
stat='STD.txt' #Statistic save file