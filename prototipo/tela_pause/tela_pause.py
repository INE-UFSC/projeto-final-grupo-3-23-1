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

        camino_imagem_fundo = os.path.join('imagens', 'tela_pause.jpg')
        self.__imagem_fundo = pg.image.load(camino_imagem_fundo)

        dimens_botao_voltar_jogo = (self.telaW()/8, self.telaH()/10)

        #carregar aparência botão: 
        
        caminho_imagem_botao = os.path.join('imagens', 'botao_voltar_ao_jogo.jpg')

        desenhavel_botao_voltar_jogo = DesenhavelImagem(self.tela, caminho_imagem_botao, dimens_botao_voltar_jogo)
        self.__botoes = {"voltar_jogo": Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimens_botao_voltar_jogo, 
                               desenhavel_botao_voltar_jogo,"")}


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
