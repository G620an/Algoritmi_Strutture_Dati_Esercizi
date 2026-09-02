from Alberi import AlberoBinario

def bilanciatoFino(n:int, a:AVL=None, i=0):
    if a is None:
        a = AlberoBinario()
    if i > n:
        return
    a.inserisci(i)
    bilanciatoFino(a, i+1)