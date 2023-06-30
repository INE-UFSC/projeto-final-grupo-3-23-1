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
        self.__instrucoes = Instrucoes(tela)

        #imagem fundo:
        camino_imagem_fundo = os.path.join('imagens', 'tela_pause.jpg')
        self.__imagem_fundo = pg.image.load(camino_imagem_fundo)

        #botões:
        dimensao_botoes = (self.telaW()/8, self.telaH()/12)

        #carregar aparência botão: 
        
        #voltar jogo:
        caminho_img_botao_voltar_jogo = os.path.join('imagens', 'botao_voltar_jogo.png')
        desenhavel_botao_voltar_jogo = DesenhavelImagem(self.tela, caminho_img_botao_voltar_jogo, dimensao_botoes)
        botao_voltar_jogo_pos_tela = (self.telaW()/2, self.telaH()*9/10)

        #instruções:
        caminho_img_botao_instrucoes = os.path.join('imagens', 'botao_instr_pause.png')
        desenhavel_botao_instrucoes = DesenhavelImagem(self.tela, caminho_img_botao_instrucoes, dimensao_botoes)
        botao_instrucoes_pos_tela = (botao_voltar_jogo_pos_tela[0], botao_voltar_jogo_pos_tela[1]-2)

        #voltar menu:
        caminho_img_botao_vlt_menu = os.path.join('imagens', 'botao_voltar_menu.png')
        desenhavel_botao_vlt_menu = DesenhavelImagem(self.tela, caminho_img_botao_vlt_menu, dimensao_botoes)


        self.__botoes = {"voltar_jogo": Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimensao_botoes, 
                               desenhavel_botao_voltar_jogo,""),
                               "instrucoes": Botao(tela, (botao_voltar_jogo_pos_tela[0]-300, botao_voltar_jogo_pos_tela[1]),
                               dimensao_botoes, 
                               desenhavel_botao_instrucoes,""),
                               "voltar_menu": Botao(tela, (botao_voltar_jogo_pos_tela[0]+300, botao_voltar_jogo_pos_tela[1]),
                               dimensao_botoes, 
                               desenhavel_botao_vlt_menu,"")}


    def desenhar(self):

        if self.modo == ModoPause.PausePrincipal:
            self.tela.blit(self.imagem_fundo , (0, 0))
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
            self.instrucoes.desenhar()
            self.instrucoes.atualizar(eventos)
        

        if self.modo == ModoPause.Menu:
            pass


    def trocar_modo(self, eventos):

        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_ESCAPE:
                    if self.modo == ModoPause.Instrucoes:
                        self.modo = ModoPause.PausePrincipal
                        

        if self.modo == ModoPause.PausePrincipal: 
            if self.botoes["voltar_jogo"].apertou:
                print("clicou no botão voltar jogo")
                self.modo = ModoPause.SairPause
                self.botoes["voltar_jogo"].resetApertou()

            elif self.botoes["instrucoes"].apertou:
                self.modo = ModoPause.Instrucoes
                self.botoes["instrucoes"].resetApertou()
                
            elif self.botoes["voltar_menu"].apertou:
                print("modo pause = menu")
                self.modo = ModoPause.Menu
                self.botoes["voltar_menu"].resetApertou()

        if self.modo == ModoPause.Instrucoes:
            if self.instrucoes.botao_voltar.apertou:
                self.modo = ModoPause.PausePrincipal
                self.instrucoes.botao_voltar.resetApertou()


        #else:
             #self.modo = ModoPause.PausePrincipal

    def reset(self):
        print("resetou pause")
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
