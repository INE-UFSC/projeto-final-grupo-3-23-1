from basico.desenhavel import *
from basico.entidade import Entidade
from basico.evento import Evento
from menu.botao import Botao
import pygame as pg
from pygame.locals import *
import os

class TelaPause(Entidade):
    def __init__(self, tela):
        super().__init__(tela)

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


        self.__botoes = {"voltar_jogo": Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimensao_botoes, 
                               desenhavel_botao_voltar_jogo,""),
                               "instrucoes": Botao(tela, (botao_voltar_jogo_pos_tela[0], botao_voltar_jogo_pos_tela[0]+2),
                               dimensao_botoes, 
                               desenhavel_botao_instrucoes,"")}


    def desenhar(self):
        self.tela.blit(self.imagem_fundo , (0, 0))

        for botao in self.botoes.values():
            botao.desenhar()

    def atualizar(self, eventos):
        for botao in self.botoes.values():
            botao.atualizar(eventos)

    @property
    def botoes(self):
        return self.__botoes
        
    @property
    def imagem_fundo(self):
        return self.__imagem_fundo
