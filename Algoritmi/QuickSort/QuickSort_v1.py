from random import Random

def partiziona(v, ini:int, fin:int):
    pivot = Random().randrange(ini, fin)
    temp = v[pivot]
    v[pivot] = v[ini]
    v[ini] = temp
    inf = ini + 1
    sup = fin
    while(inf < sup):
        while(inf<=sup and v[inf]<v[ini]):
            inf += 1
        while(ini<=sup and v[ini]<=v[sup]):
            sup -= 1
        if(inf<sup):
            temp = v[inf]
            v[inf] = v[sup]
            v[sup] = temp
    temp = v[inf-1]
    v[inf-1] = v[ini]
    v[ini] = temp
    return inf-1 #Posizione di v[ini] cioè la posizione naturale del PIVOT

def sort(v, ini:int, fin:int):
    if fin-ini+1 <= 1:
        return
    else:
        p = partiziona(v , ini , fin)
        sort(v , ini , p-1)
        sort(v , p+1 , fin)


if __name__ == "__main__":
    v = [9 , 4, 2, 7, 0, -1, -11, 3, 4, 2, 8, 84, 82, 81, -8]
    #scelgo 4
    #[4,9,2,7,0] inf = 1 sup = 4
    #[4,9,2,7,0] inf = 1 e sup=4 siamo stati sfortunati
    #[4,0,2,7,9] inf = 1 sup = 4
    #[4,0,2,7,9] inf = 2 sup = 2
    #[2,0,4,7,9] già parzialmente ordinato p = 2
    #[2,0] [4] [7,9]
    #[2,0] scelgo 0 inf = 1 sup = 1
    sort(v , 0 , len(v)-1)
    print(v)



