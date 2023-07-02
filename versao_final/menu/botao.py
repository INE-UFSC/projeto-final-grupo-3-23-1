from basico.entidade_tela import EntidadeTela
from basico.evento import *

import pygame as pg

class Botao(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, texto, tamanho_fonte = 75/1080, fonte = "Comic Sans MS"):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)

        self.__texto = texto
        self.__fonte = pg.font.SysFont(fonte, int(tamanho_fonte * self.tela.get_height()))

        self.__apertou = False

    def atualizar(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoApertouBotaoEsquerdo):
                rect = pg.Rect((0, 0), self.dimensoes) 
                rect.center = self.pos_tela
                if rect.collidepoint(evento.pos_mouse): 
                    self.apertou = True

    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela)

        text_width, text_height = self.fonte.size(self.texto)

        self.tela.blit(self.fonte.render(self.texto, False, (51, 0, 0)),
                        (self.pos_tela[0] - text_width/2, self.pos_tela[1] - text_height/2))

    def resetApertou(self):
        self.apertou = False

    @property
    def texto(self):
        return self.__texto

    @property
    def fonte(self):
        return self.__fonte

    @property
    def apertou(self):
        return self.__apertou
    
    @apertou.setter
    def apertou(self, bool):
        self.__apertou = bool
