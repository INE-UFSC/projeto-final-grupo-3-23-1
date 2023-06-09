import pygame as pg

from basico.evento import EventoColisao
from basico.entidade_tela import EntidadeTela

class SistemaColisao:
    @staticmethod
    def colidiu(a, b):
        rect_a = a.getRect()
        rect_b = b.getRect()

        return rect_a.colliderect(rect_b)
        
    @staticmethod
    def getColisoes(colisores: list[EntidadeTela]):
        eventos = []
        for i in range(len(colisores)):
            for j in range(i+1, len(colisores)):
                a = colisores[i]
                b = colisores[j]
                if SistemaColisao.colidiu(a, b):
                    eventos.append(EventoColisao(a, b))
        return eventos

