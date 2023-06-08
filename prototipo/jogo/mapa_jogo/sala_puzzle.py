from .sala import Sala

class SalaPuzzle(Sala):
    def __init__(self, desenhavel, puzzle):
        super().__init__(desenhavel)
        self.__puzzle = puzzle
    
    def desenhar_resto(self):
        self.__puzzle.desenhar()
    
    def atualizar_resto(self, eventos):
        self.__puzzle.atualizar(eventos)

    def getColisores(self):
        colisores = super().getColisores()
        colisores.append(self.__puzzle)
        return colisores

    @property
    def puzzle(self):
        return self.__puzzle
