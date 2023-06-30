import pygame as pg
from pygame.locals import *

from enum import Enum

from basico.entidade_tela import EntidadeTela, Entidade
from basico.desenhavel import DesenhavelRetangulo, DesenhavelImagem
from basico.sistema_colisao import SistemaColisao
from basico.evento import *
from tela_pause.tela_pause import TelaPause
from jogo.labirinto.porta import Porta
from jogo.jogador.jogador import Jogador
from jogo.labirinto.labirinto import Labirinto
from jogo.tela_game_over import TelaGameOver
from jogo.mapa.mapa import Mapa
from tela_pause.tela_pause import ModoPause

class ModoJogo(Enum):
    Labirinto = 1
    Mapa = 2
    Pause = 3
    GameOver = 4
    IrParaMenu = 5

class Jogo(Entidade):
    def __init__(self, tela):
        super().__init__(tela)

        dimens_jogador = (50*self.telaW()/1960, 50*self.telaH()/1080)
        dimens_imagem = (3*dimens_jogador[0], 2*dimens_jogador[1])

        imagem_jogador = 'imagens/jogador.jpg'
        self.__jogador = Jogador(
            self.tela, (self.telaW()/2, self.telaH()/2), dimens_jogador,
            DesenhavelImagem(self.tela, imagem_jogador, dimens_imagem, 'white')
#            DesenhavelRetangulo(self.tela, (0, 255, 0), dimens_jogador)
        )

        self.__labirinto = Labirinto(self.tela, self.jogador)
        self.__mapa = Mapa(self.tela, self.labirinto.salas, imagem_jogador)
        self.__pause = TelaPause(self.tela)
        self.__tela_game_over = TelaGameOver(self.tela)
        self.__modo = ModoJogo.Labirinto


    def atualizar(self, eventos: list[Evento]):
        for evento in eventos:
            if isinstance(evento, EventoApertouTecla):
                if evento.tecla == pg.K_TAB:
                    if self.modo == ModoJogo.Labirinto:
                        self.modo = ModoJogo.Mapa
                    else:
                        self.modo = ModoJogo.Labirinto

                if evento.tecla == pg.K_ESCAPE:
                    if self.modo == ModoJogo.Labirinto:
                        self.modo = ModoJogo.Pause

                    elif self.modo == ModoJogo.Pause:
                        if self.pause.modo == ModoPause.PausePrincipal:
                            self.pause.reset()
                            self.modo = ModoJogo.Labirinto

        if self.modo == ModoJogo.Labirinto:
            self.labirinto.atualizar(eventos)
            if self.jogador.ativo:
                self.jogador.atualizar(eventos)
                    
            if self.jogador.vida <= 0:
                self.modo = ModoJogo.GameOver

            if self.labirinto.sala_final.botoes[0].apertou:
                self.labirinto.sala_final.botoes[0].resetApertou()
                pg.quit()
                exit()

        elif self.modo == ModoJogo.Pause:
            self.pause.atualizar(eventos)

            if self.pause.modo == ModoPause.SairPause:
                print("saindo do pause")
                self.pause.reset()
                self.modo = ModoJogo.Labirinto
        
            if self.pause.modo == ModoPause.Menu:
                print("modo jogo = ir para menu")
                self.modo = ModoJogo.IrParaMenu

                

        elif self.modo == ModoJogo.Mapa:
            self.mapa.atualizar(eventos)

        elif self.modo == ModoJogo.GameOver:
            self.tela_game_over.atualizar(eventos)
            if self.__tela_game_over.botoes[0].apertou:
                self.__tela_game_over.botoes[0].resetApertou()
                pg.quit()
                exit()

    def desenhar(self):
        if self.modo == ModoJogo.Labirinto:
            self.labirinto.desenhar()
            self.jogador.desenhar()
            self.desenharInformacoes()
        
        elif self.modo == ModoJogo.Pause:
            self.pause.desenhar()
        elif self.modo == ModoJogo.Mapa:
            self.mapa.desenhar()
        elif self.modo == ModoJogo.GameOver:
            self.__tela_game_over.desenhar()

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

    @property
    def pause(self):
        return self.__pause

    @property
    def tela_game_over(self):
        return self.__tela_game_over
