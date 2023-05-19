from abc import ABC
from entidade import Entidade
from aparencia.Aparencia import Aparencia

class Sala(Entidade, ABC):
    def __init__(self, aparencia: Aparencia, sala_portas: list, powerups: list):
        self.__aparencia = aparencia
        self.__sala_portas = sala_portas
        self.__powerups = powerups
