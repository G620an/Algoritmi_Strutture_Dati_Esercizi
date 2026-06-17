from random import Random
from Alberi.AlberoBinario import AlberoBinario
from Grafo.Grafo import Grafo
from Grafo.GeneraGrafo import GeneraGrafo

class Prim:
    def __init__(self):
        pass
    
    def calcola(g:Grafo):
        r = Random()
        n = g.n
        x = r.nextInt(n)
        A = AlberoBinario(x)
        for _ in range(n):
            min = -1
            for a in g.getAdiacenza(x):
                if a.peso < min: #per abbassare il costo di prim a nlogn devo usare un minheap
                    x = a.y
                    min = a.peso
            A.aggiungi(x)
        return A


if __name__ == '__main__':
    g = Grafo()
    gen = GeneraGrafo(g,3)
    h = gen.genera(10)
    prim = Prim().calcola(h)
    print(prim)


