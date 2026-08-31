from Grafo.Grafo import Grafo
from Alberi.AlberoBinario import AlberoBinario

#Useremo un Heap modificabile per implementare dijktra, un heap modificabile detto anche heap indicizzato è un particolare min heap
#che oltre le solite operazioni permette anche un decrease_key(nodo, nuova_distanza) in log(n), cioè aggiornare la priorità di un elemento
#già presente

class Dijktra:
    def __init__(self):
        pass

    def calcola(g:Grafo, radice:int):
        if radice >= g.n or radice < 0:
            raise ValueError("Indice non valido")

        ACM = AlberoBinario(g.getNodo(radice))





def Dijkstra(g: GrafoP, source: int):#Dijktra del professore con heap modificabile
    padri: list[int] = [-1 for i in range(g.n)]
    pesi: list[int] = [sys.maxsize for i in range(g.n)]
    preso: list[bool] = [False for i in range(g.n)]
    curr: int = source
    padri[curr] = curr
    preso[curr] = True
    count = 1
    result = []
    mioheap: HeapModificabile = HeapModificabile(g.n)
    for a in g.adiacenti(curr):
        mioheap.ins(Pair(a.y, a.peso))
        padri[a.y] = curr
        pesi[a.y] = a.peso
    while not mioheap.evuoto():
        count += 1
        cp: Pair = mioheap.out()
        preso[cp.x] = True
        result.append((padri[cp.x], cp.x, cp.p))
        for a in g.adiacenti(cp.x):
            if not preso[a.y]:
                if padri[a.y] == -1:
                    mioheap.ins(Pair(a.y, a.peso + pesi[cp.x]))
                    padri[a.y] = cp.x
                    pesi[a.y] = a.peso + pesi[cp.x]
                elif pesi[a.y] > a.peso + pesi[cp.x]:
                    mioheap.update(Pair(a.y, a.peso + pesi[cp.x]))
                    padri[a.y] = cp.x
                    pesi[a.y] = a.peso + pesi[cp.x]
    return result


#padri[i]: il predecessore di i nell'albero dei cammini minimi. -1 significa "non ancora scoperto".

#pesi[i]: la distanza minima conosciuta finora da source a i (inizialmente infinito, sys.maxsize).

#preso[i]: True se i è già stato estratto definitivamente dalla heap — cioè la sua distanza è ormai finale, non cambierà più.

#mioheap: una coda a priorità (min-heap) di coppie (vertice, distanza-provvisoria), che oltre a ins/out sa fare update
#(decrease-key) in modo efficiente su un elemento già presente.


#Inizializzazione
#source viene marcato preso e reso genitore di se stesso (convenzione per riconoscere la radice). Poi tutti i suoi
#vicini diretti vengono inseriti in heap con priorità pari al peso dell'arco (che coincide con la distanza da source,
#dato che dist(source) = 0).



#Il ciclo principale

#Ad ogni iterazione:
    #cp = mioheap.out(): estrae la coppia con distanza minima.
    #Per l'invariante di Dijkstra, questa distanza è già ottima e definitiva per cp.x.
    #cp.x viene marcato preso.
    #Si aggiunge a result la tripla (padri[cp.x], cp.x, cp.p). Attenzione: cp.p non è il peso dell'ultimo arco,
    # ma la distanza cumulativa da source a cp.x — lo si vede dal fatto che viene costruita come a.peso + pesi[cp.x],
    # cioè peso-arco + distanza-già-accumulata.

    #Si scorrono i vicini a di cp.x non ancora presi:
        #se mai scoperti (padri[a.y] == -1) → si inseriscono per la prima volta in heap;
        #se già scoperti ma si trova un cammino più corto passando per cp.x (il classico relax) → si aggiorna la loro priorità con update invece
        #di reinserirli come duplicati.
        #Questo è proprio il punto in cui serve una heap "modificabile": una heap normale non permette di abbassare la priorità
        #di un elemento già presente in O(log n) senza sapere dove si trova; questa la sa ritrovare (probabilmente tramite un array
        #di posizioni interno) e la risistema.