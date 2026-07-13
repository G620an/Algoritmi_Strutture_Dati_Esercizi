#Devo verificare se esiste almeno un nodo per cui vale che tutti gli elementi nel sottoAlberoBinario sx ci sono tutti gli 
#elementi del sottoAlberoBinario dx

def esisteNodo(a):
    if a is None: return False
    if a.dx is None and a.sx is None: return False
    return compare(a.sx, a.dx) or esisteNodo(a.sx) or esisteNodo(a.dx)


def compare(sx , dx): #due alberi
    if sx is None and dx is None: return True
    if sx is None and dx is not None: return False
    if sx is not None and dx is None: return False
    return esiste(sx.info , dx) and compare(sx.sx , sx.dx) and compare(dx.sx , dx.dx)

def esiste(val , a):
    if a is None: return False
    if val == a.info:
        return True
    return esiste(val , a.sx) or esiste(val , a.dx)


#Analisi della complessità:

#CTM = n (la radice è un nodo non foglia e vale subito l'esisteNodo)

#CSM = 1 (pari ai record fatti per cercare all'interno dell'AlberoBinario per verificare subito esisteNodo) esco subito

#CTP = da fare con teorema divide et impera d=2 c=2 a=2 siamo nel caso n^d cio n^2 nel caso AlberoBinario completo dove
#non si presenta questo elemento

#CSP = solo valore a sx e degenere a dx la proprietà è verificata e sono attivi -n- record di attivazione