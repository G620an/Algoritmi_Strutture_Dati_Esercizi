#G è un grafo non orientato con pesi non negativi
#k è un lista di nodi detti ancora
#Si vuole approssimare la distanza minima tra tutte le coppie di nodi
#approx(x,y) = somma(dist(x,k[i] + dist(y,k[i]))) e poi si fa la media
from Dijktra.Dijktra import Dijktra
from Grafo.Grafo import Grafo


def distanza(G,s):
    dist = [float('inf') for i in range(G.n)]
    dist[s] = 0 #distanza da se stesso
    AlberoBinario = Dijktra.calcola(G,s)
    for padre,nodo,distanza in AlberoBinario: #restituisce una terna
        dist[nodo] = distanza
    return dist

def distanzaAncore(G:Grafo, k:list): #Restituisce un dizionario
    n = len(k)
    approx = {}
    for el in k:
        distanze = distanza(G,el)
        for x in range(G.n):
            for y in range(G.n):
                if approx[(x,y)] is None:
                    approx[(x,y)] = 0
                approx[(x,y)] += distanze[x] + distanze[y]
    for e in approx:
        e /= n
    return approx


#Complessità:
#CTM(n, m, k) == CTP(n, m, k) = theta(kmlog(m)) dobbiamo comunque calcolare tutte le distanze; il costo di distanza è dominato da Dijkstra
#il costo in distanzaAncora dipende dal numero di volte in cui eseguiamo distanza, ma anche dal numero di volte che eseguiamo i for interni
#alla fine però conta l'esecuzione di distanza

#CTM(n, m, k) == CTP(n, m, k) = la struttura dati più ampia è il dizionario, con una dimensione pari a theta(n^2), visto che deve contenere
#uno spazio di valori n x n