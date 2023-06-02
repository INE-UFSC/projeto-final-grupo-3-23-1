import pygame as pg

from abc import ABC, abstractmethod

class Desenhavel:
    def __init__(self, tela):
        self.tela = tela

    @abstractmethod
    def desenhar(self):
        pass

class DesenhavelRetangulo(Desenhavel):
    def __init__(self, tela, cor):
        super().__init__(tela)
        self.cor = cor

    def desenhar(self, pos_tela, dimensoes):
        pg.draw.rect(self.tela, self.cor, (*pos_tela, *dimensoes))

