import pygame as pg
from math import sin, cos, radians

from basico.entidade_tela import EntidadeTela
from basico.evento import *
from jogo.mapa_jogo.sala_porta import *
from .tiro import Tiro

class Jogador(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)

        self.__vida = 3
        self.__powerups = []
        self.__tiros = []
        self.__direcao = 0

        self.__invulnerabilidade = False
    
        self.last_tick = 0
        self.ultima_colisao = 0
        self.ultimo_tiro = 0 

    @property
    def vida(self):
        return self.__vida

    def getColisores(self):
        colisores = []
        colisores.append(self)
        colisores.extend(self.__tiros)
        return colisores

    def atualizar(self, eventos: list):

        if pg.time.get_ticks() - self.ultima_colisao > 3000:
            self.__invulnerabilidade = False
            self.desenhavel.cor = (0, 255, 0)

        if self.__invulnerabilidade:
            if pg.time.get_ticks() - self.last_tick > 250:
                if self.desenhavel.cor == (0, 255, 0):
                    self.desenhavel.cor = (255, 255, 255)
                elif self.desenhavel.cor == (255, 255, 255):
                    self.desenhavel.cor = (0, 255, 0) 
                self.last_tick = pg.time.get_ticks() 
        
        apertadas = []
        moveu = False
        for evento in eventos:
            if isinstance(evento, EventoTeclaApertada):
                if evento.tecla == pg.K_k:
                    self.atirar(self.__powerups)

                if evento.tecla == pg.K_w or evento.tecla == pg.K_s or evento.tecla == pg.K_a or evento.tecla == pg.K_d:
                    apertadas.append(evento.tecla)
                    moveu = True

                if pg.K_w in apertadas:
                    self.__direcao = 270
                if pg.K_s in apertadas:
                    self.__direcao = 90
                if pg.K_a in apertadas:
                    self.__direcao = 180
                if pg.K_d in apertadas:
                    self.__direcao = 0
                if pg.K_w in apertadas and pg.K_a in apertadas:
                    self.__direcao = 225
                if pg.K_w in apertadas and pg.K_d in apertadas:
                    self.__direcao = 315
                if pg.K_s in apertadas and pg.K_a in apertadas:
                    self.__direcao = 135
                if pg.K_s in apertadas and pg.K_d in apertadas:
                    self.__direcao = 45


            if isinstance(evento, EventoColisao) \
                    and evento.possui(self):
                from jogo.mapa_jogo.inimigo import Inimigo

                if evento.possuiTipo(Inimigo):
                    if not self.__invulnerabilidade:
                        self.__vida -= 1
                        self.__invulnerabilidade = True
                        self.desenhavel.cor = (255, 255, 255)
                        self.ultima_colisao = pg.time.get_ticks()
                        self.last_tick = pg.time.get_ticks()
                
                if evento.possuiTipo(SalaPorta):
                    sala_porta = evento.getElemDoTipo(SalaPorta)
                    if sala_porta.porta.aberta:
                        self.__tiros = []
                        if isinstance(sala_porta, SalaPortaBaixo):
                            self.pos_tela = (self.pos_tela[0], sala_porta.dimensoes[1]+self.dimensoes[1]/2)
                        elif isinstance(sala_porta, SalaPortaCima):
                            self.pos_tela = (self.pos_tela[0], self.tela.get_height()-(sala_porta.dimensoes[1]+self.dimensoes[1]/2))
                        elif isinstance(sala_porta, SalaPortaDireita):
                            self.pos_tela = (sala_porta.dimensoes[0]+self.dimensoes[0]/2, self.pos_tela[1])
                        elif isinstance(sala_porta, SalaPortaEsquerda):
                            self.pos_tela = (self.tela.get_width()-(sala_porta.dimensoes[0]+self.dimensoes[0]/2), self.pos_tela[1])
        if moveu:
            nova_pos = list(self.pos_tela)
            nova_pos[1] += 5 * sin(radians(self.__direcao))
            nova_pos[0] += 5 * cos(radians(self.__direcao))

            if nova_pos[0] > self.tela.get_width()-self.dimensoes[0]/2:
                nova_pos[0] = self.tela.get_width()-self.dimensoes[0]/2
            if nova_pos[0] < self.dimensoes[0]/2:
                nova_pos[0] = self.dimensoes[0]/2
            if nova_pos[1] > self.tela.get_height()-self.dimensoes[1]/2:
                nova_pos[1] = self.tela.get_height()-self.dimensoes[1]/2
            if nova_pos[1] < self.dimensoes[1]/2:
                nova_pos[1] = self.dimensoes[1]/2

            self.pos_tela = tuple(nova_pos)
                
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
        if pg.time.get_ticks() - self.ultimo_tiro > 500:
            self.ultimo_tiro = pg.time.get_ticks()
            self.__tiros.append(Tiro(
                self.tela,
                self.pos_tela,
                (self.tela.get_width()*20/1980, self.tela.get_height()*20/1080),
                self.__direcao
            ))
