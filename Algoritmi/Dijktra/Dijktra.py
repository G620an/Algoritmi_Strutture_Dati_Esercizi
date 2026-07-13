from Grafo.Grafo import Grafo
from Alberi.AlberoBinario import AlberoBinario

class Dijktra:
    def __init__(self):
        pass

    def calcola(g:Grafo, radice:int):
        if radice >= g.n or radice < 0:
            raise ValueError("Indice non valido")

        ACM = AlberoBinario(g.getNodo(radice))
        bitset = [0]*g.n
        bitset[radice] = 1

        Ns = len(g.getAdiacenza(radice))
        Ni = 0

        corrente = radice
        costoRaggiungereCorrente = 0

        while Ni != Ns:
            newCor = None
            minimo = 0
            for nodi in g.getAdiacenza(corrente):
                p = g.getPeso(corrente, nodi)
                if p <= minimo:
                    minimo = p
                    newCor = nodi

