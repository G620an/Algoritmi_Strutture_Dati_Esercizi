from QuickSort_v1 import partiziona

def sort(v, ini:int, fin:int):
    while fin > ini:
        p = partiziona(v , ini , fin)
        sort(v , ini , p-1)
        ini = p+1
        fin = fin #preparo prossima chiamata


if __name__ == "__main__":
    v = [9 , 4, 2, 7, 0, -1, -11, 3, 4, 2, 8]
    sort(v , 0 , len(v)-1)
    print(v)
