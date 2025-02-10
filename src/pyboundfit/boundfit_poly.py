#
# Copyright 2025 Universidad Complutense de Madrid
#
# This file is part of pyboundfit
#
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSE.txt
#

import numpy as np
from numpy.polynomial import Polynomial


def boundfit_poly(
        x, y, deg, boundary='upper',
        xi=100, niter=100,
        return_all_fits=False
):
    if boundary not in ['upper', 'lower']:
        raise SystemExit(f'Invalid boundary: {boundary}')
    flag = {'upper': 1, 'lower': -1}
    # initial fit
    poly = Polynomial.fit(x=x, y=y, deg=deg)
    if return_all_fits:
        list_all_fits = [poly]
    else:
        list_all_fits = None
    # iterate to compute upper boundary
    residuals_previous = None
    for i in range(niter):
        residuals = y - poly(x)
        sign = np.sign(residuals).astype(int)
        w = np.ones_like(x)
        w[sign==flag[boundary]] = xi
        w[sign==0] = xi
        poly = Polynomial.fit(x=x, y=y, deg=deg, w=w)
        if return_all_fits:
            list_all_fits.append(poly)
        if i == 0:
            residuals_previous = residuals
        else:
            if np.all(np.isclose(residuals, residuals_previous)):
                break
            else:
                residuals_previous = residuals
    if return_all_fits:
        return poly, list_all_fits
    else:
        return poly
