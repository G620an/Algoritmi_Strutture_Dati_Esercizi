import Random

class Prim:
    def __init__(self):
        pass
    
    def calcola(g):
        r = Random()
        n = g.n
        x = r.nextInt(n)
        A = Albero(x)
        for _ in range(n):
            min = -1
            for a in g.getAdiacenza(x):
                if a.peso < min: #per abbassare il costo di prim a nlogn devo usare un minheap
                    x = a.y
                    min = a.peso
            A.aggiungi(x)
        return A


