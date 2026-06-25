from operator import truediv

from Backtracking.Backtracking import Backtracking
from Grafo.Grafo import Grafo
from Grafo.GeneraGrafo import GeneraGrafo

class Cricca(Backtracking):
    def __init__(self, g:Grafo):
        super().__init__()
        self.g = g
        self.cricca = [-1]*self.g.n

    def primaScelta(self, l):
        self.cricca[l] += 1
        return True

    def successivaScelta(self, l):
        if self.cricca[l] < self.g.n-1:
            self.cricca[l]+=1
            if self.cricca.count(self.cricca[l]) > 1:
                return False
            return True
        return False

    def verificaVincoli(self, l):
        listaAd = self.g.getAdiacenza(self.cricca[l])
        for i in range(self.g.n):
            if i == l or self.cricca[i] == -1:
                continue
            if self.cricca[i] not in listaAd:
                return False
        return True

    def soluzioneCompleta(self, l):
        return False

    def costruisciSoluzione(self, l):
        pass

    def calcola(self):
        print(self.risolvi())
        return self.cricca

if __name__ == "__main__":
    g = Grafo(5)
    genera = GeneraGrafo(g, 3)
    genera.genera(5)
    cricca = Cricca(g)
    for riga in g._m:
        print(riga)
    print("------------------------------------------------------------------------------------")
    print(cricca.calcola())
