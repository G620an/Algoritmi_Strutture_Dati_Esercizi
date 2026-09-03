from Grafo.Grafo import Grafo

'''
Progettare un algoritmo di visita in ampiezza di un grafo il
cui insieme di vertici non sia preventivamente noto e
analizzarne la complessità.
[Suggerimento : utilizzare un dizionario.]
'''

def visitaAmpezza(g:Grafo):
    visitare = [0]
    visitati = set()
    print(g.getNodo(0))

    while len(visitare) > 0:
        n = visitare.pop(0)
        visitati.add(n)
        for nodo in g.getAdiacenza(n):
            if nodo not in visitati:
                print(nodo)
                visitare.append(nodo)



