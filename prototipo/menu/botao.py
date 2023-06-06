from basico.entidade_tela import EntidadeTela
from basico.evento import *

import pygame as pg

class Botao(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel

        self.apertou = False
    
    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela, self.dimensoes)

    def atualizar(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoApertouBotaoEsquerdo):
                rect = pg.Rect((0, 0), self.dimensoes) 
                rect.center = self.pos_tela
                if rect.collidepoint(evento.pos_mouse): 
                    self.apertou = True

    def resetApertou(self):
        self.apertou = False

