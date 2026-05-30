#Colorare il grafo in modo tale che in nodi adiacenti non ci siano gli stessi colori
#Colori: Rosso, Blue e Verde

#livello -> Nodo da colorare
#scelte -> Colori (se ho C colori le scelte vanno da 0 a C-1)
#Vincolo -> Il colore del nodo livello deve essere diverso dai suoi adiacenti
#Soluzione -> Una lista  che va da 0->n dove per ogni valore (ID nodo) abbiamo il colore

from Algoritmi import Backtracking
class Coloratore(Backtracking):
    def __init__(self, G):
        self.colori = ['R','V','B'] #Rosso Verde e Blue
        self.G = G
        self.listaColori = ['B']*G.n
        self.decisioni = [False]*G.n
    def primaScelta(self, l):
        return 
    
    def successivaScelta(self, l):
        if self.G.getNodo(l+1) in self.G.getAdiacenza(l):
            return True
        else:
            return False
    
    def verificaVincoli(self, l):
        for nodi in self.G.getAdiacenza(l):
            if self.listaColori[l] == self.listaColori[nodi]: #Verifica se un vicino ha lo stesso colore
                return False
        return True

    def soluzioneCompleta(self, l):

    
    def costruisciSoluzione(self, l):
        self.decisioni[l] = True
    
    def coloraGrafo(self):
        self.risovli()
                