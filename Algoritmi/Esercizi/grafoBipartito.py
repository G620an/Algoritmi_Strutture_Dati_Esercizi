#Un grafo non orientato G è Bipartito se l'insieme dei nodi può essere partizionato in due insiemi tali che nessun
#arco connette due nodi appartenenti alla stessa parte.
from Grafo.Grafo import Grafo


def grafoBipartito(g:Grafo):
    if g is None:
        return True
    s1 = set()
    s2 = set()
    for x in range(g.n):
        for y in range(g.n):
            if x == y:
                continue
            if g.arco(x, y):
                s1.add(y)
            else:
                s2.add(y)
    if len(s1) + len(s2) == g.n: #y deve essere aggiunto in un solo insieme, va bene che sia aggiunto infinite volte su s2
        return True #ma deve comunque scegliere un insieme
    return False

#alla fine se y è su s2 e non su s1, significa che (x,y) non esiste
#alla fine avremo due insiemi, s1 dove ci sono solo nodi adiacenti ad x per esempio e che quindi non possono stare con x
#e s2 dove ci sono nodi che possono stare con x

#Complessità:

#Matrice di adiacenza:
#CTM(n,m) == CTP(n,m) = theta(n^2) devo comunque scorrere i due for a prescindere dalla forma di g, prevedendo un set visto come hashset o bitset
#le operazioni sono theta(1)
#CSP(n,m) == CSM(n,m= = theta(n) abbiamo solo il costo di mantenere i due set, essi al più hanno 2n elementi

#Lista di adiacenza:
#considerando che g.arco(x,y) è theta(1) sia con la matrice di adiacenza che con la lista, le analisi fatte sopra valgono anche per
#questa costruzione