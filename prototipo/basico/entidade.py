from abc import ABC, abstractmethod

import pygame as pg

from basico.evento import Evento

class Entidade(ABC):
    def __init__(self, tela: pg.Surface):
        self.tela = tela

    def atualizar(self, eventos: list[Evento]):
        pass

    def desenhar(self):
        pass

    def getColisores(self):
        return []

