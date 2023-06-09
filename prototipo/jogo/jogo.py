import pygame as pg
from pygame.locals import *

from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from basico.evento import *

from jogo.mapa_jogo.porta import Porta
from jogo.jogador.jogador import Jogador
from jogo.mapa_jogo.mapa_jogo import MapaJogo

class Jogo:
    def __init__(self, tela):
        self.tela = tela

        self.jogador = Jogador(
            self.tela, (tela.get_width()/2, tela.get_height()/2), (50, 50),
            DesenhavelRetangulo(self.tela, (0, 255, 0))
        )

        self.mapa_jogo = MapaJogo(self.tela, self.jogador)

    def atualizar(self, eventos: list[Evento]):
        self.mapa_jogo.atualizar(eventos)
        if self.jogador.ativo:
            self.jogador.atualizar(eventos)
                
        if self.jogador.vida <= 0:
            print('Fim de jogo')
            exit()

    def desenhar(self):
        self.mapa_jogo.desenhar()
        self.jogador.desenhar()

    def getColisores(self):
        colisores = []

        sala = self.mapa_jogo.getSala()

        colisores.extend(sala.getColisores())
        colisores.extend(self.jogador.getColisores())
        return colisores




