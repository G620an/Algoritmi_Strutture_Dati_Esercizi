#Scrivete una funzione ricorsiva che, ricevendo il riferimento a un albero binario contenente numeri
#interi, restituisca la somma di tutti i valori pari contenuti nei nodi dell’albero.

from Alberi import *
from Alberi.AlberoBinario import AlberoBinario


def sommaPari(a:AlberoBinario):
    return s(a._radice)

def s(a):
    if a is None:
        return 0
    if a.info % 2 == 0:
        return a.info + s(a.dx) + s(a.dy)
    else:
        return s(a.dx) + s(a.dy)