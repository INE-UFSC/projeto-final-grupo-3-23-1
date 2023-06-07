from basico.entidade import Entidade
from .botao import Botao
from basico.desenhavel import DesenhavelRetangulo

import pygame as pg

class Menu(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        self.tela = tela

        self.botoes = [Botao(tela, (tela.get_width()/2, 3*tela.get_height()/7),(600, 125),
                              DesenhavelRetangulo(tela, (153, 76, 0)), "Jogar"),

                       Botao(tela, (tela.get_width()/2, 4*tela.get_height()/7), (600, 125),
                              DesenhavelRetangulo(tela, (153, 76, 0)), "Instruções"),

                       Botao(tela, (tela.get_width()/2, 5*tela.get_height()/7), (600, 125),
                              DesenhavelRetangulo(tela, (153, 76, 0)), "Créditos"),

                       Botao(tela, (tela.get_width()/2, 6*tela.get_height()/7), (600, 125),
                              DesenhavelRetangulo(tela, (153, 76, 0)), "Sair")
                       ]
        self.modo = ""
        self.font = pg.font.SysFont("Comic Sans MT", 250)

    def atualizar(self, eventos: list):
        for botao in self.botoes:
            botao.atualizar(eventos)

    def desenhar(self):
        self.tela.blit(self.font.render("Labirinto de Talam", False, (255, 255, 255)),
                        (self.tela.get_width()/11, self.tela.get_height()/6))

        for botao in self.botoes:
            botao.desenhar()

    def rodar(self):
        cor_fundo = (255, 255, 255)

        self.tela.fill(cor_fundo)

        self.atualizar()
        self.desenhar()

    
