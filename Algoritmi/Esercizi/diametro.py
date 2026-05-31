#Grafo non orientato non pesato e connesso (n = m-1)
#Restituisce la massima distanza, minima tra due nodi raggiungibili, quindi la
#lunghezza del più lungo cammino minimo tra i nodi

def diametro(G):
    mas = 0
    for nodo in G:
        #m = max(Dijktra.camminoMinimo(G, nodo), lambda(x:len(x))) #Si può fare senza Dijktra e renderlo un pò più efficiente
        if m > mas:
            mas = m
    return mas

#Complessità (matrice di adiacenza):
#CTP(m,n) == CTM(m,n) = mnlogm (devo comunque considerare tutti i nodi e quindi fare Dijktra n volte)
#CSP(m,n) === CSM(m,n) = tetha di n perchè devo solo considerare la foresta derivata dai cammini minimi del singolo nodo

#Complessità (lista di adiacenza)
#CTP(m,n) == CTM(m,n) = idem come sopra
#Idem come sopra
