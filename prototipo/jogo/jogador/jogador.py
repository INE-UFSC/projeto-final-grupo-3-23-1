import pygame as pg

from basico.entidade_tela import EntidadeTela
from basico.evento import *
from jogo.mapa_jogo.sala_porta import *
from .tiro import Tiro

class Jogador(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, arma = ""):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)

        self.__vida = 1000
        self.__powerups = []
        self.__tiros = []
        self.__direcao = 0

        self.__invulnerabilidade = False
        self.__ultima_colisao = 0

    contador = 0

    @property
    def vida(self):
        return self.__vida

    def atualizar(self, eventos: list):
        if pg.time.get_ticks() - self.__ultima_colisao > 3000:
            self.__invulnerabilidade = False

        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_k:
                    self.atirar(self.__powerups)

            if isinstance(evento, EventoTeclaApertada):
                nova_pos = list(self.pos_tela)

                if evento.tecla == pg.K_w:
                    if nova_pos[1] > 0:
                        nova_pos[1] -= 5
                    self.__direcao = 270
                if evento.tecla == pg.K_s:
                    if nova_pos[1] < 400-self.dimensoes[1]:
                        nova_pos[1] += 5
                    self.__direcao = 90
                if evento.tecla == pg.K_a:
                    if nova_pos[0] > 0:
                        nova_pos[0] -= 5
                    self.__direcao = 180
                if evento.tecla == pg.K_d:
                    if nova_pos[0] < 500-self.dimensoes[0]:
                        nova_pos[0] += 5 
                    self.__direcao = 0

                self.pos_tela = tuple(nova_pos)
                

            if isinstance(evento, EventoColisao) \
                    and any(isinstance(x, Jogador) for x in evento.colisores):
                from jogo.mapa_jogo.inimigo import Inimigo

                if any(isinstance(x, Inimigo) for x in evento.colisores):
                    if not self.__invulnerabilidade:
                        self.__vida -= 1
                        self.__invulnerabilidade = True
                        self.__ultima_colisao = pg.time.get_ticks()
                
                if any(isinstance(x, SalaPorta) for x in evento.colisores):
                    pass

        tiros_rem = []
        for t in self.__tiros:
            if not t.ativo:
                tiros_rem.append(t)
            else:
                t.atualizar(eventos)

        for tiro in tiros_rem:
            self.__tiros.remove(tiro)

    def desenhar(self):
        super().desenhar()

        for t in self.__tiros:
            t.desenhar()

    def atirar(self, powerups):
        self.__tiros.append(Tiro(
            self.tela,
            (self.pos_tela[0] + (self.dimensoes[0] - 10)/2,
                self.pos_tela[1] + (self.dimensoes[1]-10)/2),
            (20, 20), self.__direcao))
