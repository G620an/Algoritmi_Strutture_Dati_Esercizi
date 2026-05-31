#Colorare il grafo in modo tale che in nodi adiacenti non ci siano gli stessi colori
#Colori: Rosso, Blue e Verde

#livello -> Nodo da colorare
#scelte -> Colori (se ho C colori le scelte vanno da 0 a C-1)
#Vincolo -> Il colore del nodo livello deve essere diverso dai suoi adiacenti
#Soluzione -> Una lista  che va da 0->n dove per ogni valore (ID nodo) abbiamo il colore

from Backtracking import Backtracking
from Grafo.Grafo import Grafo
from Grafo.GeneraGrafo import GeneraGrafo

class Coloratore(Backtracking):
    def __init__(self, G:Grafo):
        super().__init__()
        self.colori = ['R','V','B'] #Rosso Verde e Blue
        self.G = G
        self.listaColori = ['']*G.n

    def primaScelta(self, l:int):
        self.listaColori[l] = 'R'
        return True
    
    def successivaScelta(self, l:int):
        if self.listaColori[l] == '':
            self.listaColori[l] = 'R'
            return True
        elif self.listaColori[l] == 'R':
            self.listaColori[l] = 'V'
            return True
        elif self.listaColori[l] == 'V':
            self.listaColori[l] = 'B'
            return True
        elif self.listaColori[l] == 'B':
            return False
        return False

    def verificaVincoli(self, l:int):
        for nodo in self.G.getAdiacenza(l):
            if self.listaColori[l] == '':
                continue
            if self.listaColori[l] == self.listaColori[nodo]: #Verifica se un vicino ha lo stesso colore
                return False
        return True

    def soluzioneCompleta(self, l:int):
        if l+1 == self.G.n: return True
        return False
    
    def costruisciSoluzione(self, l:int):
        return
    
    def coloraGrafo(self):
        b = self.risolvi()
        return self.listaColori, b


if __name__ == "__main__":
    n = 20 ; sup = 3
    g = Grafo(n)
    for r in g._m:
        print(r)
    print("--------------------------------------------------------------------------------")
    g = GeneraGrafo(g, sup).genera(n)
    for r in g._m:
        print(r)
    color = Coloratore(g)
    print("--------------------------------------------------------------------------------")
    l, ris = color.coloraGrafo()
    print(l)
    print(ris)


                