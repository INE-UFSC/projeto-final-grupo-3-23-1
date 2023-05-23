import pygame as pg

from basico.entidadeTela import EntidadeTela
from basico.evento import *
from mapa_jogo.sala_porta import *
from .tiro import Tiro

class Jogador(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, arma = ""):
        self.__tela = tela
        self.__pos_tela = list(pos_tela)
        self.__dimensoes = dimensoes
        self.__direcao = 90
        self.__desenhavel = desenhavel

        self.__vida = 3
        self.__powerups = []
        self.__tiros = []

    @property
    def pos_tela(self):
        return self.__pos_tela

    def atualizar(self, eventos: list):
        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_z:
                    self.atirar(self.__powerups)

            if isinstance(evento, EventoTeclaApertada):
                print('apertada')
                if evento.tecla == pg.K_w:
                    if self.__pos_tela[1] > 0:
                        self.__pos_tela[1] -= 5
                    self.__direcao = 270
                if evento.tecla == pg.K_s:
                    if self.__pos_tela[1] < 400:
                        self.__pos_tela[1] += 5
                    self.__direcao = 90
                if evento.tecla == pg.K_a:
                    if self.__pos_tela[0] > 0:
                        self.__pos_tela[0] -= 5
                    self.__direcao = 180
                if evento.tecla == pg.K_d:
                    if self.__pos_tela[0] < 500:
                        self.__pos_tela[0] += 5 
                    self.__direcao = 0
                

            if type(evento) == EventoColisao:
                from mapa_jogo.inimigo import Inimigo

                if type(evento.colisores[0]) == Jogador:
                    if type(evento.colisores[1]) == Inimigo:
                        self.__vida -= 1
                elif type(evento.colisores[1]) == Jogador:
                    if type(evento.colisores[0]) == Inimigo:
                        self.__vida -= 1

        for t in self.__tiros:
            t.atualizar(eventos)

    def desenhar(self):
        self.__desenhavel.desenhar(self.__tela, self.__pos_tela, self.__dimensoes)

        for t in self.__tiros:
            t.desenhar()

    def atirar(self, powerups):
        self.__tiros.append(Tiro(self.__tela, self.__pos_tela, (10, 10), self.__direcao))
