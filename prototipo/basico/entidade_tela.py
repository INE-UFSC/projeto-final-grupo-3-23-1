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
        desenhavel: Desenhavel,
        solido: bool = False,
        movel: bool  = False
    ):
        super().__init__(tela)

        self.__pos_tela = pos_tela
        self.__dimensoes = dimensoes
        self.__desenhavel = desenhavel

        self.__ativo = True

        self.__solido = solido
        self.__movel = movel

    @property
    def pos_tela(self):
        return self.__pos_tela

    @pos_tela.setter
    def pos_tela(self, pos_tela):
        self.__pos_tela = pos_tela

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

    @property
    def desenhavel(self):
        return self.__desenhavel

    @desenhavel.setter
    def desenhavel(self, desenhavel):
        self.__desenhavel = desenhavel

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def solido(self):
        return self.__solido

    @solido.setter
    def solido(self, solido):
        self.__solido = solido

    @property
    def movel(self):
        return self.__movel

    @movel.setter
    def movel(self, movel):
        self.__movel = movel

    def get_distancia(self, entidade1, entidade2):
        d = math.sqrt((entidade1.pos_tela[0]-entidade2.pos_tela[0])**2 + (entidade1.pos_tela[1] - entidade2.pos_tela[1])**2)
        return d

    def getRect(self):
        rect = pg.Rect((0, 0), self.dimensoes)
        rect.center = self.pos_tela
        return rect

    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela)

    def getColisores(self):
        return [self]

