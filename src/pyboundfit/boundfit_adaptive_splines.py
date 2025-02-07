#
# Copyright 2025 Universidad Complutense de Madrid
#
# This file is part of pyboundfit
#
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSE.txt
#

"""Compute boundary using adaptive splines"""

import numpy as np
from .numsplines import AdaptiveLSQUnivariateSpline


def boundfit_adaptive_splines(x, y, t, boundary='upper', xi=100, niter=20):
    if boundary not in ['upper', 'lower']:
        raise SystemExit(f'Invalid boundary: {boundary}')
    flag = {'upper': 1, 'lower': -1}
    # the x data must be sorted
    isort = np.argsort(x)
    x = x[isort]
    y = y[isort]
    # initial fit
    spl = AdaptiveLSQUnivariateSpline(x=x, y=y, t=t)
    # iterate to compute upper boundary
    for i in range(niter):
        residuals = y - spl(x)
        sign = np.sign(residuals).astype(int)
        w = np.ones_like(x)
        w[sign==flag[boundary]] = xi
        w[sign==0] = xi
        spl = AdaptiveLSQUnivariateSpline(x=x, y=y, w=w, t=t)
    return spl
