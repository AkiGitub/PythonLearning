import pytest
from EDXsample import convert

def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_error():
    with pytest.raises(TypeError):
        convert('10') #when we write this code

def test_float_conversion():
    assert convert(0.001) ==pytest.approx(149597870.691,abs=0.1) #tolerance or 1e-2