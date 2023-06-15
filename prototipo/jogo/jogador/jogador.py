import pygame as pg
from math import sin, cos, radians

from basico.entidade_tela import EntidadeTela
from basico.evento import *
from jogo.mapa_jogo.sala_porta import *
from jogo.mapa_jogo.powerup import *
from .tiro import Tiro

class Jogador(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)

        self.__direcao = 0
        self.__vida = 3
        self.__powerups = []
        self.__tiros = []

        self.__invulnerabilidade = False
        self.__ultimo_tick_inv = 0
        self.__ultima_colisao = 0
        self.__ultimo_tiro = 0 

    def atualizar(self, eventos: list):

        if pg.time.get_ticks() - self.ultima_colisao > 3000:
            self.invulnerabilidade = False
            self.desenhavel.cor = (0, 255, 0)

        if self.invulnerabilidade:
            if pg.time.get_ticks() - self.last_tick > 250:
                if self.desenhavel.cor == (0, 255, 0):
                    self.desenhavel.cor = (255, 255, 255)
                elif self.desenhavel.cor == (255, 255, 255):
                    self.desenhavel.cor = (0, 255, 0) 
                self.last_tick = pg.time.get_ticks() 
        
        apertadas = []
        moveu = False
        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_k:
                    self.atirar(self.powerups)

            if isinstance(evento, EventoTeclaApertada):
                if evento.tecla == pg.K_w or evento.tecla == pg.K_s \
                        or evento.tecla == pg.K_a or evento.tecla == pg.K_d:
                    apertadas.append(evento.tecla)
                    moveu = True

                if pg.K_w in apertadas:
                    self.direcao = 270
                if pg.K_s in apertadas:
                    self.direcao = 90
                if pg.K_a in apertadas:
                    self.direcao = 180
                if pg.K_d in apertadas:
                    self.direcao = 0
                if pg.K_w in apertadas and pg.K_a in apertadas:
                    self.direcao = 225
                if pg.K_w in apertadas and pg.K_d in apertadas:
                    self.direcao = 315
                if pg.K_s in apertadas and pg.K_a in apertadas:
                    self.direcao = 135
                if pg.K_s in apertadas and pg.K_d in apertadas:
                    self.direcao = 45

            if isinstance(evento, EventoColisao) \
                    and evento.possui(self):
                from jogo.mapa_jogo.inimigo import Inimigo

                if evento.possuiTipo(Inimigo):
                    if not self.invulnerabilidade:
                        self.vida -= 1
                        self.invulnerabilidade = True
                        self.desenhavel.cor = (255, 255, 255)
                        self.ultima_colisao = pg.time.get_ticks()
                        self.last_tick = pg.time.get_ticks()

                if evento.possuiTipo(Powerup):
                    self.powerups.append(evento.getElemDoTipo(Powerup))
                
                if evento.possuiTipo(SalaPorta):
                    sala_porta = evento.getElemDoTipo(SalaPorta)
                    if sala_porta.porta.aberta:
                        self.__tiros = []
                        if isinstance(sala_porta, SalaPortaBaixo):
                            self.pos_tela = (self.pos_tela[0], 
                                             sala_porta.dimensoes[1]+self.dimensoes[1]/2)
                        elif isinstance(sala_porta, SalaPortaCima):
                            self.pos_tela = (self.pos_tela[0], 
                                             self.tela.get_height()-(sala_porta.dimensoes[1]+self.dimensoes[1]/2))
                        elif isinstance(sala_porta, SalaPortaDireita):
                            self.pos_tela = (sala_porta.dimensoes[0]+self.dimensoes[0]/2, 
                                             self.pos_tela[1])
                        elif isinstance(sala_porta, SalaPortaEsquerda):
                            self.pos_tela = (self.tela.get_width()-(sala_porta.dimensoes[0]+self.dimensoes[0]/2), 
                                             self.pos_tela[1])

        if moveu:
            nova_pos = list(self.pos_tela)
            nova_pos[0] += 5 * cos(radians(self.direcao))
            nova_pos[1] += 5 * sin(radians(self.direcao))

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
        for t in self.tiros:
            if not t.ativo:
                tiros_rem.append(t)
            else:
                t.atualizar(eventos)

        for tiro in tiros_rem:
            self.tiros.remove(tiro)

    def desenhar(self):
        super().desenhar()

        for t in self.tiros:
            t.desenhar()

    def getColisores(self):
        colisores = []
        colisores.append(self)
        colisores.extend(self.tiros)
        return colisores

    def atirar(self, powerups):
        dano, cadencia, velocidade = 1, 500, 10
        for powerup in powerups:
            if isinstance(powerup, PowerupCadencia):
                cadencia -= powerup.incremento
            
            if isinstance(powerup, PowerupVelocidadeTiro):
                velocidade += powerup.incremento

            if isinstance(powerup, PowerupDano):
                dano += powerup.incremento

        if pg.time.get_ticks() - self.ultimo_tiro > cadencia:
            self.ultimo_tiro = pg.time.get_ticks()
            self.tiros.append(Tiro(self.tela, self.pos_tela,
                                   (self.tela.get_width()*20/1980, self.tela.get_height()*20/1080),
                                    self.direcao, dano, velocidade))

    @property
    def direcao(self):
        return self.__direcao

    @property
    def vida(self):
        return self.__vida

    @property
    def powerups(self):
        return self.__powerups

    @property
    def tiros(self):
        return self.__tiros

    @property
    def invulnerabilidade(self):
        return self.__invulnerabilidade

    @property
    def ultimo_tick_inv(self):
        return self.__ultimo_tick_inv

    @property 
    def ultima_colisao(self):
        return self.__ultima_colisao
    
    @property
    def ultimo_tiro(self):
        return self.__ultimo_tiro
    
    @direcao.setter
    def direcao(self, direcao):
        self.__direcao = direcao

    @vida.setter
    def vida(self, vida):
        self.__vida = vida 

    @invulnerabilidade.setter
    def invulnerabilidade(self, invul):
        self.__invulnerabilidade = invul
    
    @ultimo_tick_inv.setter
    def ultimo_tick_inv(self, ultimo):
        self.__ultimo_tick_inv = ultimo
    
    @ultima_colisao.setter
    def ultima_colisao(self, ultima):
        self.__ultima_colisao = ultima
    
    @ultimo_tiro.setter
    def ultimo_tiro(self, ultimo):
        self.__ultimo_tiro = ultimo