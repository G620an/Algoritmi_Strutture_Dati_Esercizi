from Grafo.Grafo import Grafo
#Sia G = (V, E) un grafo orientato, e siano x, y, z tre vertici di
#G. Stabilire se y si trova su un cammino da x verso z.


def sonoNelCammino(g:Grafo, x:int, z:int, y:int):
    cammini = Dijkstra(g, x)

