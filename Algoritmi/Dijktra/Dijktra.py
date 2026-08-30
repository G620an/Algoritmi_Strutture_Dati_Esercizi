from Grafo.Grafo import Grafo
from Alberi.AlberoBinario import AlberoBinario

#Useremo un Heap modificabile per implementare dijktra, un heap modificabile detto anche heap indicizzato è un particolare min heap
#che oltre le solite operazioni permette anche un decrease_key(nodo, nuova_distanza) in log(n), cioè aggiornare la priorità di un elemento
#già presente

class Dijktra:
    def __init__(self):
        pass

    def calcola(g:Grafo, radice:int):
        if radice >= g.n or radice < 0:
            raise ValueError("Indice non valido")

        ACM = AlberoBinario(g.getNodo(radice))


