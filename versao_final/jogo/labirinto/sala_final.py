from .sala import Sala
from .jogador_sala_final import JogadorSalaFinal
from basico.evento import EventoColisao
from jogo.jogador.jogador import Jogador
import pygame as pg
import os
from menu.botao import Botao
from basico.desenhavel import DesenhavelRetangulo, DesenhavelImagem

class SalaFinal(Sala):
    def __init__(self, tela, desenhavel, jogador):
        super().__init__(tela, desenhavel)
        self.__jogador_sala_final = JogadorSalaFinal(tela, jogador)
        self.__modo = 1
        self.__jogador_dimensoes = jogador.dimensoes

        self.__texto_final = DesenhavelImagem(tela, os.path.join('imagens', 'sala_final', 'texto_final.png'),
                                              (self.telaW()*5/8, self.telaH()/3))

        dimens_botao = (self.telaW()/6, self.telaH()/9)
        arq_im_botao_sair = os.path.join('imagens', 'botoes', 'sair_branco.png')
        arq_im_botao_voltar_menu = os.path.join('imagens', 'botoes', 'voltar_ao_menu_branco.png')
        self.__botoes = [Botao(tela, (6*self.telaW()/8, 25*self.telaH()/32),
                                  dimens_botao,
                                  DesenhavelImagem(tela, arq_im_botao_sair, dimens_botao),
                                  ''),
                        Botao(tela, (6*self.telaW()/8, 29*self.telaH()/32),
                                  dimens_botao,
                                  DesenhavelImagem(tela, arq_im_botao_voltar_menu, dimens_botao),
                                  '')]

    def desenhar(self):
        super().desenhar()
        self.__jogador_sala_final.desenhar()
        if self.__modo == 2:
            self.__texto_final.desenhar((self.telaW()/2, self.telaH()*2.25/8))
            for botao in self.__botoes:
                botao.desenhar()
    
    def atualizar(self, eventos):
        super().atualizar(eventos)
        for evento in eventos:
            if isinstance(evento, EventoColisao):
                if evento.possui(self.__jogador_sala_final):
                    if evento.possuiTipo(Jogador):
                        self.__modo = 2
        for botao in self.__botoes:
            botao.atualizar(eventos)

    def getColisores(self):
        colisores = super().getColisores()
        colisores.append(self.__jogador_sala_final)
        return colisores

    @property
    def botoes(self):
        return self.__botoes