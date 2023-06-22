import pygame as pg
from pygame.locals import *

from abc import ABC, abstractmethod
from basico.entidade import Entidade
from .aparencia import Aparencia


class Sala(Entidade, ABC):
    def __init__(self, desenhavel):
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


    
