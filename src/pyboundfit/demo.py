# -*- coding: utf-8 -*-
#
# Copyright 2025 Universidad Complutense de Madrid
#
# This file is part of pyboundfit
#
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSE.txt
#

import matplotlib.pyplot as plt
import numpy as np

from pyboundfit import boundfit_adaptive_splines, boundfit_poly


def __demofun(xtest, ytest, plot=False, verbose=True):
    if verbose:
        print('Computing upper boundary (polynomial fit)... ', end='')
    poly1 = boundfit_poly(x=xtest, y=ytest, deg=5, boundary='upper')
    if verbose:
        print('OK!\nComputing lower boundary (polynomial fit)... ', end='')
    poly2 = boundfit_poly(x=xtest, y=ytest, deg=5, boundary='lower')
    if verbose:
        print('OK!\nComputing upper boundary (splines fit)... ', end='')
    spl1 = boundfit_adaptive_splines(x=xtest, y=ytest, t=10, boundary='upper', xi=100, niter=40)
    if verbose:
        print('OK!\nComputing lower boundary (splines fit)... ', end='')
    spl2 = boundfit_adaptive_splines(x=xtest, y=ytest, t=10, boundary='lower', xi=100, niter=40)
    if verbose:
        print('OK!')

    if plot:
        xmin = np.min(xtest)
        xmax = np.max(xtest)
        xplot = np.linspace(xmin, xmax, 1000)

        fig, ax = plt.subplots()
        ax.plot(xtest, ytest, 'ko', markersize=5, label='original data')
        ax.plot(xplot, poly1(xplot), 'b-', label='polynomial fit')

        ax.plot(xplot, poly2(xplot), 'b-')

        ax.plot(xplot, spl1(xplot), 'r:', label='spline fit')
        xknots = spl1.get_knots()
        yknots = spl1(xknots)
        ax.plot(xknots, yknots, 'g.', markersize=5, label='knot location')

        ax.plot(xplot, spl2(xplot), 'r:')
        xknots = spl2.get_knots()
        yknots = spl2(xknots)
        ax.plot(xknots, yknots, 'g.', markersize=5)

        ax.fill_between(xplot, spl1(xplot), spl2(xplot), facecolor='grey', alpha=0.5)

        ax.set_xlabel('X axis (arbitrary units)')
        ax.set_ylabel('Y axis (arbitrary units)')
        ax.legend()

        plt.tight_layout()
        plt.show()

    return poly1, poly2, spl1, spl2
