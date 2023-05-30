import pygame as pg
from math import cos, sin, radians
from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from basico.evento import EventoColisao

class Tiro(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, direcao, dano = 1, velocidade = 1):
        desenhavel = DesenhavelRetangulo((0, 255, 255))
        super().__init__(tela, pos_tela, dimensoes, desenhavel)

        self.__direcao = direcao

        self.__dano = dano
        self.__velocidade = velocidade

    def atualizar(self, eventos):
        nova_pos = list(self.pos_tela)

        nova_pos[0] += self.__velocidade * cos(radians(self.__direcao))
        nova_pos[1] += self.__velocidade * sin(radians(self.__direcao))

        self.pos_tela = tuple(nova_pos)

        for evento in eventos:
            if isinstance(evento, EventoColisao) \
                    and any(isinstance(x, Tiro) for x in evento.colisores):
                from jogo.mapa_jogo.inimigo import Inimigo
                if any(isinstance(x, Inimigo) for x in evento.colisores):
                    self.ativo = False

