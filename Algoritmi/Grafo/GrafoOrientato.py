import numpy

from Grafo.Grafo import Ramo

class GrafoOrientato:
    def __init__(self, N:int):
        self.n=0 #Numero di nodi
        self.m=0 #Numero di archi
        self._matrice = numpy.zeros((N, N)) #N è la dimensione del grafo prestabilita
        self._nodi = []
        self._archi = []

    def inserisciNodo(self, info, indexCollegamento:int, peso):
        pass

    def getNodo(self, index:int):
        return self._nodi[index]