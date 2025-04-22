from Rational import Rational


class RationalList:

    def __init__(self, *args):
        self.list = []
        for el in args:
            self.list.append(Rational(el))
        self.index = 0
        self.sort()

    def sort(self):
        self.list = sorted(self.list, key = lambda x: (x.d, x.n))

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __len__(self):
        return len(self.list)

    def __add__(self, other):
        if isinstance(other, RationalList):
            return RationalList(self.list + other.list)
        else:
            return RationalList(self.list + Rational(other))

    def __iadd__(self, other):
        RationalList(self.list + other)

    def __iter__(self):
        return self

    def __next__(self):
        item = self.list[self.index]
        self.index += 1
        if self.index >= len(self.list):
            raise StopIteration
        return item

if __name__ == '__main__':
    testlist = [21/24,  2,  -24/4,  5/7,  -12/17,  3/6,  -5,  24/15,  -16/3,  13/19,  -23,  8,  -7/4,  22/6,  9/5,  13,  -2,  -14/9,  19,  17/19,  -7/15]
    for i in RationalList(testlist):
        print(i)