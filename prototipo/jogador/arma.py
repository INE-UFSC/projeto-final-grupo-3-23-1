import pygame as pg

from basico.entidadeTela import EntidadeTela

class Arma(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, cadencia, tiro):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.__tela = tela
        self.__pos_tela = pos_tela
        self.__dimensoes = dimensoes
        self.__cadencia = cadencia
        self.__tiro = tiro

    def atirar(self, powerups):
        pass