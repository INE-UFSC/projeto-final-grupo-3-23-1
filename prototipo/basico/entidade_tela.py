from abc import ABC
import pygame as pg

from basico.entidade import Entidade
from basico.desenhavel import Desenhavel

class EntidadeTela(Entidade, ABC):
    def __init__(
        self,
        tela: pg.Surface,
        pos_tela: tuple[int, int],
        dimensoes: tuple[int, int],
        desenhavel: Desenhavel
    ):
        super().__init__(tela)

        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel

        self.ativo = True

    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela, self.dimensoes)

    def getColisores(self):
        return [self]

