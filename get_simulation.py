# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import numpy as np
import scipy.signal as signal


def simulate_single_channel(
    mode: str = 'short', sfreq: int = 256, seconds: float = 10.0,
    f1: float = 25.0, f2: float = 40.0, seed: int = 123
    )-> np.array:
    """Generate time serie with high-frequency bursts.

    Adapted from [1, 2].

    Parameters
    ----------
    mode : str
        Length of the simulation (`'short'` or `'long'`). If `'long'` is selected,
        the simulation is extended to eight times its lenght. Burst patterns
        are repeated in time but the noise is not. Default is set to `'short'`.
    sfreq : int
        Sampling frequency. Default is set to 256 Hz.
    seconds : int
        Length of recording. If mode is set to ´'long'´, this will be multiplied by 8.
    f1, f2 : int
        Frequency of the first and second burst (Hz).

    Return
    ------
    x : numpy.array
        Array containing the simulation.

    References
    ----------
    [1] Quinn, A. J., van Ede, F., Brookes, M. J., Heideman, S. G.,
        Nowak, M., Seedat, Z. A., … Woolrich, M. W. (2019). Unpacking
        Transient Event Dynamics in Electrophysiological Power Spectra.
        Brain Topography, 32(6), 1020–1034. https://doi.org/10.1007/s10548-019-00745-5

    [2] https://github.com/OHBA-analysis/Quinn2019_BurstHMM/blob/master/hmm_util_get_simulation.m
    """

    # A noise time-course is created by direct pole-placement. This creates a filte
    # with an approximately 1/f frequency profile.
    time_vect = np.linspace(0, seconds, seconds*sfreq)

    # the value in poly is the filter root. it can vary between 0 < x < 1 where 0
    # is white noise and 1 is an extremely sloped spectrum
    # a is then the denominator polynomial of a digital filter which is used to
    # create the signal
    noise = np.random.random(len(time_vect))
    b, a = signal.butter(1, 0.5)
    x = signal.filtfilt(b, a, noise)

    # Define burst occurances and durations
    seconds = 10
    np.random.seed(seed)
    starts = np.sort(
        np.round(np.array([0.1, 0.3, 0.6, 0.9]) * (seconds/2) * sfreq)).astype(int)
    starts2 = (starts + (seconds/2 * sfreq)).astype(int)
    duration = np.round((np.random.random(4) + 0.1) * sfreq).astype(int)

    # Create burst time-courses
    x2 = np.zeros(seconds*sfreq)
    x3 = np.zeros(seconds*sfreq)

    for st, dur in zip(starts, duration):
        # Add slow burst
        tmp = np.sin(2*np.pi*f1*time_vect[st:st+dur])
        tmp = tmp * signal.tukey(len(tmp), alpha=.25)
        x2[st:st+dur] = x2[st:st+dur] + tmp

    for st, dur in zip(starts2, duration):
        # Add fast burst
        tmp = np.sin(2*np.pi*f2*time_vect[st:st+dur])
        tmp = tmp * signal.tukey(len(tmp), alpha=.25)
        x3[st:st+dur] = x3[st:st+dur] + tmp

    # sum the noise and burst time-courses to create the final simulation
    amp2 = .3
    amp3 = .3

    if mode == 'long':
        # Extend simulation to eight times its lenght
        # Burst patterns are repeated in time but the noise is not
        noise = np.random.random(len(time_vect) * 8)
        x = signal.filtfilt(b, a, noise)
        x2 = np.tile(amp2 * x2, (1, 8))
        x3 = np.tile(amp3 * x3, (1, 8))
        time_vect = np.linspace(0, seconds * 8, seconds * sfreq * 8)

    elif mode == 'short':
        # Return short form of simulation
        noise = np.random.random(len(time_vect))
        x = signal.filtfilt(b, a, noise)
        x2 = np.tile(amp2 * x2, (1, 1))
        x3 = np.tile(amp3 * x3, (1, 1))
    else:
        raise ValueError('Mode should be ´short´ or ´long´')

    data = x + x2 + x3

    # Concatenate different parts of simulation
    x = np.vstack([data, x2[0, :], x3[0, :]])

    return x