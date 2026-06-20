#Union Find ottimizzata per le find
from copy import deepcopy
class Nodo:
    def __init__(self, info):
        self.info = info
        self.dx = None
        self.sx = None
        self.h = 1

    def __str__(self):

        return "(" + str(self.info) + ", " +str(self.h) + ")"

class UFF:
    def __init__(self):
        self._n = 0
        self._set = {}
        self._genitori = {}


    def makeSet(self, x):
        n = Nodo(x)
        self._set[x] = n
        self._genitori[x] = x
        self._n += 1

    def find(self, x):
        return self._genitori[x]

    def union(self, x, y):
        if self.find(x) == self.find(y):
            return
        xn = self._set[x]
        yn = self._set[y]
        hy = yn.h
        hx = xn.h
        if xn.h >= yn.h:
            self._inserisci(xn, yn)
            self._set[x].h += hy
            self._set[y] = None
        else:
            self._inserisci(yn, xn)
            self._set[x] = yn
            self._set[x].h += hx
            self._set[y] = None
        self._genitori[y] = self._genitori[x]
        self._n -= 1
        return self._set[x]


    def _inserisci(self, xn, yn):
        if xn.dx is None:
            xn.dx = yn
            return
        if xn.sx is None:
            xn.sx = yn
            return
        cor = xn
        while cor.dx is not None:
            cor = cor.dx
        cor.dx = yn
        cor = xn
        while cor.sx is not None:
            cor = cor.sx
        cor.sx = yn


if __name__ == '__main__':
    UFF = UFF()
    UFF.makeSet("A")
    UFF.makeSet("B")
    UFF.makeSet("C")
    UFF.makeSet("D")
    print(UFF.find("A"))
    print(UFF.union("A", "B"))
    print(UFF.find("B"))
    print(UFF.union("A", "C"))
    print(UFF.find("C"))
    print(UFF.union("A", "D"))
    print(UFF.find("D"))