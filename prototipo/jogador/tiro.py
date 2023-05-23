import pygame as pg
from math import cos, sin, radians
from basico.entidadeTela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo

class Tiro(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, direcao, dano = 1, velocidade = 1):

        self.__tela = tela
        self.__pos_tela = list(pos_tela)
        self.__dimensoes = dimensoes
        self.__direcao = direcao
        self.__desenhavel = DesenhavelRetangulo((0, 255, 255))

        self.__dano = dano
        self.__velocidade = velocidade

    def atualizar(self, eventos):
        self.__pos_tela[0] += self.__velocidade * cos(radians(self.__direcao))
        self.__pos_tela[1] += self.__velocidade * sin(radians(self.__direcao))

    def desenhar(self):
        self.__desenhavel.desenhar(self.__tela, self.__pos_tela, self.__dimensoes)

    def eventoColisao(self, outro):
        from mapa_jogo.inimigo import Inimigo

        if isinstance(outro, Inimigo):
            self.kill()



