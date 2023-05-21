import pygame as pg
from pygame.locals import *

from basico.entidadeTela import EntidadeTela, DesenhavelRetangulo
from jogador.jogador import Jogador

pg.init()
tela = pg.display.set_mode((500, 400))

cor_fundo = (0, 0, 0)
cor_rect = (255, 0, 0)

tela.fill(cor_fundo)

figura = DesenhavelRetangulo(cor_rect)
personagem = EntidadeTela(tela, (30, 40), (100, 100), figura)
j = Jogador(tela, (330,100), (100, 100), figura)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

        personagem.desenhar()
        j.desenhar()

    pg.display.update()
