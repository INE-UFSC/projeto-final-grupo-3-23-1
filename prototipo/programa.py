import pygame as pg
from pygame.locals import *

from basico.sistema_colisao import SistemaColisao
from basico.evento import *
from basico.entidade import Entidade

from jogo.jogo import Jogo
from menu.menu import Menu

class Programa(Entidade):
    def __init__(self):
        pg.init()

        info = pg.display.Info()

        self.tela = pg.display.set_mode((1366, 768))
        #self.tela = pg.display.set_mode((info.current_w, info.current_h))
        
        self.jogo = Jogo(self.tela)
        self.menu = Menu(self.tela)

        self.modo = 1

    def rodar(self):
        while True:

            eventos = self.getEventos()

            self.atualizar(eventos)
            self.desenhar()

            pg.display.update()
            pg.time.delay(int(1000/60))

            self.trocarModo()

    def atualizar(self, eventos):
        if self.modo == 1:
            self.menu.atualizar(eventos)
        elif self.modo == 2:
            self.jogo.atualizar(eventos)

    def desenhar(self):
        self.tela.fill((0, 0, 0))
        if self.modo == 1:
            self.menu.desenhar()
        elif self.modo == 2:
            self.jogo.desenhar()

    def getEventos(self):
        eventos = []
        for evento in pg.event.get():
            if evento.type == QUIT:
                pg.quit()
                exit()
            if evento.type == pg.KEYDOWN:
                eventos.append(EventoApertouTecla(evento.key, evento.unicode))
            if evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    eventos.append(EventoApertouBotaoEsquerdo(pg.mouse.get_pos()))
#                    print(eventos[-1].pos_mouse)

        teclas_apertadas = pg.key.get_pressed()
        for tecla in range(len(teclas_apertadas)):
            if teclas_apertadas[tecla]:
                eventos.append(EventoTeclaApertada(tecla))

        colisores = self.getColisores()
        colisoes = SistemaColisao.getColisoes(colisores)
        eventos.extend(colisoes)

        return eventos

    def getColisores(self):
        return self.jogo.getColisores()

    def trocarModo(self):
        if self.menu.botoes[0].apertou:
            self.modo = 2
            self.menu.botoes[0].resetApertou()
        if self.menu.botoes[3].apertou or self.jogo.mapa_jogo.sala_final.botoes[0].apertou:
            pg.quit()
            exit()
        if self.jogo.mapa_jogo.sala_final.botoes[1].apertou:
            self.modo = 1
            self.jogo.mapa_jogo.sala_final.botoes[1].resetApertou()
