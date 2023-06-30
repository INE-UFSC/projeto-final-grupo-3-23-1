from basico.entidade import Entidade
from .botao import Botao
from basico.desenhavel import DesenhavelRetangulo, DesenhavelImagem
from .instrucoes import Instrucoes
from .creditos import Creditos
from jogo.tela_game_over import TelaGameOver
import os

from enum import Enum

import pygame as pg

class ModoMenu(Enum):
    TelaPrincipal = 1
    Instrucoes = 2
    Creditos = 3

class Menu(Entidade):
    def __init__(self, tela):
        super().__init__(tela)

        arq_fundo = os.path.join('imagens', 'menu', 'menu.png')
        self.__fundo = DesenhavelImagem(tela, arq_fundo, (self.telaW(), self.telaH()))
        dimens_botao = (5/16 *self.telaW(), 125/1080 *self.telaH())

        self.botoes = [Botao(tela, (self.telaW()/2, 3*self.telaH()/7), dimens_botao,
                              DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao), "Jogar"),

                       Botao(tela, (self.telaW()/2, 4*self.telaH()/7), dimens_botao,
                              DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao), "Instruções"),

                       Botao(tela, (self.telaW()/2, 5*self.telaH()/7), dimens_botao,
                              DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao), "Créditos"),

                       Botao(tela, (self.telaW()/2, 6*self.telaH()/7), dimens_botao,
                              DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao), "Sair")
                       ]

        self.__instrucoes = Instrucoes(tela)
        self.__creditos = Creditos(tela)
        self.__modo = ModoMenu.TelaPrincipal
        self.__font = pg.font.SysFont("Comic Sans MT", int(250/1080 * self.telaH()))

    def atualizar(self, eventos: list):
        if self.modo == ModoMenu.TelaPrincipal:
            for botao in self.botoes:
                botao.atualizar(eventos)
        elif self.modo == ModoMenu.Instrucoes:
            self.instrucoes.atualizar(eventos)
        elif self.modo == ModoMenu.Creditos:
            self.creditos.atualizar(eventos)

        self.trocarModo()

    def desenhar(self):
        if self.modo == ModoMenu.TelaPrincipal:
            self.fundo.desenhar((self.telaW()/2, self.telaH()/2))

            for botao in self.botoes:
                botao.desenhar()
        elif self.modo == ModoMenu.Instrucoes:
            self.instrucoes.desenhar()
        elif self.modo == ModoMenu.Creditos:
            self.creditos.desenhar()

    def trocarModo(self):
        if self.botoes[1].apertou:
            self.modo = ModoMenu.Instrucoes
            if self.instrucoes.botao_voltar.apertou:
                self.modo = ModoMenu.TelaPrincipal
                self.instrucoes.botao_voltar.resetApertou()
                self.botoes[1].resetApertou()

        elif self.botoes[2].apertou:
            self.modo = ModoMenu.Creditos
            if self.creditos.botao_voltar.apertou:
                self.modo = ModoMenu.TelaPrincipal
                self.creditos.botao_voltar.resetApertou()
                self.botoes[2].resetApertou()

        elif self.botoes[3].apertou:
            pg.quit()
            exit()

    @property
    def fundo(self):
        return self.__fundo

    @property
    def instrucoes(self):
        return self.__instrucoes
    
    @property
    def creditos(self):
        return self.__creditos
    
    @property
    def modo(self):
        return self.__modo
    
    @modo.setter
    def modo(self, modo):
        self.__modo = modo
    
    @property
    def font(self):
        return self.__font

