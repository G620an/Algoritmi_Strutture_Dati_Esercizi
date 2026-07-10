import numpy

class DistanzaEditing:
    def __init__(self):
        pass

    def calcola(a:str, b:str):
        n1 = len(a)
        n2 = len(b)
        m = []
        for _ in range(n1+1):
            riga = [0]*(n2+1)
            m.append(riga)
        for j in range(1, n2+1):
            for i in range(1, n1+1):
                if a[i-1]==b[j-1] :
                    m[i][j] = m[i-1][j-1]
                else:
                    m[i][j] = 1 + min(m[i-1][j], m[i][j-1], m[i-1][j-1])
        return m[n1][n2]


if __name__ == "__main__":
    a = "mo"
    b = "la"
    print(DistanzaEditing.calcola(a, b))