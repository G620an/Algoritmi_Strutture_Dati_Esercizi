from Alberi.AlberoBinario import AlberoBinario


def verificaUnicita(a:AlberoBinario):
    if a is None:
        return True
    if a.dx() is None and a.sx() is None:
        return verifica(a)
    return verificaUnicita(a.dx()) and verificaUnicita(a.sx())

def verifica(a:AlberoBinario, d={}):
    if d[a.info] is not None:
        d[a.info] = a
        return True
    return False

#Analisi di complessità:
#CTM(n) = theta(log(n)) l'albero è bilanciato e la condizione è subito smentita alla seconda discesa su un nodo foglia
#CTP(n) = theta(n) la condizione è verificata, quindi devo scorrere tutto l'albero
#CSM(n) = theta(log(n)) nel caso di albero bilanciato (log(n) record al più contemporaneamente)
#CSP(n) = theta(n) caso di albero degenere, n record