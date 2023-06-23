from basico.entidade import Entidade
from .botao import Botao
from basico.desenhavel import DesenhavelRetangulo

import pygame as pg

class Menu(Entidade):
    def __init__(self, tela):
        super().__init__(tela)

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
        self.modo = ""
        self.font = pg.font.SysFont("Comic Sans MT", int(250/1080 * self.telaH()))

    def atualizar(self, eventos: list):
        for botao in self.botoes:
            botao.atualizar(eventos)

    def desenhar(self):
        self.tela.blit(self.font.render("Labirinto de Talam", False, (255, 255, 255)),
                        (self.telaW()/11, self.telaH()/6))

        for botao in self.botoes:
            botao.desenhar()

    def rodar(self):
        cor_fundo = (255, 255, 255)

        self.tela.fill(cor_fundo)

        self.atualizar()
        self.desenhar()

    
