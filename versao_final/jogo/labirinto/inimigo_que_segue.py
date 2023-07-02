from basico.entidade_tela import EntidadeTela
from basico.evento import Evento, EventoColisao
from jogo.jogador.jogador import Jogador
import pygame as pg
from math import atan2, cos, sin, radians, pi
from basico.sistema_colisao import SistemaColisao
from basico.desenhavel import *
from jogo.labirinto.inimigo import Inimigo
from .obstaculo import Obstaculo

import os
import math

class InimigoQueSegue(Inimigo):

    def __init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador ):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador)

        self.__dano = dano
        self.__direction = 0
        self.__nivel_velocidade = velocidade
        self.__velocidade = 0
        self.__vida = vida_inicial
        self.__alvo = jogador
        # Crie um objeto Clock para controlar o tempo
        #self.__clock = pg.time.Clock()
        self.__colidindo = False
        self.__pode_mexer = True

        # imagens
        arquivo = os.path.join('imagens', 'inimigos', 'inimigo.png')
        sheet = pg.image.load(arquivo).convert()

        qtd = 9

        w, h = sheet.get_rect().size
        x = w/qtd
        y = h/qtd

        indices = [
            (2, 1),
            (2, 2),
            (1, 2),
            (0, 2),
            (0, 1),
            (0, 0),
            (1, 0),
            (2, 0)
        ]

        self.__desenhaveis = []

        i0 = 3
        j0 = 3
        for i in range(8):
            curr_i, curr_j = indices[i]

            x = (i0+curr_i) * w/qtd
            y = (j0+curr_j) * h/qtd

            sprite = pg.Surface((w/qtd, h/qtd))
            sprite.blit(sheet, (0, 0), (x, y, w/qtd, h/qtd))

            self.__desenhaveis.append(DesenhavelSurface(tela, sprite, (w/qtd, h/qtd), (89, 139, 205)))

    def desenhar(self):
        projetil_direcao = math.degrees(self.direction)

        x = int(round(projetil_direcao / 360 * 8))
        x %= 8

        self.desenhavel = self.__desenhaveis[x]

        super().desenhar()

