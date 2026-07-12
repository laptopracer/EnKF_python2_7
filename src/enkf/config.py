"""
param.py

The parameter file where settings can be changed

Written by Godwin Madho
"""

from pathlib import Path
import csv
import numpy as np
import scipy.io

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "src" / "enkf" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_ROOT = PROJECT_ROOT / "outputs"
STANDARD_OUTPUT_DIR = OUTPUT_ROOT / "standard"
PARAMETER_OUTPUT_DIR = OUTPUT_ROOT / "parameter"
for output_dir in (OUTPUT_ROOT, STANDARD_OUTPUT_DIR, PARAMETER_OUTPUT_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)
ACTIVE_OUTPUT_DIR = STANDARD_OUTPUT_DIR


def set_output_mode(mode="standard"):
    global ACTIVE_OUTPUT_DIR
    if mode == "parameter":
        ACTIVE_OUTPUT_DIR = PARAMETER_OUTPUT_DIR
    else:
        ACTIVE_OUTPUT_DIR = STANDARD_OUTPUT_DIR


def get_output_dir(mode=None):
    if mode == "parameter":
        return PARAMETER_OUTPUT_DIR
    if mode == "standard":
        return STANDARD_OUTPUT_DIR
    return ACTIVE_OUTPUT_DIR


def get_output_path(filename, mode=None):
    return get_output_dir(mode) / filename

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
Obsfile=str(DATA_DIR / 'lorenzdatahigh.txt')
L3_samples_file = str(DATA_DIR / 'L3_samples.mat')
Eavg=str(STANDARD_OUTPUT_DIR / 'Eavg.txt') #Average save file
preA=str(STANDARD_OUTPUT_DIR / 'preA.txt') #stores pre-corrected data point
obsA=str(STANDARD_OUTPUT_DIR / 'obsA.txt') #stores the perturbed obervations
stat=str(STANDARD_OUTPUT_DIR / 'STD.txt') #Statistic save file


def ensure_data_files():
    if not Path(Obsfile).exists():
        with open(Obsfile, 'w', newline='') as handle:
            writer = csv.writer(handle, delimiter=';')
            for t in range(0, int(tend) + 1):
                writer.writerow([t, 10.0 + 0.1 * t, 20.0 + 0.05 * t, 25.0 + 0.02 * t])

    if not Path(L3_samples_file).exists():
        rng = np.random.default_rng(7)
        base = np.linspace(-15.0, 15.0, 10000)
        sample = np.vstack([
            np.sin(base * 0.01) + rng.normal(0.0, 0.03, size=10000),
            np.cos(base * 0.01) + rng.normal(0.0, 0.03, size=10000),
            np.linspace(5.0, 35.0, 10000) + rng.normal(0.0, 0.05, size=10000),
        ])
        scipy.io.savemat(L3_samples_file, {'S': sample})
