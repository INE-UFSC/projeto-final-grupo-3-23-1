import pygame as pg
from pygame.locals import *

from basico.sistema_colisao import SistemaColisao
from basico.evento import *
from basico.entidade import Entidade

from jogo.jogo import *
from menu.menu import Menu

from enum import Enum

class ModoPrograma(Enum):
    Menu = 1
    Jogo = 2


class Programa(Entidade):
    def __init__(self):
        pg.init()

        info = pg.display.Info()
#        self.tela = pg.display.set_mode((1366, 768))
        tela = pg.display.set_mode((info.current_w, info.current_h*9/10))
        super().__init__(tela)

        self.__jogo = Jogo(self.tela)
        self.__menu = Menu(self.tela)

        self.__modo = ModoPrograma.Menu

        self.__colisoes = []

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, jogo):
        self.__jogo = jogo

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, menu):
        self.__menu = menu

    @property
    def modo(self):
        return self.__modo

    @modo.setter
    def modo(self, modo):
        self.__modo = modo

    @property
    def colisoes(self):
        return self.__colisoes

    @colisoes.setter
    def colisoes(self, colisoes):
        self.__colisoes = colisoes


    def rodar(self):
        while True:
#            print('inicio do frame')

            eventos = self.getEventos()
            eventos.extend(self.colisoes)

            self.atualizar(eventos)

            colisores = self.getColisores()

            self.colisoes = SistemaColisao.getColisoes(colisores)
            SistemaColisao.removerSobreposicoes(colisores)
            SistemaColisao.colocarDentroDaTela(colisores, self.tela)

            self.desenhar()

            pg.display.update()
            pg.time.delay(int(1000/60))

            self.trocarModo()

    def atualizar(self, eventos):
        if self.modo == ModoPrograma.Menu:
            self.menu.atualizar(eventos)

        elif self.modo == ModoPrograma.Jogo:
            self.jogo.atualizar(eventos)
            

    def desenhar(self):
        self.tela.fill((0, 0, 0))
        if self.modo == ModoPrograma.Menu:
            self.menu.desenhar()
        elif self.modo == ModoPrograma.Jogo:
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

        return eventos

    def getColisores(self):
        return self.jogo.getColisores()

    def trocarModo(self):
        if self.menu.botoes[0].apertou:
            self.modo = ModoPrograma.Jogo
            self.jogo = Jogo(self.tela)
            self.menu.botoes[0].resetApertou()

            pg.mixer.music.load('musica/wish_youd_never_left.mp3')
            pg.mixer.music.play(-1)

        if self.jogo.labirinto.sala_final.botoes[1].apertou:
            self.modo = ModoPrograma.Menu
            self.jogo.labirinto.sala_final.botoes[1].resetApertou()

        if self.jogo.tela_game_over.botoes[1].apertou:
            self.jogo.tela_game_over.botoes[1].resetApertou()
            self.modo = ModoPrograma.Menu


        if self.modo == ModoPrograma.Jogo:
            if self.jogo.modo == ModoJogo.IrParaMenu:
                self.modo = ModoPrograma.Menu
