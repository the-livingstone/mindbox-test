from decimal import Decimal
from math import pi, sqrt
class Area:
    def calculate(
        self,
        a: Decimal | float,
        b: Decimal | float = None,
        c: Decimal | float = None,
    ) -> Decimal:
        if isinstance(a, (int, float, Decimal)):
            if a < 0:
                raise ValueError('Cannot calcucate area with negative numbers')
        else:
            raise ValueError('Cannot calcucate area')
        if isinstance(b, (int, float, Decimal)) and isinstance(c, (int, float, Decimal)): # triangle
            if b < 0 or c < 0:
                raise ValueError('Cannot calcucate area with negative numbers')
            if isinstance(a, (int, float)):
                a = Decimal(a)
            if isinstance(b, (int, float)):
                b = Decimal(b)
            if isinstance(c, (int, float)):
                c = Decimal(c)
            if a == 0 or b == 0 or c == 0:
                return 0
            hyp = max([a, b, c])
            is_square = a**2 + b**2 + c**2 == 2 * hyp**2
            if is_square:
                return (a * b * c) / (2 * hyp)
            else:
                hp = (a + b + c) / 2
                try:
                    s = sqrt(hp * (hp - a) * (hp - b) * (hp - c))
                except ValueError:
                    raise ValueError('Triangle does not exist')
                return Decimal(s)
        elif b is None and c is None: # circle
            if isinstance(a, (int, float)):
                a = Decimal(a)
            return Decimal(pi) * a**2
        else:
            raise ValueError('Cannot calcucate area')
        
a = Area()
print(a.calculate(2, 4, 5))