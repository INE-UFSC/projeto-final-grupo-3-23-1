from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo, DesenhavelTexto, DesenhavelImagem
from basico.evento import EventoApertouBotaoEsquerdo, EventoColisao, EventoApertouTecla
from .caixa_de_resposta import CaixaDeResposta
import pygame as pg
import os
from enum import Enum
from menu.botao import Botao

class ModoComputador(Enum):
    Escrever = 1
    ChecarResposta = 2
    Acertou = 3
    Errou = 4

class Computador(EntidadeTela):
    def __init__(self, tela, desenhavel, dimen_pc, desenhavel_puzzle,
                 desenhavel_acertou, desenhavel_errou, resposta, jogador):
        super().__init__(tela,
                        (tela.get_width()/2, tela.get_height()/2),
                        dimen_pc, desenhavel)
        self.__im_puzzle = desenhavel_puzzle
        self.__im_ganhou = desenhavel_acertou
        self.__im_perdeu = desenhavel_errou
        self.__resposta = resposta
        self.__resolvido = False
        self.__modo = ModoComputador.Escrever
        self.__jogador = jogador
        self.__ligado = False

        dimens_botao_tentar_dnv = (self.telaW()*3/16, self.telaH()/16)
        dimens_botao_responder = (self.telaW()/10, self.telaH()/20)
        self.__botao_responder = Botao(tela, (self.telaW()*2.7/4, self.telaH()*3/5), 
                                       dimens_botao_responder,
                                       DesenhavelImagem(tela, os.path.join('imagens', 'botoes', 'responder.png'),
                                                        dimens_botao_responder), '')
        self.__botao_tentar_dnv = Botao(tela, (self.telaW()/2, self.telaH()*3/5), 
                                        dimens_botao_tentar_dnv,
                                       DesenhavelImagem(tela, os.path.join('imagens', 'botoes', 'tentar_novamente.png'),
                                        dimens_botao_tentar_dnv), '')

        self.__caixa_resposta = CaixaDeResposta(tela, (self.telaW()*1.8/4, self.telaH()*3/5),
                                                (self.telaW()/3, self.telaH()/30))

        
    
    def atualizar(self, eventos):
        self.tentarLigar(eventos)
        if self.__ligado:
            if self.__modo == ModoComputador.Escrever:
                self.__caixa_resposta.atualizar(eventos)
                if self.__caixa_resposta.selecionada:
                    for evento in eventos:
                        if isinstance(evento, EventoApertouTecla):
                            if evento.tecla == pg.K_RETURN or evento.tecla == pg.K_KP_ENTER:
                                self.__modo = ModoComputador.ChecarResposta
                    self.__jogador.ativo = False
                else:
                    self.__jogador.ativo = True
                self.__botao_responder.atualizar(eventos)
                if self.__botao_responder.apertou:
                    self.__modo = ModoComputador.ChecarResposta
                    self.__botao_responder.resetApertou()

            elif self.__modo == ModoComputador.ChecarResposta:
                self.__jogador.ativo = True
                if self.__caixa_resposta.chute.strip().lower() == self.__resposta:
                    self.__resolvido = True
                    self.__modo = ModoComputador.Acertou
                else:
                    self.__modo = ModoComputador.Errou

            elif self.__modo == ModoComputador.Errou:
                self.__botao_tentar_dnv.atualizar(eventos)
                if self.__botao_tentar_dnv.apertou:
                    self.__modo = ModoComputador.Escrever
                    self.__caixa_resposta.chute = ''
                    self.__botao_tentar_dnv.resetApertou()

    def desenhar(self):
        super().desenhar()
        if self.__ligado:
            self.__im_puzzle.desenhar((self.telaW()/2, self.telaH()/2))
            if self.__modo == ModoComputador.Escrever:
                self.__caixa_resposta.desenhar()
                self.__botao_responder.desenhar()

            elif self.__modo == ModoComputador.Acertou:
                self.__im_ganhou.desenhar((self.telaW()/2, self.telaH()/2))
    
            elif self.__modo == ModoComputador.Errou:
                self.__im_perdeu.desenhar((self.telaW()/2, self.telaH()/2))
                self.__botao_tentar_dnv.desenhar()

    def tentarLigar(self, eventos):
        for evento in eventos:
            from jogo.jogador.jogador import Jogador
            if isinstance(evento, EventoColisao):
                if evento.possui(self) and evento.possuiTipo(Jogador):
                    self.__ligado = True
            else:
                self.__ligado = False

    @property
    def resolvido(self):
        return self.__resolvido