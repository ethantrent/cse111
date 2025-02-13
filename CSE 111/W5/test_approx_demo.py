import pytest
from pytest import approx
from approx_demo import final_value

def test_final_value():
    p = 100
    r = 0.08
    n = 12
    t = 9
    a = final_value(p, r, n, t)
    assert a == approx(204.95, abs=0.005)

pytest.main(["-v", "--tb=line", "-rN", __file__])