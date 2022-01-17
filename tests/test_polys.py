
from polys import Polynomial
def test_print():
    p=Polynomial((2,1,0,3))

    assert str(p) == "3x^3 + x + 2"


