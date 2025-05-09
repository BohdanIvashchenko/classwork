class Equation:
    def __init__(self, b, c=None):
        if isinstance(b,Equation):
            self.b = b.b
            self.c = b.c
        else:
            self.b = b
            self.c = c
    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return tuple(('inf',))
            else:
                return tuple()
        else:
            return tuple((-self.c/self.b,))

    def show(self):
        print(f'({self.b})x + ({self.c}) = 0')

if __name__ ==  '__main__':
    test = [[0,0],[0,1],[1,0],[1,1],[2,5],[-100,0]]
    for t in test:
        print(Equation(t[0],t[1]).solve())

