from Backtracking import Backtracking


class Sudoku(Backtracking):
    def __init__(self, sudo):
        self.sudo = sudo
        self.n = len(sudo)
        self.scelto = []
        for x in range(self.n):
            for y in range(self.n):
                if sudo[x][y] != ".":
                    self.scelto.append((x,y))

    def primaScelta(self, lvl):
        riga = lvl//self.n
        colonna = lvl - (riga * self.n)

        if (riga, colonna) not in self.scelto:
            self.sudo[lvl] = 1
            return True
        else:
            return False

    def successivaScelta(self, lvl):
        riga = lvl//self.n
        colonna = lvl - (riga * self.n)

        if (riga, colonna) not in self.scelto:
            if self.sudo[riga][colonna] < 9:
                self.sudo[riga][colonna] += 1
            else:
                return False

        return True

    def soluzioneCompleta(self, lvl):
        riga = lvl//self.n
        colonna = lvl - (riga * self.n)
        if riga >= self.n:
            return True
        return False

    def verificaVincoli(self, lvl):
        riga = lvl//self.n
        colonna = lvl - (riga * self.n)
        x = self.sudo[riga][colonna]
        if self.sudo[riga].count(x) > 1:
            return False
        count = 0
        for el in range(1, self.n):
            if self.sudo[riga][el] == x:
                count += 1
        if count > 1:
            return False
        return True


    def costruisciSoluzione(self, lvl):
        return self.sudo

    def calcola(self):
        print(self.risolvi())
        return self.sudo


if __name__ == "__main__":
    sudo = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sudoku = Sudoku(sudo)
