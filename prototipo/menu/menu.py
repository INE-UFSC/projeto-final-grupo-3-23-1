from basico.entidade import Entidade
from .botao import Botao
from basico.desenhavel import DesenhavelImagem
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

        arq_im_fundo = os.path.join('imagens', 'menu', 'menu.png')
        self.__im_fundo = DesenhavelImagem(tela, arq_im_fundo, (self.telaW(), self.telaH()))

        arq_botao_jogar = os.path.join('imagens', 'botoes', 'jogar.png')
        arq_botao_instrucoes = os.path.join('imagens', 'botoes', 'instrucoes.png')
        arq_botao_creditos = os.path.join('imagens', 'botoes', 'creditos.png')
        arq_botao_sair = os.path.join('imagens', 'botoes', 'sair.png')

        dimens_botao = (1/7*self.telaW(), 8/84*self.telaH())

        self.botoes = [Botao(tela, (self.telaW()/2, 3*self.telaH()/7), dimens_botao,
                              DesenhavelImagem(tela, arq_botao_jogar, (1/6 *self.telaW(), 1/9 *self.telaH())), ""),

                       Botao(tela, (self.telaW()/4, 4*self.telaH()/7), dimens_botao,
                              DesenhavelImagem(tela, arq_botao_instrucoes, dimens_botao), ""),

                       Botao(tela, (self.telaW()/4, 5*self.telaH()/7), dimens_botao,
                              DesenhavelImagem(tela, arq_botao_creditos, dimens_botao), ""),

                       Botao(tela, (self.telaW()*3/4, 4.5*self.telaH()/7), dimens_botao,
                              DesenhavelImagem(tela, arq_botao_sair, dimens_botao), "")
                       ]
        arq_instrucoes = os.path.join('imagens', 'menu', 'instrucoes.png')
        arq_botao_voltar = os.path.join('imagens', 'botoes', 'voltar.png')
        self.__instrucoes = Instrucoes(tela, arq_instrucoes, arq_botao_voltar)
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
            self.im_fundo.desenhar((self.telaW()/2, self.telaH()/2))

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
    def im_fundo(self):
        return self.__im_fundo

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

