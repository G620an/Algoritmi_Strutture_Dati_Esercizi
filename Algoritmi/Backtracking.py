#Facciamo degli esercizi sull'ultima tecnica di programmazione studiata nel corso

#Costruzione generale del backtracking

#1° scelta su un livello, restituisce la prima scelta su un livell
class Backtracking():
    def __init__(self):
        pass

    def primaScelta(self, l): #l è il livello dove ci troviamo
        pass

    def successivaScelta(self, l): #Restituisce le scelte successive
        pass

    def verificaVincoli(self, l): #Ogni volta che si prova qualcosa si verifica se non sono violati i vincoli
        #Se falso devo rivedere le mie scelte    
        pass

    def soluzioneCompleta(self, l): #Controlla se abbiamo finito
        #Se true la soluzione corrente è completa
        pass

    def costruisciSoluziones(self, l): #Costruisce la soluzione ripercorrendo il percorso delle scelte
        pass

    def risolvi(self): #Schema di risoluzione generale del backtracking
        l = 1
        rivedi = False #Se lo metto a true significa che devo tornare indietr
        if not self.primaScelta: #Non ho scelte da fare
            return False
        while l >=0:
            if self.verificaVincoli(l):
                if self.soluzioneCompleta(l):
                    self.costruisciSoluzione(l)
                    return True
                l += 1
                if not self.successivaScelta(l):
                    rivedi = True #Devo rivedere le mie scelte
            else:
                #Vincolo non più verificato
                if not self.successivaScelta(l):
                    rivedi = True
        while rivedi and l>=0:
            l -= 1
            if self.successivaScelta(l):
                rivedi = False
            return False
            

        