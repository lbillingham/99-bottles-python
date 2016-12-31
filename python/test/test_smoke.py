"""
Tests for `smoke` module.
"""
from bottles import smoke


def test_constant():
    assert smoke.CONST == 42

def test_func_return():
    assert 'return value' == smoke.func()
