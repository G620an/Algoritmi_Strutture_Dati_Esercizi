#G è un grafo non orientato con pesi non negativi
#k è un lista di nodi detti ancora
#Si vuole approssimare la distanza minima tra tutte le coppie di nodi
#approx(x,y) = somma(dist(x,k[i] + dist(y,k[i]))) e poi si fa la media

def distanza(G,s):
    dist = [float('inf') for i in range(G.n)]
    dist[s] = 0 #distanza da se stesso
    albero = Dijkstra.calcola(G,s)
    for padre,nodo,distanza in albero: #restituisce una terna
        dist[nodo] = distanza
    return dist

def distanzaAncore(G:Grafo, k:list): #Restituisce un dizionario
    n = len(k)
    approx = [0]*G.m
    for k in K:
        distanze = distanza(G,k)
        for x in range(G.n):
            for y in range(G.n):
                approx[(x,y)] += distanze[x] + distanze[y]
    for e in approx:
        e /= n
    return approx
