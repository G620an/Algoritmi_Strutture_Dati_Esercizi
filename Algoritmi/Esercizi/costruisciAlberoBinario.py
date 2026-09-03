from Alberi.AlberoBinario import AlberoBinario

'''
Dato un array a di n elementi, progettare un algoritmo che costruisca ricorsiva-
mente in tempo O(n) un albero binario bilanciato tale che a[i] sia l’(i + 1)-esimo
campo u.dato in ordine di visita anticipata. Considerare anche gli algoritmi per le
altre visite.
'''


def costruisiAlberoBinario(lista, a: AlberoBinario = None, c = None):
    if a is None:
        a = AlberoBinario(lista.pop(0))
        c = [a]

    if len(c) > 0:
        nodo = c.pop(0)

        if len(lista) > 0:
            nodo.setSX(lista.pop(0))
            c.append(nodo.sx)
        else:
            return a

        if len(lista) > 0:
            nodo.setDX(lista.pop(0))
            c.append(nodo.dx)
        else:
            return a

        costruisiAlberoBinario(lista, a, c)

    return a
