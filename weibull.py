import numpy as np
import scipy.optimize as sp
import math


def solve_weibull(c, p1, pq, p93):
    a = 0.6 * p1
    b = (p93 - a)/(-math.log(0.07)) ** (1 / c)

    return (a ** 2) + (2 * a * b * (math.gamma(1 + 1 / c))) + ((b**2) * (math.gamma(1 + 2 / c))) - (pq ** 2)


def calc_height(si, age):
    """calculate height of doms using site index ba=25 value"""
    return si * (2.14915 * (1 - math.exp(-0.025042 * age))) ** (0.755862)


def calc_percentiles(age, tpa, height):
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

