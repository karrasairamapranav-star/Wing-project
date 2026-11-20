"""Tests for Week 1, Evening 2. Evening 3 tests come later:
write your own first, then compare."""
import numpy as np
import pytest

from aerofoil.naca import cosine_spacing, thickness


# ---------- cosine_spacing ----------

def test_cosine_spacing_length():
    assert len(cosine_spacing(50)) == 50


def test_cosine_spacing_ends():
    x = cosine_spacing(50)
    assert x[0] == pytest.approx(0.0, abs=1e-12)
    assert x[-1] == pytest.approx(1.0, abs=1e-12)


def test_cosine_spacing_increasing():
    x = cosine_spacing(50)
    assert np.all(np.diff(x) > 0)


def test_cosine_spacing_clusters_at_ends():
    x = cosine_spacing(51)
    gaps = np.diff(x)
    middle_gap = gaps[len(gaps) // 2]
    assert gaps[0] < middle_gap
    assert gaps[-1] < middle_gap


def test_cosine_spacing_symmetric():
    x = cosine_spacing(51)
    assert np.allclose(x, 1.0 - x[::-1])


# ---------- thickness ----------

def test_thickness_zero_at_leading_edge():
    assert thickness(0.0, 0.12) == pytest.approx(0.0, abs=1e-12)


def test_thickness_closed_trailing_edge():
    assert thickness(1.0, 0.12) == pytest.approx(0.0, abs=1e-4)


def test_thickness_value_at_30_percent():
    # half-thickness of a 12% section at x = 0.3
    assert thickness(0.3, 0.12) == pytest.approx(0.0600, abs=1e-3)


def test_thickness_max_near_30_percent():
    x = np.linspace(0, 1, 2001)
    y = thickness(x, 0.12)
    assert 0.28 < x[np.argmax(y)] < 0.32


def test_thickness_scales_with_t():
    x = np.linspace(0.01, 0.99, 20)
    assert np.allclose(thickness(x, 0.24), 2 * thickness(x, 0.12))


def test_thickness_works_on_arrays():
    x = cosine_spacing(30)
    assert thickness(x, 0.12).shape == x.shape
