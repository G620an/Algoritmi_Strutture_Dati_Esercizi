#Colorare il grafo in modo tale che in nodi adiacenti non ci siano gli stessi colori
#Colori: Rosso, Blue e Verde

#livello -> Nodo da colorare
#scelte -> Colori (se ho C colori le scelte vanno da 0 a C-1)
#Vincolo -> Il colore del nodo livello deve essere diverso dai suoi adiacenti
#Soluzione -> Una lista  che va da 0->n dove per ogni valore (ID nodo) abbiamo il colore
class Coloratore(Backtrackingq):
    def __init__(self):
        colori = [R,V,B] #Rosso Verde e Blue
    
    def primaScelta(self, l):
        return 
    
    def successivaScelta(self, l):
        if G.getNodo(l+1) in G.getAdiacenza(l):
            return True
        else:
            return False
    
    def verificaVincoli(self, l):
        for nodi in G.getAdiacenza(l):
            if listaColori[l] == listaColori[n]: #Verifica se un vicino ha lo stesso colore
                return False
        return True

    
    def soluzioneCompleta(self, l):
        pass
    
    def costruisciSoluziones(self, l):
        return
    
    def coloraGrafo(G):
        listaColori = ['B']*G.n
                