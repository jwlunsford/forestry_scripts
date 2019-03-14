import numpy as np
import scipy.optimize as sp
import math


def solve_weibull(c, p1, pq, p93):
    """recover the weibull parameters.

    Args:
        c  (int)  -  the value we want to find
        p1 (real) -  the diameter of the 1st percentile
        pq (real) -  the quadratic mean diameter
        p93 (real) - the diameter of the 93rd percentile

    Returns:
        returns the formula to the calling statement.  Intended for use with the scipy optimize functions only, and not as a standalone function.
    """

    a = 0.6 * p1
    b = (p93 - a)/(-math.log(0.07)) ** (1 / c)

    return (a ** 2) + (2 * a * b * (math.gamma(1 + 1 / c))) + ((b**2) * (math.gamma(1 + 2 / c))) - (pq ** 2)


def calc_height(si, age):
    """calculate height of doms using site index ba=25 value

    Args:
        si (int)  - expected site index value for the timber stand
        age (int) - age of the timber stand in years

    Returns:
        the tree height in feet
    """
    return si * (2.14915 * (1 - math.exp(-0.025042 * age))) ** (0.755862)


def calc_percentiles(age, tpa, height):
    """calculate the diameter percentiles.

    Args:
        age (int) - age of the timber stand in years
        tpa (int) - the trees per acre (current stocking)
        height (real) - estimated or measured height of the dominant trees, which can be entered directly or calcualted via calc_height.

    Returns:
        a tuple of values representing the diameters at the first and ninty-third percentiles, as well as the quadratic mean diameter.
    """
    p1 = 2.14462 * (height ** 0.70266) * (tpa ** -0.36282) * math.exp(-1.96895 / age)
    pq = 2.14462 * (height ** 0.70266) * (tpa ** -0.25968) * math.exp(0.45967 / age)
    p93 = 2.24213 * (height ** 0.71401) * (tpa ** -0.22932) * math.exp(0.45967 / age)
    return p1, pq, p93



if __name__ == '__main__':
    initial_c_value = 3

    ht = calc_height(75, 20)
    p1, pq, p93 = calc_percentiles(15, 450, ht)

    # fsolve() finds the root of a nonlinear equation defined by func(x) = 0
    print("height = {}".format(ht))
    print("percentiles = {}, {}, {}".format(p1, pq, p93))
    print(sp.fsolve(solve_weibull, initial_c_value, args=(p1, pq, p93)))

