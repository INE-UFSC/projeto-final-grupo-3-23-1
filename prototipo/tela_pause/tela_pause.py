from basico.desenhavel import *
from basico.entidade import Entidade
from basico.evento import *
from menu.botao import Botao
from menu.instrucoes import Instrucoes

from enum import Enum
import pygame as pg
from pygame.locals import *
import os

class ModoPause(Enum):
    PausePrincipal = 1
    Instrucoes = 2
    Menu = 3
    SairPause = 4

class TelaPause(Entidade):
    def __init__(self, tela):
        super().__init__(tela)

        self.__modo = ModoPause.PausePrincipal

        #tela instuções:
        arq_instrucoes = os.path.join('imagens', 'pause', 'instrucoes.png')
        arq_botao_voltar = os.path.join('imagens', 'botoes', 'voltar azul.png')
        self.__instrucoes = Instrucoes(tela, arq_instrucoes, arq_botao_voltar)

        #imagem fundo:
        arq_imagem_fundo = os.path.join('imagens', 'pause', 'pause.png')
        self.__imagem_fundo = DesenhavelImagem(tela, arq_imagem_fundo, (self.telaW(), self.telaH()))

        #botões:
        dimensao_botoes = (self.telaW()/8, self.telaH()/12)

        #carregar aparência botão: 
        
        #voltar jogo:
        caminho_img_botao_voltar_jogo = os.path.join('imagens', 'botoes', 'voltar ao jogo.png')
        desenhavel_botao_voltar_jogo = DesenhavelImagem(self.tela, caminho_img_botao_voltar_jogo, dimensao_botoes)

        #instruções:
        caminho_img_botao_instrucoes = os.path.join('imagens', 'botoes', 'instrucoes azul.png')
        desenhavel_botao_instrucoes = DesenhavelImagem(self.tela, caminho_img_botao_instrucoes, dimensao_botoes)

        #voltar menu:
        caminho_img_botao_vlt_menu = os.path.join('imagens', 'botoes', 'voltar ao menu.png')
        desenhavel_botao_vlt_menu = DesenhavelImagem(self.tela, caminho_img_botao_vlt_menu, dimensao_botoes)


        self.__botoes = {"voltar_jogo": Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimensao_botoes, 
                               desenhavel_botao_voltar_jogo,""),
                               "instrucoes": Botao(tela, (self.telaW()/4, self.telaH()*9/10),
                               dimensao_botoes, 
                               desenhavel_botao_instrucoes,""),
                               "voltar_menu": Botao(tela, (self.telaW()*3/4, self.telaH()*9/10),
                               dimensao_botoes, 
                               desenhavel_botao_vlt_menu,"")}


    def desenhar(self):

        if self.modo == ModoPause.PausePrincipal:
            self.imagem_fundo.desenhar((self.telaW()/2, self.telaH()/2))
            for botao in self.botoes.values():
                botao.desenhar()

        if self.modo == ModoPause.Instrucoes:
            self.instrucoes.desenhar()

    def atualizar(self, eventos):
        if self.modo == ModoPause.PausePrincipal:
            for botao in self.botoes.values():
                botao.atualizar(eventos)

        self.trocar_modo(eventos)

        if self.modo == ModoPause.Instrucoes:
            self.instrucoes.atualizar(eventos)

    def trocar_modo(self, eventos):

        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_ESCAPE:
                    if self.modo == ModoPause.Instrucoes:
                        self.modo = ModoPause.PausePrincipal
                        

        if self.modo == ModoPause.PausePrincipal: 
            if self.botoes["voltar_jogo"].apertou:
                self.modo = ModoPause.SairPause
                self.botoes["voltar_jogo"].resetApertou()

            elif self.botoes["instrucoes"].apertou:
                self.modo = ModoPause.Instrucoes
                self.botoes["instrucoes"].resetApertou()
                
            elif self.botoes["voltar_menu"].apertou:
                self.modo = ModoPause.Menu
                self.botoes["voltar_menu"].resetApertou()

        elif self.modo == ModoPause.Instrucoes:
            if self.instrucoes.botao_voltar.apertou:
                self.modo = ModoPause.PausePrincipal
                self.instrucoes.botao_voltar.resetApertou()

    def reset(self):
        self.modo = ModoPause.PausePrincipal

    @property
    def botoes(self):
        return self.__botoes
        
    @property
    def imagem_fundo(self):
        return self.__imagem_fundo

    @property
    def instrucoes(self):
        return self.__instrucoes
    
    @property
    def modo(self):
        return self.__modo
    
    @modo.setter
    def modo(self, modo):
        self.__modo = modo
