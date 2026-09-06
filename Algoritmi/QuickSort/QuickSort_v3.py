
def partiziona(lista, low:int, high:int):
    pivot = lista[-1]
    i = low - 1 #per avere lo spazio di inserimento
    for j in range(low, high):
        if lista[j] <= pivot:
            i += 1
            temp = lista[j]
            lista[j] = lista[i]
            lista[i] = temp

    temp = lista[i+1]
    lista[i+1] = pivot
    lista[-1] = temp
    return i + 1

def QuickSort(lista, low:int, high:int):
    while low < high:
        pivotIndex = partiziona(lista, low, high)
        if pivotIndex - low < high - low:
            QuickSort(lista[:pivotIndex], low, pivotIndex-1)
            low = pivotIndex + 1
        else:
            QuickSort(lista[pivotIndex:], pivotIndex+1, high)
            high = pivotIndex - 1



if __name__ == '__main__':
    l = [-1, 12, 0, -4, 5, 6, 98, 3, 4, 5, 1, 2, 3, -1, -9, -43]
    QuickSort(l, 0, len(l))
    print(l)