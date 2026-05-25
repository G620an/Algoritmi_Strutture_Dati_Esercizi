class Knapsack:
    def __init__(self):
        pass

    def calcola(i:list , v:list, w:int):
        n = len(i)
        for _ in range(n): m.append([0]*w)
        for W in range(w):
            k = 0
            for peso in i:
                m[peso, W] = max((m[peso-1][W] if peso>W else 0) , m[peso-1][W] , m[peso-1][W-peso]+v[k])
                k *= 1
        return m

    def riempiZaino(i:list , v:list , w:int):
        m = calcola(i , v , w)
        z = []
        k = len(i) - 1
        j = w-1 
        while k > 0 and j > 0:
            f = m[k][j]
            if m[k-1][j-i[k]]+v[k] > m[k-1][j]:
                z.append(k)
                j -= i[k]
            else:
                k -= 1
        z.reverse()
        return z
    
    def maxVantaggio(i:list, v:list, w:int):
        return calcola(i,v,w)[len(i)-1][w-1]



if __name__ == "__main__":
    i = [1, 4, 0, 3, 6]
    v = [9, 4, 1, 8, 5]
    w = 12
    print("Massimo vantaggio: " + Knapsack.maxVantaggio(i, v, w))
    print(Knapsack.calcola(i, v, w))