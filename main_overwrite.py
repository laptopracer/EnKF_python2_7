import time
import numpy as np
import matplotlib.pyplot as plt
from src.enkf.config import m, n, dt, tend, nstep, Eavg, stat
from src.enkf import L3ini, L3rk4model, L3obs, calcH, assimilation, plotting
from src.enkf.utils import clear_output_files, save_series


if __name__ == '__main__':
    start_time = time.perf_counter()
    clear_output_files(["en*.txt", "preA.txt", "obsA.txt"])

    plt.close('all')

    print('Getting initial conditions')
    x = L3ini.ini(n, m)
    tcur = 0.0

    save_series(Eavg, tcur, x.mean(axis=1), mode='w')
    save_series(stat, tcur, np.std(x, axis=1), mode='w')

    print('Running the main code')
    step = 1

    while tcur <= tend:
        tcur = step * dt
        x = L3rk4model.L3Ens(tcur, x)[1]

        save_series(stat, tcur, np.std(x, axis=1), mode='a')

        if step % nstep == 0:
            print(tcur)
            observations = L3obs.L3Obs(tcur, n)
            H = calcH.calc_H()
            x = assimilation.EnKF(x, observations, tcur, H)
            save_series(stat, tcur, np.std(x, axis=1), mode='a')

        step += 1

    plotting.plotavg()
    plotting.plotens(m)
    plotting.STD()
    elapsed = time.perf_counter() - start_time
    print("Time taken for the simulation =", elapsed)
