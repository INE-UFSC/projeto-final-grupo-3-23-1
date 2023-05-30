import pygame as pg
from pygame.locals import *

from abc import ABC, abstractmethod
from basico.entidade import Entidade
from .aparencia import Aparencia


class Sala(Entidade, ABC):
    def __init__(self, aparencia):
        self.__aparencia = aparencia
        self.__sala_portas = []

    def desenhar(self):
        for sala_porta in self.sala_portas:
            sala_porta.desenhar()
        
        self.desenhar_resto()
    
    @abstractmethod
    def desenhar_resto(self):
        pass
    
    def atualizar(self, eventos):
        for sala_porta in self.__sala_portas:
            sala_porta.atualizar(eventos)

        self.atualizar_resto(eventos)        

    @abstractmethod
    def atualizar_resto(self, eventos):
        pass

    def adicionar_sala_porta(self, sala_porta):
        self.__sala_portas.append(sala_porta)

    @property
    def desenho(self):
        return self.__desenho
    
    @property
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def sala_portas(self,):
        return self.__sala_portas


    
