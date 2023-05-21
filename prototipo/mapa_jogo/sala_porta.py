from abc import ABC, abstractmethod
from sala import Sala
from porta import Porta
from basico.entidadeTela import EntidadeTela, DesenhavelRetangulo

class SalaPorta(EntidadeTela, ABC):
    def __init__(self, sala: Sala, porta: Porta, pos_tela, dimensoes):
        desenhavel = DesenhavelRetangulo((150, 75, 0))
        super().__init__(sala.desenho, pos_tela, dimensoes, desenhavel)
        self.__sala = sala
        self.__porta = porta
    
    def atualizar(self):
        pass #fazer!!
    

class SalaPortaBaixo(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        pos_tela = (550, 0)
        dimensoes = (200, 100)
        super().__init__(self, sala, porta, pos_tela, dimensoes)


class SalaPortaCima(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        pos_tela = (550, 600)
        dimensoes = (200, 100)
        super().__init__(self, sala, porta, pos_tela, dimensoes)

class SalaPortaDireita(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta):
        pos_tela = (1200, 250)
        dimensoes = (100, 200)
        super().__init__(self, sala, porta, pos_tela, dimensoes)

class SalaPortaEsquerda(SalaPorta):
    def __init__(self, sala: Sala, porta: Porta, pos_tela, dimensoes):
        pos_tela = (000, 250)
        dimensoes = (100, 200)
        super().__init__(self, sala, porta, pos_tela, dimensoes)