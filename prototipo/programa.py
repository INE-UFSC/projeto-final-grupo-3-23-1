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

contador = 0

def tentarMudarSala(coord_sala_atual, mapa_jogo, eventos):
    for evento in eventos:
        if isinstance(evento, EventoColisao) \
                and any(isinstance(x, SalaPorta) for x in evento.colisores) \
                and any(isinstance(x, Jogador) for x in evento.colisores):
            movimentacao = {
                SalaPortaEsquerda: [-1, 0],
                SalaPortaDireita:  [1, 0],
                SalaPortaCima:     [0, -1],
                SalaPortaBaixo:    [0, 1]
            }

            tipo_sala_porta = None
            for colisor in evento.colisores:
                if isinstance(colisor, SalaPorta):
                    tipo_sala_porta = type(colisor)

            sala_atual = coord_sala_atual

            for i in range(len(sala_atual)):
                sala_atual[i] = (sala_atual[i] + movimentacao[tipo_sala_porta][i]) % 2

                if sala_atual[i] < 0:
                    sala_atual[i] += 2
            return True
    return False

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

    return MapaJogo(salas, portas), inimigos

pg.init()
tela = pg.display.set_mode((500, 400))


jogador = Jogador(
        tela, (20, 20), (50, 50),
        DesenhavelRetangulo((0, 255, 0)))
        
mapa_jogo, inimigos = criarMapaJogo(tela, jogador)

coord_sala_atual = [0, 0]

while True:
    eventos = lerEventos()

    jogador.atualizar(eventos)
    mapa_jogo.atualizar(eventos)
            
    t_sala_atual = tuple(coord_sala_atual)

    if t_sala_atual == (0, 0):
        cor_fundo = (255, 255, 255)
    elif t_sala_atual == (0, 1):
        cor_fundo = (0, 0, 0)
    elif t_sala_atual == (1, 0):
        cor_fundo = (200, 230, 255)
    elif t_sala_atual == (1, 1):
        cor_fundo = (232, 202, 45)

    tela.fill(cor_fundo)

    jogador.desenhar()
    mapa_jogo.desenhar()

#    for inimigo in inimigos:
#        if EntidadeTela.sistema_colisao.colidiu(inimigo, jogador):
#            print('colidiu')

    EntidadeTela.sistema_colisao.removerNaoAtivos()

    if (tentarMudarSala(coord_sala_atual, mapa_jogo, eventos)):
        jogador.pos_tela = (250, 200)

    if jogador.vida <= 0:
        print('Fim de jogo')
        exit()

    pg.display.update()
    pg.time.delay(int(1000/60))

