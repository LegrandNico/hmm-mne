.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
  :target: https://github.com/LegrandNico/mne-hmm/blob/master/LICENSE

----------------

HMM-MNE is a Python module implementing Hidden Markov Modeling (HMM) for electrophysiological data using the methods described in [#]_.

The HMM inference is preformed using the `hmmlearn library <https://hmmlearn.readthedocs.io/en/stable/>`_.

**Notebooks**

  -  `Introduction to HMM <https://github.com/LegrandNico/hmm-mne/blob/master/Hidden%20Markov%20Models.ipynb>`_.

  -  `Envelope threshold and HMM <https://github.com/LegrandNico/mne-hmm/blob/master/1%20-%20Envelope%20HMM.ipynb>`_.

  .. image:: https://colab.research.google.com/github/LegrandNico/mne-hmm/blob/master/notebooks/1-EnvelopeHMM.ipynb
    :target: https://colab.research.google.com/assets/colab-badge.svg

  -  `Time Delay Embedded HMM <https://github.com/LegrandNico/mne-hmm/blob/master/2%20-%20Embedded%20HMM.ipynb>`_.

  .. image:: https://colab.research.google.com/github/LegrandNico/mne-hmm/blob/master/notebooks/2-EmbeddedHMM.ipynb
    :target: https://colab.research.google.com/assets/colab-badge.svg


1- Envelope threshold and Envelope HMM
--------------------------------------

Time-course Simulation
======================

Simulation of transient high frequency events, adapted from [#]_ and [#]_.

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Simulation.png
  :align:   center

Narrow band detection
=====================

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/NarrowBand.png
  :align:   center

Wider band detection
====================

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/WiderBand.png
  :align:   center


2 - Time Delay Embedded HMM
---------------------------

TDE-HMM inference
=================

Implementation of the Time Delay Embedded HMM (TDE-HMM). Unlike the simple thresholding approach, this model embeds at each time point a lagged representation of the signal [t-n:t+n], and has then access to the whole frequency spectrum, and is able to disambiguate between burst of different frequencies.

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/tde-hmm.png
  :align:   center


State-specific power spectra
============================

The frequency content of the three states show that the model successfully discriminated between the noise, the 40 Hz and the 25 Hz burst.

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Spectral0.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Spectral1.png
  :align:   center

.. figure::  https://github.com/LegrandNico/mne-hmm/blob/master/Images/Spectral2.png
  :align:   center

Notes
-----

This repository contains Python adaptation for some of the functionalities proposed by the HMM-MAR toolbox [#]_. It was created for educational purpose. You should refer to the original Matlab toolbox is you want to use HMM for research.

References
----------

.. [#] Vidaurre, D., Hunt, L. T., Quinn, A. J., Hunt, B. A. E., Brookes, M. J., Nobre, A. C., & Woolrich, M. W. (2018). Spontaneous cortical activity transiently organises into frequency specific phase-coupling networks. Nature Communications, 9(1). https://doi.org/10.1038/s41467-018-05316-z

.. [#] Quinn, A. J., van Ede, F., Brookes, M. J., Heideman, S. G., Nowak, M., Seedat, Z. A., … Woolrich, M. W. (2019). Unpacking Transient Event Dynamics in Electrophysiological Power Spectra. Brain Topography, 32(6), 1020–1034. https://doi.org/10.1007/s10548-019-00745-5

.. [#] https://github.com/OHBA-analysis/Quinn2019_BurstHMM

.. [#] The HMM-MAR toolbox: https://github.com/OHBA-analysis/HMM-MAR
