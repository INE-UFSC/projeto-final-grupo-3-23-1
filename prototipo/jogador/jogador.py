import pygame as pg

from basico.entidadeTela import EntidadeTela
from mapa_jogo.inimigo import Inimigo
from mapa_jogo.sala_porta import *
from .arma import Arma

class Jogador(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, arma = ""):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.__tela = tela
        self.__pos_tela = pos_tela
        self.__dimensoes = dimensoes
        self.__vida = 3
        self.__arma = arma
        self.__powerups = []

    def atualizar(self, eventos: list):
        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_w:
                    if self.__pos_tela != 0: #arrumar
                        self.__pos_tela[1] += 1
                elif evento.key == pg.K_s:
                    if self.__pos_tela != 0:
                        self.__pos_tela[1] -= 1
                elif evento.key == pg.K_a:
                    if self.__pos_tela != 0:
                        self.__pos_tela[0] -= 1
                elif evento.key == pg.K_d:
                    if self.__pos_tela != 0: #arrumar
                        self.__pos_tela[0] += 1 

            if evento.py == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    self.__arma.atirar(self.__powerups)

    def eventoColisao(self, outro):
        if isinstance(outro, Inimigo):
            self.__vida -= 1

        if isinstance(outro, SalaPortaCima):
            pass
        if isinstance(outro, SalaPortaBaixo):
            pass
        if isinstance(outro, SalaPortaEsquerda):
            pass
        if isinstance(outro, SalaPortaDireita):
            pass

    def desenhar(self):
        self.desenhavel.desenhar(self.__tela, self.__pos_tela, self.__dimensoes)