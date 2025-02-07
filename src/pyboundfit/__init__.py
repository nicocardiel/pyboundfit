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

from .boundfit_adaptive_splines import boundfit_adaptive_splines
from .boundfit_poly import boundfit_poly
from .demo import __demofun
from .numsplines import AdaptiveLSQUnivariateSpline
from .version import version

xtest = np.array([
       0.00942565, 0.01650751, 0.0094016 , 0.01338138, 0.01506783,
       0.01845347, 0.02833649, 0.02940194, 0.01532497, 0.02366032,
       0.02036319, 0.03297524, 0.03320563, 0.04905057, 0.04852699,
       0.04595793, 0.04587471, 0.07226911, 0.0496335 , 0.0676703 ,
       0.06487086, 0.07796277, 0.06547842, 0.07318176, 0.06972563,
       0.08104114, 0.07264829, 0.09757855, 0.0965408 , 0.08932587,
       0.10231739, 0.1060282 , 0.10771105, 0.10900682, 0.12378439,
       0.11900921, 0.10667756, 0.12077588, 0.10916265, 0.11852379,
       0.14367031, 0.12921771, 0.12996079, 0.14538471, 0.13763835,
       0.1474058 , 0.14080204, 0.14307827, 0.16495128, 0.1625994 ,
       0.14980865, 0.17055026, 0.17440569, 0.16401055, 0.17103064,
       0.17591271, 0.16817765, 0.18229868, 0.18065716, 0.16244984,
       0.1732468 , 0.20226192, 0.18972254, 0.18599243, 0.20005412,
       0.18760668, 0.21689622, 0.20712592, 0.21017846, 0.20853586,
       0.22419369, 0.21222205, 0.21906802, 0.22104092, 0.22767891,
       0.23383094, 0.23714833, 0.24723214, 0.22770634, 0.22945717,
       0.25291216, 0.25327426, 0.24582821, 0.22697008, 0.24326646,
       0.23102495, 0.26671305, 0.27298141, 0.25515455, 0.26789275,
       0.26593417, 0.26005024, 0.26850998, 0.28235561, 0.28954485,
       0.27586856, 0.29124242, 0.29070601, 0.3028478 , 0.29477507
])

ytest = np.array([
        1.10252080e+02,  7.67058790e+01,  7.02577440e+01,  3.75394900e+01,
        4.06922760e+01,  5.02742610e+01,  4.68600390e+01,  2.42191050e+01,
        3.84831730e+01,  3.86593590e+01,  1.47252360e+01,  2.22465080e+01,
        2.68179510e+00,  1.19595870e+01,  1.74110240e+01,  1.67201630e+01,
        2.77993240e+01,  3.66270680e+01,  2.69611110e+01,  9.21857830e-01,
        2.14220910e+00,  2.04008880e+01,  3.03882390e+01,  2.28771740e+01,
        5.01051520e+00,  2.18050420e+01,  1.30559350e+01, -6.16652490e+00,
        1.40887050e+01,  3.38419230e+01,  1.13990660e+01,  1.89891050e+01,
        1.64933110e+00,  5.09162000e+00, -3.27368160e+00,  1.23243900e+01,
        9.57353780e+00,  2.22187880e+01, -1.64201470e+01,  1.25455360e+01,
        1.17224150e+01,  7.47747560e+00,  2.36032390e+01,  1.46141660e+01,
        1.32053680e+01,  4.17725470e+00, -3.78795100e+00, -5.01650810e-01,
       -6.67838190e+00,  4.12899400e+00,  6.32251260e+00,  8.70501140e+00,
        1.25041008e-02,  1.79749300e+01, -1.54878660e+00, -9.74757290e+00,
       -7.49199390e+00,  3.22593240e+00,  1.68599830e+01,  1.71270410e+01,
       -1.39941430e+01, -1.56554410e+01,  1.92486610e+01, -1.45476250e+01,
        1.02872920e+01,  1.48250040e+01, -1.61328620e+01,  1.50461600e+00,
       -6.37848380e-01,  8.40302470e+00, -1.41977550e+00,  9.94914530e-01,
        4.00732990e-01, -2.36654900e+00,  3.89272380e+00,  6.37594700e-01,
        6.77703620e-01,  4.38211970e+00, -1.39395450e+01, -1.67813380e+01,
        2.56948930e+01,  3.28670450e+00,  1.05266490e+01, -2.69923590e+00,
       -2.72011520e-01,  9.16016480e+00,  1.00506860e+01,  8.22050090e+00,
       -4.14227680e+00,  1.06198160e+01, -5.26334190e+00,  3.96565130e+00,
       -4.83660980e+00, -3.24047990e+00, -8.56376930e+00,  1.13915780e+00,
       -7.77840040e+00, -2.23922200e+00,  7.90724750e+00, -7.62668700e+00
])

def demo(plot=True, verbose=True):
    return __demofun(xtest=xtest, ytest=ytest, plot=plot, verbose=verbose)

__version__ = version
