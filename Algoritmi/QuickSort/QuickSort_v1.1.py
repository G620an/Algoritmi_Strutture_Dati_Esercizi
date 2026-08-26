def QuickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        return QuickSort([el for el in lista if el < lista[len(lista)//2]]) +[el for el in lista if el == lista[len(lista)//2]]+QuickSort([el for el in lista if el > lista[len(lista)//2]])



if __name__ == '__main__':
    l = [-2, 1, 0, -3, 5, 0, -12, 5, 3, 19, -3, -21, 32]
    print(QuickSort(l))
