from copy import deepcopy

from UnionFind.UFF import UFF
from Grafo.Grafo import Grafo, Ramo
from Grafo.GeneraGrafo import GeneraGrafo

class Kruskal:
    def __init__(self):
        pass

    def calcola(g:Grafo):
        uf = UFF()
        for e in g._nodi:
            uf.makeSet(e)

        archi = deepcopy(g.getArchi())
        archi.sort()

        for ramo in archi:
            x = ramo.x
            y = ramo.y
            if uf.find(x) == uf.find(y):
                continue
            uf.union(x, y)
        return uf


if __name__ == "__main__":
    g = Grafo()
    mg = GeneraGrafo(g, 1)
    g = mg.genera(10)
    print(Kruskal.calcola(g))

