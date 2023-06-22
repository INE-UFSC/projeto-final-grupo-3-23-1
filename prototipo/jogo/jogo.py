import pygame as pg
from pygame.locals import *

from enum import Enum

from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from basico.sistema_colisao import SistemaColisao
from basico.evento import *

from jogo.labirinto.porta import Porta
from jogo.jogador.jogador import Jogador
from jogo.labirinto.labirinto import Labirinto
from jogo.mapa.mapa import Mapa

class Modo(Enum):
    Labirinto = 1
    Mapa = 2

class Jogo:
    def __init__(self, tela):
        self.__tela = tela

        self.__jogador = Jogador(
            self.tela, (tela.get_width()/2, tela.get_height()/2), (50*tela.get_width()/1960, 50*tela.get_height()/1080),
            DesenhavelRetangulo(self.tela, (0, 255, 0))
        )

        self.__labirinto = Labirinto(self.tela, self.jogador)
        self.__mapa = Mapa(self.tela, self.labirinto.salas)

        self.__modo = Modo.Labirinto

    def atualizar(self, eventos: list[Evento]):
        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_TAB:
                    if self.modo == Modo.Labirinto:
                        self.modo = Modo.Mapa
                    else:
                        self.modo = Modo.Labirinto

        if self.modo == Modo.Labirinto:
            self.labirinto.atualizar(eventos)
            if self.jogador.ativo:
                self.jogador.atualizar(eventos)
                    
            if self.jogador.vida <= 0:
                print('Fim de jogo')
                exit()
        else:
            self.mapa.atualizar(eventos)

    def desenhar(self):
        if self.modo == Modo.Labirinto:
            self.labirinto.desenhar()
            self.jogador.desenhar()
            self.desenharInformacoes()
        else:
            self.mapa.desenhar()

    def getColisores(self):
        colisores = []

        sala = self.labirinto.getSala()

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
        text_dano = DesenhavelTexto(self.tela, f'- dano: {self.jogador.dano_projeteis}', tamanho_fonte)
        text_dano.desenharSuperiorDireito((espaco_linha, espaco_linha*2))
        text_velocidade = DesenhavelTexto(self.tela, f'- velocidade: {self.jogador.velocidade_projeteis}', tamanho_fonte)
        text_velocidade.desenharSuperiorDireito((espaco_linha, espaco_linha*3))
        text_cadencia = DesenhavelTexto(self.tela, f'- cadencia: {self.jogador.cadencia_projeteis}', tamanho_fonte)
        text_cadencia.desenharSuperiorDireito((espaco_linha, espaco_linha*4))

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        self.__tela = tela

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def labirinto(self):
        return self.__labirinto

    @labirinto.setter
    def labirinto(self, labirinto):
        self.__labirinto = labirinto

    @property
    def mapa(self):
        return self.__mapa

    @mapa.setter
    def mapa_tela(self, mapa):
        self.__mapa = mapa

    @property
    def modo(self):
        return self.__modo

    @modo.setter
    def modo(self, modo):
        self.__modo = modo

