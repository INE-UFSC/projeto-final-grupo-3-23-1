import pygame as pg

from basico.entidadeTela import EntidadeTela
from basico.evento import *
from mapa_jogo.inimigo import Inimigo
from mapa_jogo.sala_porta import *
from .tiro import Tiro

class Jogador(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, direcao, desenhavel, coord_sala_atual,  arma = ""):

        self.__tela = tela
        self.__pos_tela = list(pos_tela)
        self.__dimensoes = dimensoes
        self.__direcao = direcao
        self.__desenhavel = desenhavel

        self.__vida = 3
        self.__powerups = []
        self.__tiros = []

    def atualizar(self, eventos: list):
        for evento in eventos:
            if type(evento) == EventoTeclaApertada:

                if evento.tecla == pg.K_UP:
                    if self.__pos_tela < self.__tela[1]:
                        self.__pos_tela[1] -= 1
                    self.__direcao = 90
                elif evento.tecla == pg.K_DOWN:
                    if self.__pos_tela != 0:
                        self.__pos_tela[1] += 1
                    self.__direcao == 270
                elif evento.tecla == pg.K_LEFT:
                    if self.__pos_tela != 0:
                        self.__pos_tela[0] -= 1
                    self.__direcao == 180
                elif evento.tecla == pg.K_RIGHT:
                    if self.__pos_tela < self.__tela[0]:
                        self.__pos_tela[0] += 1 
                    self.__direcao == 0
                
                elif evento.tecla == pg.K_a:
                    self.atirar(self.__powerups)

            if type(evento) == EventoColisao:

                if type(evento.colisores[0]) == Jogador:
                    if type(evento.colisores[1]) == Inimigo:
                        self.__vida -= 1
                elif type(evento.colisores[1]) == Jogador:
                    if type(evento.colisores[0]) == Inimigo:
                        self.__vida -= 1

        for t in self.__tiros:
            t.atualizar()

    def desenhar(self):
        self.__desenhavel.desenhar(self.__tela, self.__pos_tela, self.__dimensoes)

        for t in self.__tiros:
            t.desenhar()

    def atirar(self, powerups):
        self.__tiros.append(Tiro(self.__pos_tela, self.__dimensoes, self.__direcoes))
