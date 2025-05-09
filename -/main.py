from Equation import *
from QuadraticEquation import *
from BiQuadraticEquation import *
from QuadraticEquation import QuadraticEquation

zero_roots = []
one_root =[]
two_roots = []
three_roots = []
four_roots = []
max_val = None
min_val = None
max_eq = None
min_eq = None
TESTS = ['input01.txt', 'input02.txt', 'input03.txt',]
for test in TESTS:
    with (open(test, 'r') as f):
        for line in f.readlines():
            s = list(map(int, line.split()))
            print(s)
            if len(s) == 2:
                eq = Equation(s[0], s[1])

            if  len(s) == 3:
                eq = QuadraticEquation(s[0], s[1], s[2])

            if len(s) == 5:
                eq = BiQuadraticEquation(s[0], s[2], s[4])

            res = eq.solve()

            if not res or res[0]=='inf':
                continue
            m1 = min(s)
            m2 = max(s)
            if max_val is None or m2 > max_val:
                max_val = m2
                max_eq = eq
            if min_val is None or m1 < min_val:
                min_val = m1
                min_eq = eq
            print(res)
            if len(res) == 0:
                zero_roots.append(eq)
            if len(res) == 1:
                one_root.append(eq)
            if len(res) == 2:
                two_roots.append(eq)
            if len(res) == 3:
                three_roots.append(eq)
            if len(res) == 4:
                four_roots.append(eq)


max_eq.show(), min_eq.show()
print(max_val, min_val)



