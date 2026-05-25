class Knapsack:
    def __init__(self):
        pass

    def calcola(i:list , v:list, w:int):
        n = len(i)
        m = []
        for _ in range(n+1):
            r = []
            for _ in range(w+1):
                r.append(0)
            m.append(r)

        for W in range(1 , w+1):
            for k in range(1, n+1):
                m[k][W] = max((m[k-1][W] if i[k-1]>W else 0) , m[k-1][W] , m[k-1][W-i[k-1]]+v[k-1])
        return m

    def riempiZaino(i:list , v:list , w:int):
        m = Knapsack.calcola(i , v , w)
        z = []
        k = len(i)
        j = w
        while k > 0 and j > 0:
            f = m[k][j]
            if f > m[k-1][j-i[k-1]]: #Torniamo indietro seguento il contrario della max del calcola
                z.append(k-1)
                j -= i[k-1]
                k -= 1
            else:
                k -= 1
        z.reverse()
        return z
    
    def maxVantaggio(i:list, v:list, w:int):
        m = Knapsack.calcola(i,v,w)
        return m[len(i)][w]


if __name__ == "__main__":
    i = [1, 4, 5, 3, 6]
    v = [9, 4, 1, 8, 5]
    w = 12
    print("Massimo vantaggio: " + str(Knapsack.maxVantaggio(i, v, w)))
    m = Knapsack.calcola(i, v, w)
    for riga in m:
        print(riga)
    print(Knapsack.riempiZaino(i, v, w))