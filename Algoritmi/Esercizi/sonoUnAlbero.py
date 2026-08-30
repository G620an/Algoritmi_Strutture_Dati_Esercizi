from Grafo.Grafo import Grafo
import random as r

def sonoUnAlbero(g:Grafo):
    minimo = g.n == g.m + 1
    if not minimo: return False
    i = r.randint(0, g.n - 1)
    c = set()
    c.add(i)
    return visita(g, i, c) == g.n

def visita(g, n, count):
    for nodo in g.getAdiacenza(n):#Visito tutti gli adiacenti di un nodo
        if nodo not in count:#se non è già stato visitato
            count.add(nodo)#aggiungo alla visita
            visita(g, nodo, count)#visito gli adiacenti del nodo visitato
    return len(count) #restituisco il numero di nodi visitati

#Complessità con matrice di adiacenza:
#CTP(n,m) = theta(n^2) perchè nel caso peggiore, è un albero, devo scorrere tutto il grafo
#CTM(n,m) = theta(1) il grafo non è un albero

#CSP(n,m) = theta(n) perchè nel caso peggiore ho un nodo con un solo adiacente e così via così dall'avere n record
#CSM(n,m) = theta(1) perchè sono sicuro che non sia un albero ed esco subito