class Dizionario_Array:
    def __init__(self, dimMax:int):
        self._dimMax = dimMax
        self._lista = [None]*dimMax

    def getDimMax(self):
        return self._dimMax

    def inserisci(self, k:int, v):
        if k < self.getDimMax() and k >= 0:
            self._lista[k] = v
        else:
            raise ValueError("Chiave fuori range")

    def rimuovi(self, k:int):
        if k < self.getDimMax() and k >= 0:
            self._lista[k] = None
        else:
            raise ValueError("Chiave fuori range")

    def cerca(self, v):
        k = 0
        for _ in range(self._dimMax):
            if self._lista[k] == v:
                return k
            k += 1
        return -1

    def __getitem__(self, k:int):
        if k < self.getDimMax() and k >= 0:
            return self._lista[k]
        else:
            raise ValueError("Chiave fuori range")
