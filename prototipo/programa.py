import pygame as pg
from pygame.locals import *

from basico.entidadeTela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from basico.evento import *
from mapa_jogo.porta import Porta
from jogador.jogador import Jogador
from mapa_jogo.aparencia import Aparencia
from mapa_jogo.musica import Musica
from mapa_jogo.textura import Textura
from mapa_jogo.inimigo import Inimigo
from mapa_jogo.mapaJogo import MapaJogo
from mapa_jogo.salaInimigo import SalaInimigo
from mapa_jogo.sala_porta import *


def lerEventos():
    eventos = []
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
            exit()
        if evento.type == pg.KEYDOWN:
            eventos.append(EventoApertouTecla(evento.key))

        teclas_apertadas = pg.key.get_pressed()
        for tecla in range(len(teclas_apertadas)):
            if teclas_apertadas[tecla]:
                eventos.append(EventoTeclaApertada(tecla))

    colisoes = EntidadeTela.sistema_colisao.getColisoes()
    eventos.extend(colisoes)

    return eventos

def tentarMudarSala(coord_sala_atual, mapa_jogo, eventos):
    for evento in eventos:
        if isinstance(evento, EventoColisao):
            movimentacao = {
                SalaPortaEsquerda: [-1, 0],
                SalaPortaDireita:  [1, 0],
                SalaPortaCima:     [0, -1],
                SalaPortaBaixo:    [0, 1]
            }

            for colisor in evento.colisores:
                tipo_sala_porta = None
                if isinstance(colisor, SalaPorta):
                    tipo_sala_porta = type(colisor)

                if tipo_sala_porta is not None:
                    sala_atual = list(coord_sala_atual)

                    for i in range(len(sala_atual)):
                        sala_atual[i] = (sala_atual[i] + movimentacao[tipo_sala_porta][i]) % 2

                        if sala_atual[i] < 0:
                            sala_atual[i] += 2

def criarMapaJogo(tela, jogador):
    salas = []
    portas = [Porta(), Porta(), Porta(), Porta()]

    aparencia = Aparencia(Musica(), Textura())

    for i in range(2):
        linha = []
        for j in range(2):
            posicoes = [
                [0, 0],
                [0, 200],
                [300, 400]
            ]

            inimigos = []
            for inimigo_i in range(3):
                inimigos.append(Inimigo(
                    tela,
                    posicoes[inimigo_i], [50, 50],
                    DesenhavelRetangulo((255, 0, 0)),
                    3, 1, 1,
                    jogador
                ))

            inimigos = []

            linha.append(SalaInimigo(
                Aparencia(Musica(), Textura()),
                [],
                inimigos
            ))
        salas.append(linha)

    def adicionarSalaPorta(sala, porta, tipo):
        sala_porta = tipo(tela, sala, porta)
        porta.adicionar_sala_porta(sala_porta)
        sala.adicionar_sala_porta(sala_porta)

    # 0,0 -0- 0,1
    #  |       |
    #  3       1 
    #  |       |
    # 1,0 -2- 1,1

    adicionarSalaPorta(salas[0][0], portas[0], SalaPortaDireita)
    adicionarSalaPorta(salas[0][1], portas[0], SalaPortaEsquerda)
    adicionarSalaPorta(salas[0][1], portas[1], SalaPortaBaixo)
    adicionarSalaPorta(salas[1][1], portas[1], SalaPortaCima)
    adicionarSalaPorta(salas[1][1], portas[2], SalaPortaEsquerda)
    adicionarSalaPorta(salas[1][0], portas[2], SalaPortaDireita)
    adicionarSalaPorta(salas[1][0], portas[3], SalaPortaCima)
    adicionarSalaPorta(salas[0][0], portas[3], SalaPortaBaixo)

    return MapaJogo(salas, portas)

pg.init()
tela = pg.display.set_mode((500, 400))

cor_fundo = (0, 0, 0)

jogador = Jogador(
        tela, (20, 20), (50, 50),
        DesenhavelRetangulo((0, 255, 0)))
        
mapa_jogo = criarMapaJogo(tela, jogador)

coord_sala_atual = [0, 0]

while True:
    eventos = lerEventos()

    jogador.atualizar(eventos)
    mapa_jogo.atualizar(eventos)
            
    tela.fill(cor_fundo)

    jogador.desenhar()
    mapa_jogo.desenhar()

    EntidadeTela.sistema_colisao.removerNaoAtivos()

    tentarMudarSala(coord_sala_atual, mapa_jogo, eventos)

    pg.display.update()
    pg.time.delay(int(1000/60))

