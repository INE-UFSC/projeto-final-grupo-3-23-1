from abc import ABC, abstractmethod
from basico.entidade import Entidade
from aparencia import Aparencia
import pygame as pg
from pygame.locals import *

class Sala(Entidade, ABC):
    def __init__(self, aparencia, sala_portas):
        self.__largura = 1300 #definir
        self.__altura = 700 #definir
        self.__desenho = pg.display.set_mode((self.__largura, self.__altura))
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
    
    @sala_portas.setter
    def sala_portas(self, sala_portas):
        self.__sala_portas = sala_portas
    