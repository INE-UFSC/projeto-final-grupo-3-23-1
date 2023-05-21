from basico.entidade import Entidade
from sala import Sala
from programa.jogo import Jogo

class MapaJogo(Entidade):
    def __init__(self, salas: list, jogo: Jogo):
        self.__salas = salas
        self.__jogo = jogo
    
    def getSala(self):
        (x, y) = self.__jogo.coord_sala_atual
        return self.__salas[x[y]]
    
    def desenhar(self):
        for sala in self.__salas:
            sala.desenhar()
    
    def atualizar(self):
        for sala in self.__salas:
            sala.atualizar()
