from ..BSplineModel import BSplineModel
import numpy as np
import pytest

# these tests fail with old version of astropy
# TODO: skip the tests if astropy 0.3.x is being used
def test_init():
    pytest.importorskip("scipy")
    knots = [0., 0., 0., 0., 2.22222222, 3.33333333, 4.44444444, 5.55555556,
             6.66666667, 7.77777778, 10., 10., 10., 10.]
    coefficients = [ -4.94881722e-18,   8.96543619e-01,   1.39407154e+00,
                    -2.36640266e-01,  -1.18324030e+00,  -8.16301228e-01,
                    4.57836125e-01,   1.48720677e+00,   1.64338775e-01,
                    -5.44021111e-01,   0.00000000e+00,   0.00000000e+00,
                    0.00000000e+00,   0.00000000e+00]
    degree = 3
    bs = BSplineModel(degree, knots, coefficients)
    x = np.linspace(0, 10, 100)
    y = [-4.94881722e-18,   1.18735992e-01,   2.30357004e-01,
        3.34750430e-01,   4.31803667e-01,   5.21404108e-01,
        6.03439149e-01,   6.77796187e-01,   7.44362616e-01,
        8.03025831e-01,   8.53673227e-01,   8.96192201e-01,
        9.30470147e-01,   9.56394461e-01,   9.73852538e-01,
        9.82731773e-01,   9.82919561e-01,   9.74303299e-01,
        9.56770381e-01,   9.30208202e-01,   8.94504159e-01,
        8.49545645e-01,   7.95220057e-01,   7.31611804e-01,
        6.59593349e-01,   5.80234170e-01,   4.94603746e-01,
        4.03771554e-01,   3.08807073e-01,   2.10779778e-01,
        1.10759150e-01,   9.81466515e-03,  -9.09841984e-02,
       -1.90567963e-01,  -2.87915531e-01,  -3.82199330e-01,
       -4.72640167e-01,  -5.58458849e-01,  -6.38876183e-01,
       -7.13112978e-01,  -7.80390041e-01,  -8.39928179e-01,
       -8.90948199e-01,  -9.32670909e-01,  -9.64317117e-01,
       -9.85288377e-01,  -9.95709231e-01,  -9.95884970e-01,
       -9.86120884e-01,  -9.66722262e-01,  -9.37994394e-01,
       -9.00242570e-01,  -8.53772081e-01,  -7.98888215e-01,
       -7.35896263e-01,  -6.65101515e-01,  -5.86934851e-01,
       -5.02329514e-01,  -4.12344338e-01,  -3.18038157e-01,
       -2.20469805e-01,  -1.20698114e-01,  -1.97819186e-02,
        8.12199470e-02,   1.81248650e-01,   2.79245355e-01,
        3.74151231e-01,   4.64971907e-01,   5.50970877e-01,
        6.31476099e-01,   7.05815530e-01,   7.73317130e-01,
        8.33308854e-01,   8.85118663e-01,   9.28074513e-01,
        9.61504362e-01,   9.84736169e-01,   9.97097891e-01,
        9.98133233e-01,   9.88248885e-01,   9.68067282e-01,
        9.38210862e-01,   8.99302061e-01,   8.51963314e-01,
        7.96817059e-01,   7.34485732e-01,   6.65591768e-01,
        5.90757605e-01,   5.10605678e-01,   4.25758425e-01,
        3.36838280e-01,   2.44467681e-01,   1.49269064e-01,
        5.18648655e-02,  -4.71224788e-02,  -1.47070532e-01,
       -2.47356858e-01,  -3.47359021e-01,  -4.46454584e-01,
       -5.44021111e-01]

    np.testing.assert_allclose(y, bs(x), rtol=1.e-4)

def test_from_data():
    pytest.importorskip("scipy")
    x1 = np.linspace(0, 10, 10)
    y1 = np.sin(x1)
    bs = BSplineModel.from_data(x1, y1, 3)
    x2 = np.linspace(0, 10, 100)
    y2 = [-4.94881722e-18,   1.18735992e-01,   2.30357004e-01,
        3.34750430e-01,   4.31803667e-01,   5.21404108e-01,
        6.03439149e-01,   6.77796187e-01,   7.44362616e-01,
        8.03025831e-01,   8.53673227e-01,   8.96192201e-01,
        9.30470147e-01,   9.56394461e-01,   9.73852538e-01,
        9.82731773e-01,   9.82919561e-01,   9.74303299e-01,
        9.56770381e-01,   9.30208202e-01,   8.94504159e-01,
        8.49545645e-01,   7.95220057e-01,   7.31611804e-01,
        6.59593349e-01,   5.80234170e-01,   4.94603746e-01,
        4.03771554e-01,   3.08807073e-01,   2.10779778e-01,
        1.10759150e-01,   9.81466515e-03,  -9.09841984e-02,
       -1.90567963e-01,  -2.87915531e-01,  -3.82199330e-01,
       -4.72640167e-01,  -5.58458849e-01,  -6.38876183e-01,
       -7.13112978e-01,  -7.80390041e-01,  -8.39928179e-01,
       -8.90948199e-01,  -9.32670909e-01,  -9.64317117e-01,
       -9.85288377e-01,  -9.95709231e-01,  -9.95884970e-01,
       -9.86120884e-01,  -9.66722262e-01,  -9.37994394e-01,
       -9.00242570e-01,  -8.53772081e-01,  -7.98888215e-01,
       -7.35896263e-01,  -6.65101515e-01,  -5.86934851e-01,
       -5.02329514e-01,  -4.12344338e-01,  -3.18038157e-01,
       -2.20469805e-01,  -1.20698114e-01,  -1.97819186e-02,
        8.12199470e-02,   1.81248650e-01,   2.79245355e-01,
        3.74151231e-01,   4.64971907e-01,   5.50970877e-01,
        6.31476099e-01,   7.05815530e-01,   7.73317130e-01,
        8.33308854e-01,   8.85118663e-01,   9.28074513e-01,
        9.61504362e-01,   9.84736169e-01,   9.97097891e-01,
        9.98133233e-01,   9.88248885e-01,   9.68067282e-01,
        9.38210862e-01,   8.99302061e-01,   8.51963314e-01,
        7.96817059e-01,   7.34485732e-01,   6.65591768e-01,
        5.90757605e-01,   5.10605678e-01,   4.25758425e-01,
        3.36838280e-01,   2.44467681e-01,   1.49269064e-01,
        5.18648655e-02,  -4.71224788e-02,  -1.47070532e-01,
       -2.47356858e-01,  -3.47359021e-01,  -4.46454584e-01,
       -5.44021111e-01]

    np.testing.assert_allclose(y2, bs(x2), rtol=1.e-4)

