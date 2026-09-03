from Grafo.Grafo import *

'''
Un pozzo in un grafo orientato G è un vertice di grado
uscente 0 e di grado entrante uguale a n-1, dove n è il
numero di vertici del grafo. Si osservi che se esiste, il pozzo
è unico. Scrivere una procedura in pseudocodice per trovare il
pozzo in G, se esiste.
'''

def trovaPozzo(g:Grafo):
    #matrice di adiacenza:
        #m[x][y] == 0 se non esiste l'arco tra due nodi x e y
        #m[x][y] == 1 se esiste l'arco ed è percorso x->y
        #m[x][y] == -1 se esiste l'arco ed è percorso y<-x
    for nodo in range(g.n):
        countIN = 0
        countOUT = 0
        for i in range(g.n):
            if g._m[nodo][i] == -1:
                countIN += 1
            elif g._m[nodo][i] == 1:
                countOUT += 1
        if countIN == g.n - 1 and countOUT == 0:
            return nodo
    return None


#CTP(n, m) = theta(n^2) perchè sono costretto a iterare su tutta la matrice e non trovare il pozzo
#CTM(n, m) = theta(n) se il primo nodo è un pozzo

#CSP(n, m) == CSM(n, m) = theta(1), in ogni caso non facciamo utilizzo di strutture dati di supporto, apparte le var che hanno costo costante
