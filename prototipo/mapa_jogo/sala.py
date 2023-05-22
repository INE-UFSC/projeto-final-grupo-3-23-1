import pygame as pg
from pygame.locals import *

from abc import ABC, abstractmethod
from basico.entidade import Entidade
from .aparencia import Aparencia


class Sala(Entidade, ABC):
    def __init__(self, aparencia, sala_portas):
        self.__aparencia = aparencia
        self.__sala_portas = sala_portas

    def desenhar(self):
        for sala_porta in self.sala_portas:
            sala_porta.desenhar()
        
        self.desenhar_resto()
    
    @abstractmethod
    def desenhar_resto(self):
        pass
    
    def atualizar(self):
        for sala_porta in self.__sala_portas:
            sala_porta.atualizar()

        self.atualizar_resto()        

    @abstractmethod
    def atualizar_resto(self):
        pass

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

    @sala_portas.setter
    def sala_portas(self, sala_portas):
        self.__sala_portas = sala_portas
    