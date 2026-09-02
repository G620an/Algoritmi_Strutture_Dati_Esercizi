class Nodo:
    def __init__(self, info):
        self.info = info
        self.sx = None
        self.dx = None
        self.genitore = None

class AlberoBinario:
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
        s = None#Stack()
        s.push(self._radice)
        while len(s) > 0:
            n = s.pop()
            if n.info == value:
                return n
            s.push(n.dx)
            s.push(n.sx)
        return Nodo(None)

    def info(self):
        return self._radice.info

    def gen(self):
        return self._radice.genitore

    def dx(self):
        return AlberoBinario(self._radice.dx)
    
    def sx(self):
        return AlberoBinario(self._radice.sx)
    
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
        return True
    
    def __iter__(self):
        return Iter(self)

class Iter:
    def __init__(self, a:AlberoBinario):
        self.a = a
        if a._radice is None: raise ValueError("AlberoBinario Vuoto!")
        self.hasNext = False
        self.corrente = a._radice
        self.direzione = 0 # 0 == sinistra ; 1 == destra ; 2 == sopra 
    
    def __next__(self):
        self.posiziona()
        if not self.hasNext:
            raise StopIteration()
        else:
            self.hasNext = False
            return self.corrente

    def posiziona(self):
        while (True):
            if self.direzione == 0 and self.corrente.sx is None: #Se stai andando a sinistra e dopo non c'è più nessuno -> restituisci
                self.hasNext = True
                self.direzione = 2
                return
            elif self.direzione == 0 and self.corrente.sx is not None: #se stai andando a sinistra e ancora c'è un nodo -> prosegui a sx
                self.corrente = self.corrente.sx
            elif self.direzione == 1 and self.corrente.dx is None:#se stai andando a destra e a destra non c'è nulla -> sali
                self.direzione = 2
            elif self.direzione == 1 and self.corrente.dx is not None:#Se stai andando a destra e c'è ancora qualcosa a destra -> prova ad andare a sinistra
                self.direzione = 0 #Provo a sx
                self.corrente = self.corrente.dx
            elif self.direzione == 2 and self.corrente.genitore is None: #Sono arrivato alla radice -> mi devo fermare
                self.hasNext = False #Stop finale
                return
            elif self.direzione == 2 and self.corrente.genitore.dx == self.corrente:#Se sto andando sopra da destra -> ho finito la visita e devo salire
                self.corrente = self.corrente.genitore #Devo continuare a salire fino a che non salgo da sinistra o arrivo alla radice
            elif self.direzione == 2 and self.corrente.genitore.sx == self.corrente:#Se sto andando sopra da sinistra -> devo visitare la radice
                self.hasNext = True
                self.direzione = 1
                self.corrente = self.corrente.genitore
                return
        
           
        
