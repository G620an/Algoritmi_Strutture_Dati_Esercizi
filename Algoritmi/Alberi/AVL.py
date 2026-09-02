class Nodo:
    def __init__(self, info=None, key=None, dx=None, sx=None, gen=None):
        self.info = None
        self.key: Nodo = None
        self.dx: Nodo = None
        self.sx: Nodo = None
        self.gen: Nodo = None
        self.h: int = 0

class AVL:
    def __init__(self):
        self._radice = None
        self._n = 0

    def inserisci(self, info, key):
        nodo = Nodo(info=info, key=key)
        if self._radice is None:
            self._radice = nodo
            self._radice.h = 1
            self._n += 1
            return
        self.posiziona(nodo, self._radice)



    def posiziona(self, nodo, pos)->Nodo:
        if nodo.key <= pos.key and pos.sx is None:
            pos.sx = nodo
            nodo.h = 1 + pos.h
            return pos
        elif nodo.key >= pos.key and pos.sx is not None:
            return self.posiziona(nodo, pos.sx)

        if nodo.key > pos.key and pos.dx is None:
            pos.dx = nodo
            nodo.h = 1 + pos.h
            return pos
        elif nodo.key > pos.key and pos.sx is not None:
            return self.posiziona(nodo, pos.dx)
        else:
            return Nodo()

    def sonoDestro(self, nodo):
        return nodo.gen.dx == nodo

    def sxsx(self, nodo):
        old = Nodo(info = nodo.info, key = nodo.key)
        




    def dxdx(self, nodo):
        pass

    def sxdx(self, nodo):
        pass

    def dxsx(self, nodo):
        pass

    def insBilancia(self, nodo:Nodo, confronto:Nodo):
        if abs(nodo.sx.h - nodo.dx.h) <= 1:
            if nodo.key <= confronto.key:
                self.insBilancia(nodo.sx, confronto)
            else:
                self.insBilancia(nodo.dx, confronto)
        else:
            ant = nodo.gen.gen
            if ant.sx.sx == nodo:
                self.sxsx(ant)
            elif ant.sx.dx == nodo:
                self.sxdx(ant)
            elif ant.dx.sx == nodo:
                self.dxsx(ant)
            elif ant.dx.dx == nodo:
                self.dxdx(ant)



