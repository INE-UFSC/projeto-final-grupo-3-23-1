from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo, DesenhavelTexto
from basico.evento import EventoApertouBotaoEsquerdo, EventoApertouTecla
import pygame as pg

class CaixaDeResposta(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes):
        self.__cor_caixa_nao_selecionada = (0, 0, 0)
        super().__init__(tela, pos_tela, dimensoes,
                         DesenhavelRetangulo(tela, self.__cor_caixa_nao_selecionada, dimensoes))
        self.__selecionada = False
        self.__chute = ''
    
    def atualizar(self, eventos):
        for evento in eventos:
            self.selecionarCaixa(evento)
            if self.selecionada:
                self.escreverNaCaixa(evento)

    def selecionarCaixa(self, evento):
        if isinstance(evento, EventoApertouBotaoEsquerdo):
            if self.getRect().collidepoint(evento.pos_mouse):
                self.selecionada = True
            else:
                self.selecionada = False

    def escreverNaCaixa(self, evento):
        if isinstance(evento, EventoApertouTecla):
            if evento.tecla == pg.K_BACKSPACE:
                self.chute = self.chute[:-1]
            elif evento.tecla != pg.K_RETURN and evento.tecla != pg.K_KP_ENTER:
                self.chute += evento.unicode
                chute = DesenhavelTexto(self.tela, self.chute)
                if chute.rect.width > self.getRect().width:
                    self.chute = self.__chute[:-1]

    def desenhar(self):
        if self.__selecionada:
            self.desenhavel.cor = (128, 128, 128)
        else:
            self.desenhavel.cor = self.__cor_caixa_nao_selecionada
        super().desenhar()

        if self.__chute == '':
            text = DesenhavelTexto(self.tela,'Digite sua resposta')
        else:
            text = DesenhavelTexto(self.tela, self.chute)
        text.desenharSuperiorDireito(self.getRect())

    @property
    def chute(self):
        return self.__chute

    @chute.setter
    def chute(self, chute):
        self.__chute = chute

    @property
    def selecionada(self):
        return self.__selecionada

    @selecionada.setter
    def selecionada(self, sel):
        self.__selecionada = sel
