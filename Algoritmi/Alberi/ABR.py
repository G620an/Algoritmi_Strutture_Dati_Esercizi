from Alberi.AlberoBinario import AlberoBinario, Nodo


class ABR(AlberoBinario):
    def __init__(self, radice = None):
        super().__init__(radice)

    def aggiungi(self, value):
        n = Nodo(value)
        trovato = False
        padre = self._radice
        if padre is None:
            self._radice = n
            trovato = True
        while not trovato:
            if padre.info >= value:
                if padre.sx is None:
                    padre.sx = n
                    trovato = True
                else:
                    padre = padre.sx
            if padre.info < value:
                if padre.dx is None:
                    padre.dx = n
                    trovato = True
                else:
                    padre = padre.dx
        self._len += 1

    def cercaNodo(self, value):
        corrente = self._radice
        trovato = False
        while not trovato:
            if corrente.info == value:
                return corrente
            elif corrente.info < value:
                corrente = corrente.dx
            elif corrente.info > value:
                corrente = corrente.sx
        return Nodo(None)

