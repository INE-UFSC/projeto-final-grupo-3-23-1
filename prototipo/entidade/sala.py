from abc import ABC
from Entidade import Entidade
from aparencia.Aparencia import Aparencia

class Sala(Entidade, ABC):
    def __init__(self, aparencia: Aparencia, portas: list, powerups: list):
        self.__aparencia = aparencia
        self.__portas = portas
        self.__powerups = powerups
