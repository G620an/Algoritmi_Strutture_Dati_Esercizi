#Stato -> sol[i] = True se elemento[i] è contenuto nella soluzione parziale
#livello -> elemento con cui lavoro
#Dominio -> True o False se prendere o non prendere un elemento
#Vincolo parziale -> Somma <= K 
#Soluzione completa -> Somma era uguale a K

class SubsetSum(Backtracking):
    def __init__(self):
        pass
    #Bisogna implementare i metodi che non ci sono nella classe Backtracking