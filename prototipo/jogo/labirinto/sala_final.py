from .sala import Sala
from .jogador_sala_final import JogadorSalaFinal
from basico.evento import EventoColisao
from jogo.jogador.jogador import Jogador
import pygame as pg
from menu.botao import Botao
from basico.desenhavel import DesenhavelRetangulo

class SalaFinal(Sala):
    def __init__(self, tela, desenhavel, jogador):
        super().__init__(desenhavel)
        self.__jogador_sala_final = JogadorSalaFinal(tela, jogador)
        self.__modo = 1
        self.__jogador_dimensoes = jogador.dimensoes
        self.__fonte = pg.font.SysFont("Comic Sans MS", int(40/1080 * tela.get_height()))
        self.__superficies = []
        self.criarMensagemFinal()
        self.botoes = [Botao(tela, (6*tela.get_width()/8, 15*tela.get_height()/16),
                                  (tela.get_width()/4, tela.get_height()/16),
                                  DesenhavelRetangulo(tela, (128, 64, 64)),
                                  'Sair', 40/1080),
                        Botao(tela, (6*tela.get_width()/8, 13*tela.get_height()/16),
                                  (tela.get_width()/4, tela.get_height()/16),
                                  DesenhavelRetangulo(tela, (128, 64, 64)),
                                  'Voltar a tela inicial', 40/1080)]
        self.tela = tela
    
    def criarMensagemFinal(self):
        mensagem = 'Felicitações!\nVocê finalizou sua jornada de autoconhecimento\ne chegou ao centro de seu “eu”'
        linhas = mensagem.split('\n')
        for linha in linhas:
            self.__superficies.append(self.__fonte.render(linha, True, (255, 255, 255)))
        self.__superficies.reverse()


    def desenharResto(self):
        self.__jogador_sala_final.desenhar()
        if self.__modo == 2:
            espaco_linha = self.__fonte.get_linesize()
            altura = self.tela.get_height()/2 - (self.__jogador_dimensoes[1] + self.tela.get_height()/8)
            alturas = []
            for s in self.__superficies:
                alturas.append(altura)
                s_rect = s.get_rect()
                s_rect.center = (self.tela.get_width()/2, altura)
                self.tela.blit(s, s_rect)
                altura -= espaco_linha
            for botao in self.botoes:
                botao.desenhar()
    
    def atualizarResto(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoColisao):
                if evento.possui(self.__jogador_sala_final):
                    if evento.possuiTipo(Jogador):
                        self.__modo = 2
        for botao in self.botoes:
            botao.atualizar(eventos)

    def getColisores(self):
        colisores = super().getColisores()
        colisores.append(self.__jogador_sala_final)
        return colisores