from abc import ABC
from sala import Sala
from porta import Porta


class SalaPorta(ABC):
    def __init__(self, sala: Sala, porta: Porta):
        self.__sala = sala
        self.__porta = porta

class SalaPortaBaixo(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        super().__init__(self, sala, porta)

class SalaPortaCima(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        super().__init__(self, sala, porta)

class SalaPortaDireita(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        super().__init__(self, sala, porta)

class SalaPortaEsquerda(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        super().__init__(self, sala, porta)