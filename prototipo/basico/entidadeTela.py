from abc import ABC
import pygame as pg

from basico.entidade import Entidade

class SistemaColisao:
    def __init__(self):
        self.entidades = []

    def adicionarEntidadeTela(self, entidade):
        self.entidades.append(entidade)

    @staticmethod
    def colidiu(a, b):
        rect_a = pg.Rect(*a.pos_tela, *a.dimensoes) 
        rect_b = pg.Rect(*b.pos_tela, *b.dimensoes) 

        return rect_a.colliderect(rect_b)
        
    def checarColisoes(self):
        for i in range(len(self.entidades)):
            for j in range(i+1, len(self.entidades)):
                a = self.entidades[i]
                b = self.entidades[j]
                if self.colidiu(a, b):
                    a.eventoColisao(b)
                    b.eventoColisao(a)

    def removerNaoAtivos(self):
        rems = []
        for entidade in self.entidades:
            if not entidade.ativo:
                rems.append(entidade)
        
        for rem in rems:
            self.entidades.remove(rem)

class EntidadeTela(Entidade, ABC):
    sistema_colisao = SistemaColisao()

    def __init__(
        self,
        tela,
        pos_tela,
        dimensoes,
        desenhavel
    ):
        super().__init__(tela)

        self.pos_tela = pos_tela
        self.dimensoes = dimensoes
        self.desenhavel = desenhavel

        self.sistema_colisao.adicionarEntidadeTela(self)

        self.ativo = True

    def eventoColisao(self, outro):
        pass

    def desenhar(self):
        self.desenhavel.desenhar(self.tela, self.pos_tela, self.dimensoes)

class DesenhavelRetangulo:
    def __init__(self, cor):
        self.cor = cor

    def desenhar(self, tela, pos_tela, dimensoes):
        pg.draw.rect(tela, self.cor, (*pos_tela, *dimensoes))

