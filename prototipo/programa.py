import pygame as pg
from pygame.locals import *

from basico.entidadeTela import EntidadeTela, DesenhavelRetangulo
from basico.evento import EventoPygame
from jogador.jogador import Jogador
from mapa_tela.mapa_tela import MapaTela
from mapa_jogo.mapaJogo import MapaJogo

pg.init()
tela = pg.display.set_mode((500, 400))

cor_fundo = (0, 0, 0)

jogador = Jogador(tela)
mapa_jogo = MapaJogo(tela)

while True:
    eventos = []
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
            exit()
        if evento.type == pg.KEYDOWN:
            eventos.append(EventoApertouTecla(evento))

        teclas_apertadas = pg.key.get_pressed()
        for tecla in teclas_apertadas:
            eventos.append(EventoTeclaApertada(tecla))

    eventos.extend(EntidadeTela.sistema_colisao.getColisoes())

    jogador.atualizar(eventos)
    mapa_jogo.atualizar(eventos)
            
    tela.fill(cor_fundo)

    jogador.desenhar()
    mapa_jogo.desenhar()

    EntidadeTela.sistema_colisao.removerNaoAtivos()

    pg.display.update()
    pg.time.delay(int(1000/60))

