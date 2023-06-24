from abc import ABC, abstractmethod
from .sala import Sala
from .porta import Porta
from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from .sala_inimigo import SalaInimigo
from .sala_puzzle import SalaPuzzle

class SalaPorta(EntidadeTela, ABC):
    @abstractmethod
    def __init__(self, tela, sala: Sala, porta: Porta, pos_tela, dimensoes):
        desenhavel = DesenhavelRetangulo(tela, (150, 75, 0), dimensoes)
        super().__init__(tela, pos_tela, dimensoes, desenhavel, solido=True, movel=False)
        self.__sala = sala
        self.__porta = porta
    
    def atualizar(self, eventos):
        if isinstance(self.__sala, SalaInimigo):
            abrir = True
            for inimigo in self.__sala.inimigos:
                if inimigo.ativo:
                    abrir = False
                    break
            if abrir:
                self.__porta.abrir()

        elif isinstance(self.__sala, SalaPuzzle):
            if self.__sala.puzzle.resolvido:
                self.__porta.abrir()
    
    @property
    def porta(self):
        return self.__porta
    
    @property
    def sala(self):
        return self.__sala
    

class SalaPortaBaixo(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (tela.get_width()/2, tela.get_height())
        dimensoes = (tela.get_height()/4, tela.get_width()/15)
        super().__init__(tela, sala, porta, pos_tela, dimensoes)


class SalaPortaCima(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (tela.get_width()/2, 0)
        dimensoes = (tela.get_height()/4, tela.get_width()/15)
        super().__init__(tela, sala, porta, pos_tela, dimensoes)

class SalaPortaDireita(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (tela.get_width(), tela.get_height()/2)
        dimensoes = (tela.get_width()/15, tela.get_height()/4)
        super().__init__(tela, sala, porta, pos_tela, dimensoes)

class SalaPortaEsquerda(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (0, tela.get_height()/2)
        dimensoes = (tela.get_width()/15, tela.get_height()/4)
        super().__init__(tela, sala, porta, pos_tela, dimensoes)
