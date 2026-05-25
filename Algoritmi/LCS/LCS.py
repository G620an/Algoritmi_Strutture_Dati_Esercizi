from inspect import stack

import numpy as np


class LCS:
    def __init__(self):
        pass

    def LCS(self, s1, s2):
        s1 = "_"+s1
        s2 = "_"+s2
        n = len(s1)
        m = len(s2)
        c = []
        for _ in range(n): c.append([0]*m)
        for i in range(1, n):
            for j in range(1, m):
                c[i][j] = max((c[i-1][j-1]+1 if s1[i]==s2[j] else -1), c[i-1][j], c[i][j-1])
        return (c[n-1][m-1] , c)

    def LCSSeq(self, s1, s2):
        n = len(s1)
        m = len(s2)
        l,c = self.LCS(s1, s2)
        s = []
        i = n ; j = m
        while i>0 and j>0:
            if c[i][j] > c[i-1][j-1]:
                s.append(s2[j-1]) #Prendiamo il carattere
                i -= 1 ; j -= 1
            else:
                j -= 1 #Andiamo a sx
        s.reverse()
        return s

        





if __name__=="__main__":
    s1 = "provoprovinoafarlorompere"
    s2 = "abcdefgh"
    lcs = LCS()
    l,c = lcs.LCS(s1,s2)
    for r in c:
        print(r)
    print(lcs.LCSSeq(s1,s2))
    print(l)
