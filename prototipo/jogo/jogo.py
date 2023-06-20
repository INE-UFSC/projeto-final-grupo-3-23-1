import pygame as pg
from pygame.locals import *

from enum import Enum

from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from basico.evento import *

from jogo.mapa_jogo.porta import Porta
from jogo.jogador.jogador import Jogador
from jogo.mapa_jogo.mapa_jogo import MapaJogo
from jogo.mapa_tela.mapa_tela import MapaTela

class Modo(Enum):
    MapaJogo = 1
    MapaTela = 2

class Jogo:
    def __init__(self, tela):
        self.tela = tela

        self.jogador = Jogador(
            self.tela, (tela.get_width()/2, tela.get_height()/2), (50*tela.get_width()/1960, 50*tela.get_height()/1080),
            DesenhavelRetangulo(self.tela, (0, 255, 0))
        )

        self.mapa_jogo = MapaJogo(self.tela, self.jogador)
        self.mapa_tela = MapaTela(self.tela, self.mapa_jogo.salas)

        self.modo = Modo.MapaJogo

    def atualizar(self, eventos: list[Evento]):
        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_TAB:
                    if self.modo == Modo.MapaJogo:
#                        print('mapajogo para mapatela')
                        self.modo = Modo.MapaTela
                    else:
#                        print('mapatela para mapajogo')
                        self.modo = Modo.MapaJogo

#        print(self.modo)

        if self.modo == Modo.MapaJogo:
            self.mapa_jogo.atualizar(eventos)
            if self.jogador.ativo:
                self.jogador.atualizar(eventos)
                    
            if self.jogador.vida <= 0:
                print('Fim de jogo')
                exit()
        else:
            self.mapa_tela.atualizar(eventos)

    def desenhar(self):
        if self.modo == Modo.MapaJogo:
            self.mapa_jogo.desenhar()
            self.jogador.desenhar()
            self.desenharInformacoes()
        else:
            self.mapa_tela.desenhar()

    def getColisores(self):
        colisores = []

        sala = self.mapa_jogo.getSala()

        colisores.extend(sala.getColisores())
        colisores.extend(self.jogador.getColisores())
        return colisores

    def desenharInformacoes(self):
        from basico.desenhavel import DesenhavelTexto
        tamanho_fonte = 25/1080
        text_vida = DesenhavelTexto(self.tela, f'pontos de foco: {self.jogador.vida}', tamanho_fonte)
        text_vida.desenharSuperiorDireito((0, 0))
        espaco_linha = text_vida.espaco_linha
        text_poderes = DesenhavelTexto(self.tela, 'poderes da varinha:', tamanho_fonte)
        text_poderes.desenharSuperiorDireito((0, espaco_linha))
        text_dano = DesenhavelTexto(self.tela, f'- dano: {self.jogador.dano_tiros}', tamanho_fonte)
        text_dano.desenharSuperiorDireito((espaco_linha, espaco_linha*2))
        text_velocidade = DesenhavelTexto(self.tela, f'- velocidade: {self.jogador.velocidade_tiros}', tamanho_fonte)
        text_velocidade.desenharSuperiorDireito((espaco_linha, espaco_linha*3))
        text_cadencia = DesenhavelTexto(self.tela, f'- cadencia: {self.jogador.cadencia_tiros}', tamanho_fonte)
        text_cadencia.desenharSuperiorDireito((espaco_linha, espaco_linha*4))



