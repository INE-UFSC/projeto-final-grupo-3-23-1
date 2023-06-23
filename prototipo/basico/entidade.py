from abc import ABC, abstractmethod

import pygame as pg

from .evento import Evento

class Entidade(ABC):
    def __init__(self, tela: pg.Surface):
        self.__tela = tela

    @property
    def tela(self):
        return self.__tela
    
    def telaW(self):
        return self.__tela.get_width()
    
    def telaH(self):
        return self.__tela.get_height()

    @tela.setter
    def tela(self, tela):
        self.__tela = tela

    def atualizar(self, eventos: list[Evento]):
        pass

    def desenhar(self):
        pass

    def getColisores(self):
        return []

