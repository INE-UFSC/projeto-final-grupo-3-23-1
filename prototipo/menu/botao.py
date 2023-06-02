from basico.entidade_tela import EntidadeTela
from basico.evento import *


class Botao(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel

        self.apertou = False
    def desenhar(self):
        self.desenhavel.desenhar()

    def atualizar(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoColisao):
                self.apertou = True

    def resetApertou(self):
        self.apertou = False

