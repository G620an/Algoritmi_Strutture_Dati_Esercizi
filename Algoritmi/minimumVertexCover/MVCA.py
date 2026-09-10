#Minimum Vertex Cover Albero
from Grafo.Grafo import Grafo

global d #d mi serve averlo ovunque

def getPeso(n:int)->int:
    pass

def MVCA(a:Grafo, r):
    adiacenti = a.getAdiacenza(r)
    d = [[0, getPeso(nodo)] for nodo in range(a.n)]

    for figlio in adiacenti:
        MVCAAUX(a, figlio, r) #risolvo prima i nodi più profondi

        d[r][0] += d[figlio][1] #non prendo la radice allora sono obligato a prendere il figlio altrimenti l'arco è escluso
        d[r][1] += min(d[figlio][0], d[figlio][1]) #prendo la radice, posso scegliere se prendere o non prendere il figlio


def MVCAAUX(a:Grafo, r:int, padre:int):
    adiacenti = a.getAdiacenza(r)
    for figlio in adiacenti:
        if figlio == padre: #tra gli adiacenti di r c'è anche il genitore, non dobbiamo considerarlo
            continue

        MVCA(a, figlio) #risolvo prima i nodi più profondi

        d[r][0] += d[figlio][1] #non prendo la radice allora sono obligato a prendere il figlio altrimenti l'arco è escluso
        d[r][1] += min(d[figlio][0], d[figlio][1]) #prendo la radice, posso scegliere se prendere o non prendere il figlio