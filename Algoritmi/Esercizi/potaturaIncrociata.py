from Alberi.AlberoBinario import AlberoBinario

foglia = lambda nodo: (True if nodo.sx() is None and nodo.dx() is None else False)
def potaturaIncrociata(a:AlberoBinario):
    if a is None:
        return
    if a.sx().info() == a.info() and foglia(a.sx()):
        a.sx() = None
    potaturaIncrociata(a.sx())
    potaturaIncrociata(a.dx())

