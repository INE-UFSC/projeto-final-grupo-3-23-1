from basico.entidade import Entidade
from sala import Sala

class MapaJogo(Entidade):
    def __init__(self, salas: list):
        self.__salas = salas
    
    def getSala(self, pos_mapa: tuple):
        x = pos_mapa[0]
        y = pos_mapa[1]
        return self.__salas[x[y]]