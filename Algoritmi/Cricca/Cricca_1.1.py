from Grafo.Grafo import Grafo
from Backtracking.Backtracking import Backtracking

class Cricca(Backtracking):
    def __init__(self, g:Grafo):
        super().__init__()
        self.g = g
        self.cr = [0]*g.n

    def primaScelta(self, lvl:int):
        self.cr[lvl] = 0
        return True

    def successivaScelta(self, lvl:int):
        if self.cr[lvl] < self.g.n:
            self.cr[lvl] += 1
            return True
        return False

    def verificaVincoli(self, lvl:int):
        for i in range(lvl): #Da vedere
            if i == lvl:
                continue
            if not self.g.esisteArco(lvl, i):
                return False
        return True

    def soluzioneCompleta(self, lvl:int):
        if not self.successivaScelta(lvl): #Da vedere
            return True
        return False

    def costruisciSoluzione(self, lvl:int):
        self.cri = self.cr[:lvl+1]

    def get(self):
       print(self.risolvi())
       return self.cri