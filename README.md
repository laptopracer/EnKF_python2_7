# EnKF Python 2.7

This repository contains a compact Python implementation of an Ensemble Kalman Filter (EnKF) applied to the Lorenz system. The code follows a classic forecast-assimilation loop: an ensemble of possible states is propagated forward by a dynamical model, observations are compared with the forecast, and the ensemble is corrected so it better matches the data.

## What this project does

The goal is to estimate the state of a chaotic dynamical system from partial and noisy observations. In this repository, the dynamical system is the Lorenz-63 model, and the estimation method is an EnKF.

## Ensemble Kalman Filter (EnKF)

EnKF is a Monte Carlo approximation of the Kalman filter. Instead of propagating a single state estimate and its covariance, it propagates an ensemble of many possible states.

The main idea is:

1. Start from an initial ensemble of plausible states.
2. Propagate each member forward in time using the model.
3. Compare the ensemble mean with observations.
4. Compute an update direction based on the ensemble covariance.
5. Adjust the ensemble members so they are closer to the observations while preserving the model dynamics.

This makes EnKF especially useful for nonlinear systems such as the Lorenz system, where the standard Kalman filter is not always appropriate.

## Lorenz System

The Lorenz system is a classical three-variable chaotic model:

- $\dot{x} = \sigma(y - x)$
- $\dot{y} = x(\rho - z) - y$
- $\dot{z} = xy - \beta z$

In this project, the default parameters are:

- $\sigma = 10$
- $\rho = 28$
- $\beta = 8/3$

These values produce the well-known chaotic behaviour that makes the system sensitive to small changes in initial conditions.

## How the code works

The workflow is implemented as a sequence of forecast and analysis steps:

1. An initial ensemble is generated from sampled data in [src/enkf/L3ini.py](src/enkf/L3ini.py) or the parameter-estimation variant in [src/enkf/L3Prini.py](src/enkf/L3Prini.py).
2. The ensemble is advanced forward in time using a fourth-order Runge-Kutta solver in [src/enkf/L3rk4model.py](src/enkf/L3rk4model.py) or [src/enkf/L3Prmodel.py](src/enkf/L3Prmodel.py).
3. At regular intervals, observations are read from the configured observation data file in [src/enkf/L3obs.py](src/enkf/L3obs.py) or [src/enkf/L3Probs.py](src/enkf/L3Probs.py).
4. The observation operator in [src/enkf/calcH.py](src/enkf/calcH.py) maps the model state into observation space.
5. The EnKF update is applied in [src/enkf/assimilation.py](src/enkf/assimilation.py), where the ensemble is adjusted toward the observations.
6. Summary files and plots are written so the user can inspect the ensemble mean, standard deviation, and assimilation behaviour.

## Repository layout

- [main.py](main.py) runs the standard Lorenz-system experiment.
- [mainPr.py](mainPr.py) runs the parameter-estimation variant with additional state variables for the model parameters.
- [src/enkf](src/enkf) contains the core implementation modules:
  - [src/enkf/config.py](src/enkf/config.py) stores the runtime parameters such as ensemble size, time step, inflation, observation settings, and output locations.
  - [src/enkf/L3ini.py](src/enkf/L3ini.py) creates the initial ensemble for the standard experiment.
  - [src/enkf/L3rk4model.py](src/enkf/L3rk4model.py) advances the ensemble using a fourth-order Runge-Kutta solver for the Lorenz system.
  - [src/enkf/L3obs.py](src/enkf/L3obs.py) loads observations and prepares the measurement vector.
  - [src/enkf/calcH.py](src/enkf/calcH.py) constructs the observation operator matrix.
  - [src/enkf/assimilation.py](src/enkf/assimilation.py) performs the EnKF update step.
  - [src/enkf/plotting.py](src/enkf/plotting.py) creates diagnostic plots of the ensemble mean, standard deviation, and assimilation behaviour.
  - [src/enkf/L3Prini.py](src/enkf/L3Prini.py), [src/enkf/L3Prmodel.py](src/enkf/L3Prmodel.py), and [src/enkf/L3Probs.py](src/enkf/L3Probs.py) implement the parameter-estimation variant.
- [outputs](outputs) stores generated files, with separate subfolders for the standard run and the parameter-estimation run.

## Running the code

From the repository root, run:

- `python main.py` for the standard state-estimation experiment
- `python mainPr.py` for the parameter-estimation experiment

The scripts use the configuration in [src/enkf/config.py](src/enkf/config.py) and write their outputs into [outputs/standard](outputs/standard) or [outputs/parameter](outputs/parameter).

## Output files

The main run produces files such as:

- [outputs/standard/Eavg.txt](outputs/standard/Eavg.txt) for the ensemble mean over time
- [outputs/standard/STD.txt](outputs/standard/STD.txt) for the ensemble standard deviation
- [outputs/standard/en0.txt](outputs/standard/en0.txt) and the other ensemble files for each member
- [outputs/standard/preA.txt](outputs/standard/preA.txt) and [outputs/standard/obsA.txt](outputs/standard/obsA.txt) for pre-update and observation values

## Notes

- The project originally started as a Python 2-style prototype, but it has been reorganized into a clearer package structure and adapted to run with modern Python.
- The implementation is intentionally simple and educational, making it suitable for understanding the core mechanics of EnKF on a chaotic dynamical system.
