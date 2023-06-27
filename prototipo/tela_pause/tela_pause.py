from basico.desenhavel import *
from basico.entidade import Entidade
from basico.evento import Evento
from menu.botao import Botao
from menu.instrucoes import Instrucoes

from enum import Enum
import pygame as pg
from pygame.locals import *
import os

class Modo(Enum):
    PausePrincipal = 1
    Instrucoes = 2
    Menu = 3
    SairPause = 4

class TelaPause(Entidade):
    def __init__(self, tela):
        super().__init__(tela)

        #tela instuções:
        self.__instrucoes = Instrucoes(self.tela)

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
        print("BOTÃO VOLTAR = ", botao_voltar_jogo_pos_tela, "BOTAO INSTRUCOES:", botao_instrucoes_pos_tela)


    def desenhar(self):
        self.tela.blit(self.imagem_fundo , (0, 0))

        for botao in self.botoes.values():
            botao.desenhar()

    def atualizar(self, eventos):
        for botao in self.botoes.values():
            botao.atualizar(eventos)

        self.trocar_modo()


    def trocar_modo(self):

        if self.botoes["voltar_jogo"].apertou:
            self.modo = Modo.SairPause
            self.botoes["voltar_jogo"].resetApertou()

        elif self.botoes["instrucoes"].apertou:
            self.modo = Modo.Instrucoes
            self.botoes["instrucoes"].resetApertou()
            
        elif self.botoes["voltar_menu"].apertou:
            self.modo = Modo.Menu
            self.botoes["voltar_menu"].resetApertou()

        else:
             self.modo = Modo.PausePrincipal

        

    @property
    def botoes(self):
        return self.__botoes
        
    @property
    def imagem_fundo(self):
        return self.__imagem_fundo
