

class RadixSort:
    def __init__(self):
        pass

    def resetPrior(p:list):
        p.clear()
        for i in range(10):
            p.append([])
    def radixSort(l:list):
        prior = []
        RadixSort.resetPrior(prior)
        massimo = max(l)
        ordine = 10
        while massimo%ordine != massimo: ordine *= 10 #Calcolo il numero di cifre massimo in termini di ordini di grandezza
        ordine *= 10
        k = 10 #Faccio scorrere gli ordini di grandezza a partire dalla cifra meno significativa
        while k <= ordine:
            for el in l:
                c = el%k #Voglio ottenere la terza cifra a partire dalla meno sign. di 194312, faccio 194312 % 1000 = 312
                c = int(c/(k/10)) #Divido 312 per 100 cioè k/10 -> 312/100 = 3,12 ; alla fine prendo la parte intera cioè 3
                prior[c].append(el)
            k *= 10
            l.clear()
            for riga in prior:
                for el in riga:
                    l.append(el)
            RadixSort.resetPrior(prior)


if __name__ == '__main__':
    l = [6, 9, 1, 3, 4, 12, 0, 0, 3, 5] #Funziona solo con numeri interi positivi però è molto efficiente tetha(n*k) con k numero cifre max dell'input
    RadixSort.radixSort(l)#Quindi alla fine è un algoritmo lineare rispetto alla dimensione dell'input, abbiamo raggiunto il lower bound dell'ordinamento
    print(l)
    print("Compare:----------------------------------------------")
    print("[0, 0, 1, 3, 3, 4, 5, 6, 9, 12]")
