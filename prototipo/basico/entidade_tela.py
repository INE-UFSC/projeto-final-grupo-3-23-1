from abc import ABC
import pygame as pg

from basico.entidade import Entidade
from basico.sistema_colisao import SistemaColisao
from basico.desenhavel import Desenhavel

class EntidadeTela(Entidade, ABC):
    sistema_colisao = SistemaColisao()

    def __init__(
        self,
        tela: pg.Surface,
        pos_tela: tuple[int, int],
        dimensoes: tuple[int, int],
        desenhavel: Desenhavel
    ):
        super().__init__(tela)

        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel

        self.sistema_colisao.adicionarColisor(self)

        self.ativo = True

    def desenhar(self):
        self.desenhavel.desenhar(self.tela, self.pos_tela, self.dimensoes)

