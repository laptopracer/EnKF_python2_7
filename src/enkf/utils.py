"""Shared helpers for the EnKF experiments."""

import os
from glob import glob
from pathlib import Path


def clear_output_files(patterns, base_dir=None):
    search_dir = Path(base_dir) if base_dir else None
    for pattern in patterns:
        matches = glob(str(search_dir / pattern)) if search_dir else glob(pattern)
        for path in matches:
            if os.path.exists(path):
                os.remove(path)


def save_series(path, timestamp, values, mode='a'):
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open(mode) as handle:
        handle.write(str(timestamp))
        for value in values:
            handle.write(';' + str(value))
        handle.write('\n')


def write_ensemble_files(ensemble, timestamp, prefix='en', output_dir=None):
    output_path = Path(output_dir) if output_dir else None
    if output_path is not None:
        output_path.mkdir(parents=True, exist_ok=True)

    for member_idx in range(ensemble.shape[1]):
        destination = output_path / f'{prefix}{member_idx}.txt' if output_path else f'{prefix}{member_idx}.txt'
        with Path(destination).open('a') as handle:
            handle.write(str(timestamp))
            for state_idx in range(ensemble.shape[0]):
                handle.write(';' + str(ensemble[state_idx, member_idx]))
            handle.write('\n')
