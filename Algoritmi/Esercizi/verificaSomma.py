#restituisce true <=> se la somma dei valori contenuti nei nodi foglia di a è uguale alla somma dei nodi al livello l di a

from Alberi.Albero import Albero

def verificaSomma(a:Albero, l:int):
    if a is None:
        return True
    sl = 0; sf = 0
    somma(a, 0, l, sl, sf)
    return sl == sf

def somma(a:Albero, h:int, l:int, sl, sf):
    if a is None: return
    if h == l:
        sl += a.info
    if a.sx is None and a.dx is None:
        sf += a.info
        return
    somma(a.sx, h+1, l, sl, sf)
    somma(a.dx, h+1, l, sl, sf)

#Analisi di complessità:
    #CTP(n) == CTM(n) = Qualsiasi tipo di albero, dobbiamo scorrere tutti i nodi (nessuno sconto) tetha(n)
    #CSP(n) = Albero degenere (a sx) e quindi n record di attivazione tutti attivi sulla somma(a.sx...) tetha(n)
    #CSM(n) = Albero bilanciato e quindi al più log(n) record di attivazione attivi contemporaneamente tetha(log(n))