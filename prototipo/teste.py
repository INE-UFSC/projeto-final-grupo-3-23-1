import pygame as pg
from pygame.locals import *

from entidade_tela.entidadeTela import EntidadeTela, FiguraRetangulo

pg.init()
tela = pg.display.set_mode((500, 400))

cor_fundo = (0, 0, 0)
cor_rect = (255, 0, 0)

tela.fill(cor_fundo)

figura = FiguraRetangulo(tela, cor_rect)
personagem = EntidadeTela((30, 40), (100, 100), figura)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

        personagem.desenhar()
         
    pg.display.update()
