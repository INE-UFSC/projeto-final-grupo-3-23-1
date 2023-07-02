from basico.entidade import Entidade
from .sala import Sala

class MapaJogo(Entidade):
    def __init__(self, salas: list, portas: list):
        self.__salas = salas
        self.__portas = portas
    
    def getSala(self):
        (x, y) = self.__jogo.coord_sala_atual
        return self.__salas[x[y]]
    
    def desenhar(self):
        for linha in self.__salas:
            for sala in linha:
                sala.desenhar()
    
    def atualizar(self, eventos):
        for linha in self.__salas:
            for sala in linha:
                sala.atualizar(eventos)
