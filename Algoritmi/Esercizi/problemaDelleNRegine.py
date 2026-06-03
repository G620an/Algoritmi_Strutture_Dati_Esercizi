from Backtracking.Backtracking import  Backtracking
from Grafo.Grafo import Grafo
from Grafo.GeneraGrafo import GeneraGrafo
import numpy as np

#Data una scacchiera dobbiamo trovare la combinazione di N regine per cui non si mangiano tra loro

class ProblemaDelleNRegine(Backtracking):
    def __init__(self, n = 0, x = 32):
        super().__init__()
        self.n = n
        self.x = x
        if n >= x:
            raise ValueError("Il numero di regine deve essere inferiore al numero di righe/colonne della scacchiera")
        self.scelte = [0]*n #Posizione di ogni singola regina nella propria riga singola

    def primaScelta(self, l):
        if l >= self.n: return False
        if self.scelte[l] >= self.x:
            return False
        self.scelte[l] = 0
        return True

    def successivaScelta(self, l):
        if l >= self.n: return False
        if self.scelte[l] + 1 >= self.x:
            return False
        self.scelte[l] += 1
        return True

    def verificaVincoli(self, l):
        for i in range(self.n):
            distanza = abs(i - l)
            if i != l:
                if self.scelte[i] == self.scelte[l]: #Controllo colonna
                    return False
                if abs(self.scelte[i] - self.scelte[l]) == distanza: #controllo diagonale
                    return False
        return True

    def soluzioneCompleta(self, l):
        if self.n == l+1: return True
        return False

    def costruisciSoluzione(self, l):
        self.sc = []
        for k in range(self.x): self.sc.append([0]*self.x)
        print("Risolto: ")
        for i in range(self.n):
            self.sc[i][self.scelte[i]] = 1

    def calcola(self):
        b = self.risolvi()
        return self.sc


if __name__ == "__main__":
    p = ProblemaDelleNRegine(7 , 24)
    sc = p.calcola()
    if sc is not None:
        for r in sc:
            print(r)

