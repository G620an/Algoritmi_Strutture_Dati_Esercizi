import sympy

class DizionarioHashMap:
    def __init__(self):
        self._dim = 17
        self._countElem = 0
        self._lista = [list()]*self._dim

    def __len__(self):
        return self._dim

    def rialloca(self):
        N = sympy.nextprime(self._dim)
        self._temp = [list()]*self._dim
        for i in range(self._dim):
            self._temp[i] = self._lista[i]
        self._dim = N


    def inserisci(self, k, v):
        kHash = hash(k)
        self._lista[kHash].append(v)
        self._countElem += 1
        f = self._countElem / self._dim
        if f > 0.75:
            self.rialloca()

    def elimina(self, k, v):
        kHash = hash(k)
        self._lista[kHash].remove(v)
        self._countElem -= 1

    def __get__(self, k):
        return self._lista[hash(k)]

