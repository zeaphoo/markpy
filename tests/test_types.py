
from markpy.types import Integer8
import pytest

def test_int8():
    i = Integer8()
    assert i.bitwidth == 8
    assert i.maxval == 127
    assert i.minval == -128
    with pytest.raises(ValueError):
        i = Integer8(128)
    i = Integer8(10) + Integer8(2)
    assert i.value == 12
    assert i == 12
    assert i < 100