import numpy as np

class Ramo():
    def __init__(self, x, y, peso):
        self.x = x
        self.y = y
        self.peso = peso

class Grafo():
    def __init__(self, maxN = 256):
        self._maxN = maxN
        self._m = np.zeros((self._maxN, self._maxN))
        self._nodi = []
        self._rami = []
        self.n = 0
        self.m = 0

    def inserisciNodo(self, info, index:int, peso:int):#index indice nodo a cui collegarlo
        self._nodi.append(info)
        if peso == 0: raise ValueError("Peso nullo non valido")
        r = Ramo(info, self._nodi[index], peso)
        self._rami.append(r)
        self.m += 1; self.n += 1
        self._m[self.n - 1][index] = peso

    def collegaDueNodi(self, x:int, y:int, peso:int):#Bisogna dare gli indici della lista nodi
        r = Ramo(self._nodi[x], self._nodi[y], peso)
        self._m[x][y] = peso
        self._rami.append(r)

    def __iter__(self):
        pass#return Iter(self._m) #Da fare

    def getAdiacenza(self, index:int):
        ad = []
        for j in range(self.n):
            if self._m[index][j] != 0: #Considero che gli archi possono essere negativi e sono nulli se pari a zero
                ad.append(j)
        return ad

    def getIndex(self, nodo):
        i = 0
        for n in self._nodi:
            if n == nodo: return i
            i += 1
        return -1

    def getNodo(self, index:int):
        return self._nodi[index]

    def getPeso(self, x:int, y:int):
        return self._m[x][y]

    def getPesoNodo(self, xNodo:int, yNodo:int):
        x = -1 ; y = -1
        for i in range(self.n):
            if self._nodi[i] == xNodo:
                x = i
            elif self._nodi[i] == yNodo:
                y = i
        if x == -1 or y == -1:
            return 0
        return self._m[x][y]

    