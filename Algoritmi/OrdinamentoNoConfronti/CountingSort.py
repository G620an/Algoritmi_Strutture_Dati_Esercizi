import numpy as np


class CountingSort():
    def __init__(self):
        pass

    def countingSort(l:list):
        minimo = min(l) #Costo tetha(n)
        massimo = max(l) #Costo tetha(n)
        m = massimo - minimo + 1
        temp = np.zeros(m)
        for el in l:
            temp[el-minimo] += 1
        l.clear()
        for i in range(len(temp)):
            c = int(temp[i])
            for k in range(c):
                l.append(minimo+i) #i = el-minimo, sommandogli minimo ottengo el
        #Costo complessivo tetha(n+m) (m dovuto allo scorrimento, m potrebbe non essere prop a n)



if __name__ == "__main__":
    l = [6, 9, 1, 3, 4, 12, -1, -32, 0, 0, 3, -3, 5]
    CountingSort.countingSort(l)
    print(l)
