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


def boundfit_adaptive_splines(x, y, t, boundary='upper', xi=100, niter=1000, adaptive=True):
    if boundary not in ['upper', 'lower']:
        raise SystemExit(f'Invalid boundary: {boundary}')
    flag = {'upper': 1, 'lower': -1}
    # the x data must be sorted
    isort = np.argsort(x)
    x = x[isort]
    y = y[isort]
    # initial fit
    spl = AdaptiveLSQUnivariateSpline(x=x, y=y, t=t, adaptive=adaptive)
    spl.niter = 0
    # iterate to refine boundary
    t_previous = None
    residuals_previous = None
    for i in range(niter):
        t = spl.get_knots()[1:-1]  # remove first and last knot to keep the inner knots
        residuals = y - spl(x)
        sign = np.sign(residuals).astype(int)
        w = np.ones_like(x)
        w[sign==flag[boundary]] = xi
        w[sign==0] = xi
        spl = AdaptiveLSQUnivariateSpline(x=x, y=y, w=w, t=t, adaptive=adaptive)
        spl.niter = i + 1
        # stop iterations when knot location and residuals are stable
        if i == 0:
            t_previous = t
            residuals_previous = residuals
        else:
            if np.all(np.isclose(t, t_previous)) and np.all(np.isclose(residuals, residuals_previous)):
                break
            else:
                t_previous = t

    spl.xi = xi

    return spl
