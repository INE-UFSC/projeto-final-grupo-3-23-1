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

    def desenhar(self):
        super().desenhar()

