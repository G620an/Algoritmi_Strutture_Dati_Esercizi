class Nodo:
    def __init__(self, info):
        self.info = info
        self.sx = None
        self.dx = None
        self.genitore = None

class Albero:
    def __init__(self , radice = None):
        self._radice = radice
        self._last = None
        self._len = 0
    
    def aggiungi(self, value):
        n = Nodo(value)
        if self._last is None:
            self._radice = n
        if self._last == self._radice:
            self._radice.sx = n
            n.genitore = self._radice
        if self._last.genitore.sx is None:
            self._last.genitore.sx = n
            n.genitore = self._last.genitore
        elif self._last.genitore.dx is None:
            self._last.genitore.dx = n
            n.genitore = self._last.genitore
        else:
            self._last.sx = n
            n.genitore = self._last
        self._last = n
        self._len += 1
    
    def cercaNodo(self, value):
        s = Stack()
        s.push(self._radice)
        while len(s) > 0:
            n = s.pop()
            if n.info == value:
                return n
            s.push(dx)
            s.push(sx)
        return Nodo(None)
    
    def rimuovi(self , value):
        n = self.cercaNodo(value)
        if n.info is None:
            return False
        if n.dx is None and n.sx is None:
            if n.genitore.dx == n:
                n.genitore.dx = None
            else:
                n.genitore.sx = None
        if n.dx is None and n.sx is not None:
            if n.genitore.dx == n:
                n.genitore.dx = n.sx
            else:
                n.genitore.sx = n.sx
        if n.dx is not None and n.sx is not None:
            x = n
            while x.dx is not None and x.sx is not None: x = x.sx
            if n.genitore.dx == n:
                n.genitore.dx = x
            else:
                n.genitore.sx = x
            self.rimuovi(x)
    

