from abc import ABC, abstractmethod
from basico.entidade_tela import EntidadeTela
from basico.evento import *

class Powerup(EntidadeTela, ABC):
    @abstractmethod
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, incremento):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, solido=False, movel=False)
        self.__incremento = incremento

    @property
    def incremento(self):
        return self.__incremento
    
    def atualizar(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoColisao):
                from jogo.jogador.jogador import Jogador
                if evento.possuiTipo(Jogador) and evento.possui(self):
                    self.ativo = False
    

class PowerupCadencia(Powerup):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, incremento):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, incremento)
        
class PowerupVelocidadeTiro(Powerup):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, incremento):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, incremento)
        
class PowerupDano(Powerup):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, incremento):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, incremento)
        
