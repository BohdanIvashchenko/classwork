from numbers import Rational


class Rational:

    def __init__(self, n, d=None):
        if isinstance(n, Rational):
            self.n = n.n
            self.d = n.d
        elif isinstance(n, int) and isinstance(d, int):
            assert d != 0
            self.n = int(n)
            self.d = int(d)
        elif isinstance(n, str):
            if '/' in n:
                self.n, self.d = map(int, n.split('/'))
            else:
                self.n = int(n)
                self.d = 1
        elif isinstance(n, int) and d is None:
            self.n = int(n)
            self.d = 1

        self.reduce()

    def reduce(self):
        def evklid(a, b):
            if a % b == 0:
                return b
            else:
                return evklid(b, a % b)
        m = evklid(self.n, self.d)
        self.n //= m
        self.d //= m

    def __str__(self):
        return f'{self.n}/{self.d}'

    def __add__(self, other):
        other = Rational(other)
        return Rational(self.n * other.d + self.d * other.n, self.d * other.d)

    def __sub__(self, other):
        other = Rational(other)
        other.n *= -1
        return self + other

    def __mul__(self, other):
        other = Rational(other)
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        other = Rational(other)
        return Rational(self.n * other.d, self.d * other.n)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, item):
        if item == 'n':
            return self.n
        elif item == 'd':
            return self.d

if __name__ == '__main__':
    with open('input01.txt') as file:
        for line in file.readlines():
            tokens = line.split()
            for i, token in enumerate(tokens):
                if i == 0:
                    res = Rational(token)
                elif i - 1 == '*':
                    res = res * token
                elif i - 1 == '/':
                    res = res / token
                elif i - 1 == '+':
                    res = res + token
                elif i - 1 == '-':
                    res = res - token
            print(res)