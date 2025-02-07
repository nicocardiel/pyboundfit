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
    expected_spl1_coef = np.array([ 70.257744  , 110.37714959,  32.06916766,  49.58457067,
        10.35319417,  19.4197963 , -22.53678477,  72.51668476,
         7.89679793])
    expected_spl2_coef = np.array([ 58.06096688,  -7.02159064,  29.50684974, -53.33382155,
        19.8011604 , -12.10226353, -26.21516219, -10.14839722,
        -7.38260503])

    assert np.all(np.isclose(pol1.coef, expected_pol1_coef))
    assert np.all(np.isclose(pol2.coef, expected_pol2_coef))
    assert np.all(np.isclose(spl1.get_coeffs(), expected_spl1_coef))
    assert np.all(np.isclose(spl2.get_coeffs(), expected_spl2_coef))
