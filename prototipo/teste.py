import pygame as pg
from pygame.locals import *

from basico.entidadeTela import EntidadeTela, DesenhavelRetangulo
#from jogador.jogador import Jogador

pg.init()
tela = pg.display.set_mode((500, 400))

cor_fundo = (0, 0, 0)

class TesteJogador(EntidadeTela):
    def __init__(self):
        figura = DesenhavelRetangulo((0, 255, 0))
        super().__init__(tela, (30, 40), (20, 20), figura)

    def eventoColisao(self, outro):
        if isinstance(outro, TesteInimigo):
            print('jogador perdendo vida')

class TesteInimigo(EntidadeTela):
    def __init__(self):
        figura = DesenhavelRetangulo((255, 0, 0))
        super().__init__(tela, (100, 100), (100, 100), figura)

    def eventoColisao(self, outro):
        if isinstance(outro, TesteJogador):
            print('Inimigo feliz')

teste_jogador = TesteJogador()
teste_inimigo = TesteInimigo()

#figura = DesenhavelRetangulo((0, 255, 0))
#j = Jogador(tela, (330,100), (100, 100), figura)


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            nova_pos = list(teste_jogador.pos_tela) 
            if event.key == pg.K_LEFT:
                nova_pos[0] -= 2
            if event.key == pg.K_RIGHT:
                nova_pos[0] += 2
            if event.key == pg.K_UP:
                nova_pos[1] -= 2
            if event.key == pg.K_DOWN:
                nova_pos[1] += 2

            teste_jogador.pos_tela = tuple(nova_pos)

    EntidadeTela.sistema_colisao.checarColisoes()

    tela.fill(cor_fundo)
    teste_jogador.desenhar()
    teste_inimigo.desenhar()
#    j.desenhar()

    pg.display.update()
    pg.time.delay(int(1000/60))
