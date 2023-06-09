from .sala import Sala
from .puzzle import Puzzle

class SalaPuzzle(Sala):
    def __init__(self, desenhavel, tela, enigma, resposta, jogador):
        super().__init__(desenhavel)
        self.__puzzle = Puzzle(tela, enigma, resposta, jogador)
    
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
