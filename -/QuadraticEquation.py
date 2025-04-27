from Equation import Equation

class  QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def solve(self):
        if self.a == 0:
            return Equation(self.b, self.c).solve()
        else:
            d = -self.b**2 - 4*self.a*self.c
            if d > 0:
                x1 = (-self.b + d ** 0.5) / 2 / self.a
                x2 = (-self.b - d ** 0.5) / 2 / self.a
                return tuple((x1, x2))
            if d==0:
                x1 = (-self.b + d ** 0.5) / 2 / self.a
                return tuple((x1,))
            else:
                return tuple()

    def show(self):
        print(f'({self.a})x^2 + ({self.b})x + ({self.c}) = 0')

