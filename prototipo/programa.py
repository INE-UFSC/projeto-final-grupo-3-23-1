import pygame as pg
from pygame.locals import *

from jogo.jogo import Jogo
from menu.menu import Menu

class Programa:
    def __init__(self):
        pg.init()
        tela = pg.display.set_mode((500, 400))

        self.jogo = Jogo(tela)
        self.menu = Menu(tela)

        self.modo = 1

    def rodar(self):
        while True:
#            if self.modo == 1:
#                self.menu.rodar()
#            elif self.modo == 2:
            self.jogo.rodar()

#            self.trocarModo()

    def trocarModo(self):
        if self.menu.botoes[0].ativo:
            self.modo = 2
