import pygame as pg
from pygame.locals import *

from jogo.jogo import Jogo

class Programa:
    def __init__(self):
        pg.init()
        tela = pg.display.set_mode((500, 400))

        self.jogo = Jogo(tela)

    def rodar(self):
        while True:
            self.jogo.rodar()

