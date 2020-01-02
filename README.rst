
An introduction to Hidden Markov Modelling for electrophysiological data.

This repository introduce Hidden Markov Modelling (HMM) of electrophysiological data .

The HMM inference is realized using the `hmm-learn library <https://hmmlearn.readthedocs.io/en/stable/>`_.

Envelope threshold and HMM
==========================

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Simulation.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/NarrowBand.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/WiderBand.png
  :align:   center

Time Delay Embedded HMM
=======================

Implementation of the Time Delay Embedded HMM (TDE-HMM) described in [#].

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/tde-hmm.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Spectral0.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Spectral.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Spectral2.png
  :align:   center

Notes
=====

This repository is a Python adaptation of some of the functionalities proposed by the HMM-MAR toolbox [#]. It was created for educational purpose. You should refer to the original Matlab toolbox is you want to use HMM for research.

References
==========

[#] Quinn, A. J., van Ede, F., Brookes, M. J., Heideman, S. G., Nowak, M., Seedat, Z. A., … Woolrich, M. W. (2019). Unpacking Transient Event Dynamics in Electrophysiological Power Spectra. Brain Topography, 32(6), 1020–1034. https://doi.org/10.1007/s10548-019-00745-5

[#] Vidaurre, D., Hunt, L. T., Quinn, A. J., Hunt, B. A. E., Brookes, M. J., Nobre, A. C., & Woolrich, M. W. (2018). Spontaneous cortical activity transiently organises into frequency specific phase-coupling networks. Nature Communications, 9(1). https://doi.org/10.1038/s41467-018-05316-z

[#] The HMM-MAR toolbox: https://github.com/OHBA-analysis/HMM-MAR
