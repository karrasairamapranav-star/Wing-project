"""NACA 4-digit aerofoil generator.

Fill in each TODO yourself. Run the tests as you go:
    pytest tests/test_naca.py -v
"""
import numpy as np


def cosine_spacing(n):
    """Return n x-positions from 0 to 1 (inclusive), packed closer
    together near the leading edge (x = 0) and trailing edge (x = 1).

    Hint: space an angle evenly, then turn it into x.
    """
    # TODO (Week 1, Evening 2)
    raise NotImplementedError


def thickness(x, t):
    """Return the HALF-thickness y_t at each x (chord = 1) for a section
    whose maximum thickness is t (e.g. t = 0.12 for a NACA xx12).

    Use the closed trailing-edge version of the NACA equation,
    so thickness(1.0, t) is zero.
    x may be a single number or a numpy array.
    """
    # TODO (Week 1, Evening 2)
    raise NotImplementedError


# ---- Week 1, Evening 3: leave these until then ----

def camber_line(x, m, p):
    """Return the camber line y_c at each x. m = max camber, p = its position."""
    # TODO (Week 1, Evening 3)
    raise NotImplementedError


def camber_slope(x, m, p):
    """Return dy_c/dx at each x."""
    # TODO (Week 1, Evening 3)
    raise NotImplementedError


def naca4(code, n=100):
    """Return (xu, yu, xl, yl): upper and lower surface coordinates
    for a 4-digit code such as "4412"."""
    # TODO (Week 1, Evening 3)
    raise NotImplementedError
