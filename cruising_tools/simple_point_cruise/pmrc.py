#!/usr/bin/env python
import numpy as np


''' This module contains forestry functions that will calculate stem green
    tons for loblolly pine (pinus taeda) using models provided by
    Borders, et al.
'''

def pmrc_lcp_tons(dbh, totHt, mTop=3.0):
    """Calculates the green tons (wood + bark) for loblolly pine in the
        Lower Coastal Plain region.
        Source: PMRC 1990, Univ. of Georgia, Borders et al.

        :param mTop: top merchantable diameter outside bark.
        :param totHt: total tree height.
        :param dbh: diameter outside bark at 4.5ft.
        :returns: volume in tons.        
    """
    # model parameters
    PARAM_A = 1.829983
    PARAM_B = 1.247669
    PARAM_C = 3.523107
    PARAM_D = 1.449947

    # model constants, and calculated exponents
    const1 = 0.0740959
    const2 = 0.123329
    exp1 = np.power(dbh, PARAM_A)
    exp2 = np.power(totHt, PARAM_B)
    exp3 = np.power(mTop, PARAM_C)
    exp4 = np.power(dbh, PARAM_D)

    # calculate and return green tons
    return ((const1 * exp1 * exp2) - (const2 * (exp3 / exp4) * 
        (totHt - 4.5))) / 2000


def pmrc_ucp_tons(dbh, totHt, mTop=3.0):
    """Calculates the green tons (wood + bark) for loblolly pine in the
        Upper Coastal Plain region.
        Source: PMRC 1990, Univ. of Georgia, Borders et al.

        :param mTop: top merchantable diameter outside bark.
        :param totHt: total tree height.
        :param dbh: diameter outside bark at 4.5ft.
        :returns: volume in tons.        
    """
    # model parameters
    PARAM_A = 1.917146
    PARAM_B= 1.038452
    PARAM_C = 3.589155
    PARAM_D = 1.413061

    # model constants, and calculated exponents
    const1 = 0.141534
    const2 = 0.0932063
    exp1 = np.power(dbh, PARAM_A)
    exp2 = np.power(totHt, PARAM_B)
    exp3 = np.power(mTop, PARAM_C)
    exp4 = np.power(dbh, PARAM_D)

    # calculate and return green tons
    return ((const1 * exp1 * exp2) - (const2 * (exp3 / exp4) * 
        (totHt - 4.5))) / 2000