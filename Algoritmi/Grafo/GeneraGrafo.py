from random import Random
from Grafo.Grafo import Grafo

class GeneraGrafo():
    def __init__(self, grafo:Grafo, sup = 0):
        self.grafo = grafo
        self.sup = sup

    def genera(self, n:int)->Grafo:
        r = Random()
        for i in range(n):
            info = r.randint(1,100)
            y = r.randint(0,i)
            peso = r.randint(1,100)
            if y == i:
                y -= 1
            self.grafo.inserisciNodo(info, y, peso)
        self.generaCollegamenti(n,r)
        return self.grafo

    def generaCollegamenti(self, n:int, r):
        for i in range(n):
            k = 0
            stop = r.randint(0,self.sup-1)
            while k < stop:
                y = r.randint(0,n-1)
                peso = r.randint(1,100)
                if i == y:
                    peso = 0
                self.grafo.collegaDueNodi(i,y,peso)
                k += 1

