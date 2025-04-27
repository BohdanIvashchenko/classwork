from QuadraticEquation import QuadraticEquation

class BiQuadraticEquation(QuadraticEquation):
    def solve(self):
        res = set()
        self.show()
        r = QuadraticEquation(self.a, self.b, self.c)
        r.show()
        print(r.solve())
        for x in r.solve():
            print(x)
            if x == "inf":
                return tuple(('inf',))
            if x >= 0:
                res.add((x**0.5))
                res.add(-(x**0.5))
            return tuple(res)


