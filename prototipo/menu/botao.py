from basico.entidade_tela import EntidadeTela
from basico.evento import *

import pygame as pg

class Botao(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, texto, tamanho_fonte = 75/1080, fonte = "Comic Sans MS"):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.tela = tela
        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel
        self.texto = texto

        self.apertou = False
    
        self.font = pg.font.SysFont(fonte, int(tamanho_fonte * self.tela.get_height()))

    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela, self.dimensoes)

        text_width, text_height = self.font.size(self.texto)
        print(text_width, text_height)
        self.tela.blit(self.font.render(self.texto, False, (51, 0, 0)),
                        (self.pos_tela[0] - text_width/2, self.pos_tela[1] - text_height/2))

    def atualizar(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoApertouBotaoEsquerdo):
                rect = pg.Rect((0, 0), self.dimensoes) 
                rect.center = self.pos_tela
                if rect.collidepoint(evento.pos_mouse): 
                    self.apertou = True

    def resetApertou(self):
        self.apertou = False

