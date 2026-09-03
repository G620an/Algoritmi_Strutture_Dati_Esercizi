from Grafo.Grafo import Grafo


'''
Sia G = (V, E) un grafo connesso e non orientato. Progettare
un algortimo che ricevuto in ingresso G e un suo vertice r,
restituisca il numero di vertici che si trovano a distanza
massima da r.
'''

def distanzaMassima(g:Grafo, r:int):
    risposta = set() #nodi a distanza massima
    a = [nodo for nodo in g.getAdiacenza(r)] #nodi da visitare
    visto = set() #nodi visitati
    visto.add(r)#visitato per creare a

    while len(a) > 0: #fino a che non esaurisco i nodi da visitare
        for nodo in a: #visito i nodi da visitare
            a.remove(nodo)
            visto.add(nodo) #non li considero più
            adiacenti = g.getAdiacenza(nodo) #prendo gli adiacenti

            for n in adiacenti:
                if n not in visto:
                    a.append(n)
                else:
                    adiacenti.remove(n)

            if len(adiacenti) == 0: #Se non ho nulla da visitare significa che sono abbastanza lontano
                risposta.add(nodo)
    return len(risposta)

#Non  corretto


