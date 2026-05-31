#Grafo non orientato
#Ogni nodo ha un tipo P o B (B=Blocco e P=Piscina)
#Il metodo vuole restituire per ogni blocco di tipo B la lista delle 3 piscine più vicine



def piscineVicine(G:Grafo):
    M = floyd.calcola(G)
    piscine = []*G.n
    for i in range(G.n):
        vicini = [float('sup')]*3
        if G.etichetta(i) == 'B': #ipotizzo questo metodo
            for j in range(G.n):
                d = M[i][j] 
                m = -1
                for k in range(3):
                    if d < vicini[k]:
                        m = k
                if m != -1 : vicini[m] = d
            vicini.sort()
            piscine[i].append(vicini)
    return piscine
    
#Complessità (matrice di adiacenza)
#CTP(m,n) == CTM(m,n) = la complessità è sovrastata dal calcolo di Floyd n^3
#CSM(m,n) == CSP(m,n) = il costo di avere la matrice di Floyd cioè n^2
