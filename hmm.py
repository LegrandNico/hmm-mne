# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import numpy as np
from sklearn.decomposition import PCA
from hmmlearn import hmm


def embedx(x, lags):
    """Embeds a [samples * channels] array X using a vector of time lags
    resulting in a [channels * samples * lags] array xe.
    
    Parameters
    ----------
    x : array
        Input data [channels x samples].
    lags : list
        The desired lags.

    Return
    ------
    xe : array
        The embedded data [channels, samples, lags]. xe contains
        only the valid subsection of the orignal data, after edge
        effects have been removed.
    valid : array
        Boolean array indexing the valid samples in xe.
    """
    Xe = np.zeros((x.shape[1], x.shape[0],  len(lags)))

    for l in range(len(lags)):
        Xe[:, :, l] = np.roll(x, lags[l], axis=0).swapaxes(0, 1)

    # Remove edges
    valid = np.ones((x.shape[0], 1), dtype=np.int8)
    valid[:np.abs(np.min(lags)), :] = 0
    valid[-np.abs(np.max(lags)):, :] = 0

    Xe = Xe[:, valid[:, 0] == 1, :]

    return Xe, valid


def hmm_tde(data, lags, n_states=3, n_components=8, **kwargs):
    """Time-delay embedded Hidden markov model.

    Adapted fro the HMM-MAR toolbox [3].
    
    Parameters
    ----------
    data : array
        Observations [channels * samples].
    lags : array | list
        Sample lags.
    n_states : int
        Number of states.
    n_components : int
        Number of components for the PCQ decomposition.

    Return
    ------
    gamma : array
        Time courses of the states probabilities given data.
    model : hmm-learn object.
        Estimated HMM model.
    xe : array
        Embedded data [channels * samples * lags]

    References
    ----------
    [1] Quinn, A. J., van Ede, F., Brookes, M. J., Heideman, S. G., Nowak, M., Seedat,
        Z. A., … Woolrich, M. W. (2019). Unpacking Transient Event Dynamics in
        Electrophysiological Power Spectra. Brain Topography, 32(6), 1020–1034.
        https://doi.org/10.1007/s10548-019-00745-5

    [2] Vidaurre, D., Hunt, L. T., Quinn, A. J., Hunt, B. A. E., Brookes, M. J., Nobre, A. C.,
        & Woolrich, M. W. (2018). Spontaneous cortical activity transiently organises into frequency
        specific phase-coupling networks. Nature Communications, 9(1).
        https://doi.org/10.1038/s41467-018-05316-z

    [3] https://github.com/OHBA-analysis/HMM-MAR
    """

    # Embed time serie
    xe, valid = embedx(data, lags)

    pca = PCA(n_components=n_components)
    y = pca.fit_transform(xe[0, :, :])

    model = hmm.GaussianHMM(n_components=n_states, n_iter=100, covariance_type='full', **kwargs)
    model.fit(y)
    gamma = model.predict_proba(y)
    
    return gamma, model, xe