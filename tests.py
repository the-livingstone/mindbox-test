import pytest
from decimal import Decimal
from figure_area import Area

def test_circles():
    a = Area()
    assert a.calculate(0) == 0
    try:
        a.calculate(-10)
        raise ValueError
    except ValueError:
        pass
    try:
        a.calculate('ssss')
        raise ValueError
    except ValueError:
        pass
    
    assert round(a.calculate(10), 2) == round(Decimal(314.16), 2)
    assert round(a.calculate(7), 2) == round(Decimal(153.94), 2)

def test_triangles():
    a = Area()
    assert a.calculate(0,0,0) == 0
    assert a.calculate(0,0,5) == 0
    assert a.calculate(0,5,6) == 0
    try:
        a.calculate(-10,4,5)
        raise ValueError
    except ValueError:
        pass
    try:
        a.calculate(5,-10,9)
        raise ValueError
    except ValueError:
        pass
    try:
        a.calculate(5,6,50)
        raise ValueError
    except ValueError:
        pass
    try:
        a.calculate(5,'fefe',50)
        raise ValueError
    except ValueError:
        pass

    assert round(a.calculate(3,4,5), 2) == round(Decimal(6), 2)
    assert round(a.calculate(5,8,10), 2) == round(Decimal(19.81), 2)