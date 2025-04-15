class Equation:
    def __init__(self, b, c):
        self.b = b
        self.c = c
    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return 'inf'
            else:
                return tuple()
        else:
            return tuple(-self.c/self.b)

if __name__ == "__main__":
    print(Equation(0, 4).solve())