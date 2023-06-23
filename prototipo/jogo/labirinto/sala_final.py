from .sala import Sala
from .jogador_sala_final import JogadorSalaFinal
from basico.evento import EventoColisao
from jogo.jogador.jogador import Jogador
import pygame as pg
from menu.botao import Botao
from basico.desenhavel import DesenhavelRetangulo, DesenhavelTexto

class SalaFinal(Sala):
    def __init__(self, tela, desenhavel, jogador):
        super().__init__(tela, desenhavel)
        self.__jogador_sala_final = JogadorSalaFinal(tela, jogador)
        self.__modo = 1
        self.__jogador_dimensoes = jogador.dimensoes
        self.__superficies = []
        self.botoes = [Botao(tela, (6*self.telaW()/8, 15*self.telaH()/16),
                                  (self.telaW()/4, self.telaH()/16),
                                  DesenhavelRetangulo(tela, (128, 64, 64)),
                                  'Sair', 40/1080),
                        Botao(tela, (6*self.telaW()/8, 13*self.telaH()/16),
                                  (self.telaW()/4, self.telaH()/16),
                                  DesenhavelRetangulo(tela, (128, 64, 64)),
                                  'Voltar a tela inicial', 40/1080)]
        self.tela = tela
    
        #criando mensagem final:
        mensagem = 'Felicitações!\nVocê finalizou sua jornada de autoconhecimento\ne chegou ao centro de seu “eu”'
        linhas = mensagem.split('\n')
        for linha in linhas:
            self.__superficies.append(DesenhavelTexto(tela, linha))
        self.__superficies.reverse()


    def desenharResto(self):
        self.__jogador_sala_final.desenhar()
        if self.__modo == 2:
            altura = self.telaH()/2 - (self.__jogador_dimensoes[1] + self.telaH()/8)
            for s in self.__superficies:
                s.desenhar((self.telaW()/2, altura))
                altura -= s.espaco_linha
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