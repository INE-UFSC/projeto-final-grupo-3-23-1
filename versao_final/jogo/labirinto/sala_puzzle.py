from .sala import Sala
from .computador import Computador

class SalaPuzzle(Sala):
    def __init__(self, tela, desenhavel, desenhavel_pc, dimen_pc, desenhavel_im_puzzle,
                 desenhavel_acertou, desenhavel_errou, resposta, jogador):
        super().__init__(tela, desenhavel)
        self.__puzzle = Computador(tela, desenhavel_pc, dimen_pc, desenhavel_im_puzzle,
                                   desenhavel_acertou, desenhavel_errou, resposta, jogador)
    
    def desenhar(self):
        super().desenhar()
        self.__puzzle.desenhar()
    
    def atualizar(self, eventos):
        super().atualizar(eventos)
        self.__puzzle.atualizar(eventos)

    def getColisores(self):
        colisores = super().getColisores()
        colisores.append(self.__puzzle)
        return colisores

    @property
    def puzzle(self):
        return self.__puzzle
