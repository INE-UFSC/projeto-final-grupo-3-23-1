import pygame as pg
from pygame.locals import *

from basico.sistema_colisao import SistemaColisao
from basico.evento import *
from basico.entidade import Entidade

from jogo.jogo import Jogo
from menu.menu import Menu
from menu.instrucoes import Instrucoes
from menu.creditos import Creditos

class Programa(Entidade):
    def __init__(self):
        pg.init()

        info = pg.display.Info()
#        self.tela = pg.display.set_mode((1366, 768))
        tela = pg.display.set_mode((info.current_w, info.current_h))
        super().__init__(tela)

        self.__jogo = Jogo(self.tela)
        self.__menu = Menu(self.tela)
        self.__instrucoes = Instrucoes(self.tela)
        self.__creditos = Creditos(self.tela)

        self.__modo = 1

        self.__colisoes = []

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, jogo):
        if isinstance(jogo, Jogo):
            self.__jogo = jogo

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, menu):
        if isinstance(menu, Menu):
            self.__menu = menu

    @property
    def instrucoes(self):
        return self.__instrucoes

    @instrucoes.setter
    def instrucoes(self, instrucoes):
        if isinstance(instrucoes, Instrucoes):
            self.__instrucoes = instrucoes
    
    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self, creditos):
        if isinstance(creditos, Creditos):
            self.__creditos = creditos

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
        if self.modo == 1:
            self.menu.atualizar(eventos)
        elif self.modo == 2:
            self.jogo.atualizar(eventos)
        elif self.modo == 3:
            self.instrucoes.atualizar(eventos)
        elif self.modo == 4:
            self.creditos.atualizar(eventos)

    def desenhar(self):
        self.tela.fill((0, 0, 0))
        if self.modo == 1:
            self.menu.desenhar()
        elif self.modo == 2:
            self.jogo.desenhar()
        elif self.modo == 3:
            self.instrucoes.desenhar()
        elif self.modo == 4:
            self.creditos.desenhar()

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
            self.modo = 2
            self.menu.botoes[0].resetApertou()
        if self.menu.botoes[1].apertou:
            self.modo = 3
            if self.instrucoes.botao_voltar.apertou:
                self.modo = 1
                self.menu.botoes[1].resetApertou()
                self.instrucoes.botao_voltar.resetApertou()
        if self.menu.botoes[2].apertou:
            self.modo = 4
            if self.creditos.botao_voltar.apertou:
                self.modo = 1
                self.menu.botoes[2].resetApertou()
                self.creditos.botao_voltar.resetApertou()
        if self.menu.botoes[3].apertou or self.jogo.labirinto.sala_final.botoes[0].apertou:
            pg.quit()
            exit()
        if self.jogo.labirinto.sala_final.botoes[1].apertou:
            self.modo = 1
            self.jogo.labirinto.sala_final.botoes[1].resetApertou()
