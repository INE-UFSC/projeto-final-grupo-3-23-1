import pygame as pg
from pygame.locals import *

from abc import ABC, abstractmethod
from basico.entidade import Entidade
from .aparencia import Aparencia


class Sala(Entidade, ABC):
    def __init__(self, desenhavel, tela):
        super().__init__(tela)
        self.__desenhavel = desenhavel
        self.__sala_portas = []

    def getColisores(self):
        colisores = []
        colisores.extend(self.__sala_portas)

        return colisores

    def desenhar(self):
        for sala_porta in self.sala_portas:
            sala_porta.desenhar()
        
        self.desenharResto()
    
    @abstractmethod
    def desenharResto(self):
        pass
    
    def atualizar(self, eventos):
        for sala_porta in self.__sala_portas:
            sala_porta.atualizar(eventos)

        self.atualizarResto(eventos)        

    @abstractmethod
    def atualizarResto(self, eventos):
        pass

    def adicionarSalaPorta(self, sala_porta):
        from .sala_porta import SalaPorta
        if isinstance(sala_porta, SalaPorta):
            self.__sala_portas.append(sala_porta)

    @property
    def desenhavel(self):
        return self.__desenhavel
    
    @property
    def sala_portas(self,):
        return self.__sala_portas


    
