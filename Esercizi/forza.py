#G grafo non orientato e pesato
#grafo sociale dove i nodi sono gli utenti e gli archi sono relazioni di amcizia
#il peso dell'arco rappresenta la forza dell'amicizia
#Implementare il metodo forza che dato un grafo e due valori k e h restituisce gli ID degli utenti
#che hanno almeno k amici collegati da archi di peso maggiore o uguale ad h

def forza(g , k , h):
    r = []
    n = g.n
    for i in range(n):
        amici = 0
        for a in g.getAdiacenza(i):
            if a.peso > 0 and a.peso >= h:
                amici += 1
            if amici >= k:
                r.append(i)
    return r

#Complessita del metodo:

#(Matrice di adiacenza)(m archi e n nodi)
#CTP(m , n)= CTM perchè devo comunque scorrere tutta la matrice di adiacenza e quindi costo n^2 con n numero nodi grafo
#CSP(m , n)= tutti hanno almeno k amici con peso maggiore di h e quindi ricopio tutti i nodi tetha di n (sempre con matrice)
#CSM(m , n)= nessuno ha almeno k amici con peso maggiore di h e quindi tetha di 1

#(Lista di adiacenza)
#CTP(m , n)= come con la matrice di adiacenza
#CTM(m , n)= avendo già le liste mi fermo prima quindi n volte qualcosa di costante quindi tetha di n
#CSP(m , n)= idem come sopra
#CSM(m , n)= idem come sopra
