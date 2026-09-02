from Alberi.AlberoBinario import AlberoBinario


def visitaInfissa(a:AlberoBinario):
    if a is None:
        return []
    return visitaInfissa(a.sx()) + [a.info()] + visitaInfissa(a.dx())

def visitaSuffissa(a:AlberoBinario):
    if a is None:
        return []
    return visitaSuffissa(a.sx()) + visitaSuffissa(a.dx()) + [a.info()]

def visitaPrefissa(a:AlberoBinario):
    if a is None:
        return []
    return [a.info()] + visitaPrefissa(a.sx()) + visitaPrefissa(a.dx())

def visitaAmpiezza(a:AlberoBinario, lista = None):
    if lista is None:
        lista = [a]

    if not lista.isEmpty():
        lista.append(a.sx())
        lista.append(a.dx())
        return [lista.pop(0)] + visitaAmpiezza(lista[0])

    return []

if __name__ == '__main__':
    a = AlberoBinario()
    for i in range(1, 10):
        a.aggiungi(i)
    print("Ampiezza: " + visitaAmpiezza(a))
    print("Pre: " + visitaPrefissa(a))
    print("Suf: " + visitaSuffissa(a))
    print("Inf: " + visitaInfissa(a))