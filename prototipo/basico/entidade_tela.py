from abc import ABC
import pygame as pg
import math

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

    def get_distancia(self, outro):
        d = math.sqrt((self.pos_tela[0]-outro.pos_tela[0])**2 + (self.pos_tela[1] - outro.pos_tela[1])**2)
        print("meu x atual:", self.pos_tela[0])
        print("meu y atual:", self.pos_tela[1])
        print("x atual jogador:", outro.pos_tela[0])
        print("y atual jogador:", outro.pos_tela[1])
        return d

    def getRect(self):
        rect = pg.Rect((0, 0), self.dimensoes)
        rect.center = self.pos_tela
        return rect

    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela, self.dimensoes)

    def getColisores(self):
        return [self]

