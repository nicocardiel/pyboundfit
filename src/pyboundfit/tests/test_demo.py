# -*- coding: utf-8 -*-
#
# Copyright 2025 Universidad Complutense de Madrid
#
# This file is part of pyboundfit
#
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSE.txt
#

import numpy as np

from pyboundfit import demo


def test_demo():
    pol1, pol2, spl1, spl2 = demo(plot=False, verbose=True)

    expected_pol1_coef = np.array([ 23.93468048,  -27.52145834,   10.30357372,   84.12092668,
         24.85352908, -107.79404231])
    expected_pol2_coef = np.array([-14.69901638,   2.20001633, -17.30738398, -10.6696552 ,
        44.38035865,  -7.86880031])
    expected_spl1_coef = np.array([110.47799613,  96.80612414,  19.94504818,  20.28181379,
        46.81825405,   7.48641351,  34.75069227,  10.60370557,
        27.02194325, -12.40047641,  34.37791295,  10.57481962,
       -14.71985266,   7.90673587])
    expected_spl2_coef = np.array([ 70.26052494,  24.51305661, -10.10028048,   4.33798346,
         1.06037889, -32.55073887,  13.72561232, -18.88227289,
        -8.61413322, -25.84615834,  -2.93643262,  -6.20214418,
        -2.61719883, -14.17871978])

    assert np.all(np.isclose(pol1.coef, expected_pol1_coef))
    assert np.all(np.isclose(pol2.coef, expected_pol2_coef))
    assert np.all(np.isclose(spl1.get_coeffs(), expected_spl1_coef))
    assert np.all(np.isclose(spl2.get_coeffs(), expected_spl2_coef))
