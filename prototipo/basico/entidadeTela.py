from abc import ABC
import pygame as pg

from .entidade import Entidade

class EntidadeTela(Entidade, ABC):
    def __init__(
        self,
        tela,
        pos_tela,
        dimensoes,
        desenhavel
    ):
        self.tela = tela
        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel

    def eventoColisao(self, outro):
        pass

    def colidiu(self, outro):
        self_x0 = self.pos_tela[0]
        self_x1 = self.pos_tela[0] + self.dimensoes[0]
        self_y0 = self.pos_tela[1]
        self_y1 = self.pos_tela[1] + self.dimensoes[1]

        outro_x0 = outro.pos_tela[0]
        outro_x1 = outro.pos_tela[0] + outro.dimensoes[0]
        outro_y0 = outro.pos_tela[1]
        outro_y1 = outro.pos_tela[1] + outro.dimensoes[1]

        return (self_x0 < outro_x0 < self_x1 \
                or self_x0 < outro_x1 < self_x1) \
            and (self_y0 < outro_y0 < self_y1 \
                or self_y0 < outro_y1 < self_y1)

    def desenhar(self):
        self.desenhavel.desenhar(self.tela, self.pos_tela, self.dimensoes)

class DesenhavelRetangulo:
    def __init__(self, cor):
        self.cor = cor

    def desenhar(self, tela, pos_tela, dimensoes):
        pg.draw.rect(tela, self.cor, (*pos_tela, *dimensoes))

