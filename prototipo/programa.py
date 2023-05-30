import pygame as pg
from pygame.locals import *

from jogo import Jogo

pg.init()
tela = pg.display.set_mode((500, 400))

jogo = Jogo(tela)

while True:
    jogo.rodar()

