from math import sqrt
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

    @staticmethod
    def atualizarSolidos(colisores: list[EntidadeTela]):
        for i in range(len(colisores)):
            for j in range(i+1, len(colisores)):
                a = colisores[i]
                b = colisores[j]

                if not (a.solido and b.solido):
                    continue

                if not (a.movel or b.movel):
                    continue

                for k in range(10):
                    if not SistemaColisao.colidiu(a, b):
                        break

                    delta_x = b.pos_tela[0] - a.pos_tela[0]
                    delta_y = b.pos_tela[1] - a.pos_tela[1]

                    tamanho = sqrt(delta_x**2 + delta_y**2)

                    if tamanho == 0:
                        vetor = (0, 1)
                    else:
                        vetor = (delta_x/tamanho, delta_y/tamanho)

                    vel = 1

                    if a.movel:
                        nova_pos = list(a.pos_tela)
                        nova_pos[0] += -vetor[0]*vel
                        nova_pos[1] += -vetor[1]*vel
                        a.pos_tela = tuple(nova_pos)
                    if b.movel:
                        nova_pos = list(b.pos_tela)
                        nova_pos[0] += vetor[0]*vel
                        nova_pos[1] += vetor[1]*vel
                        b.pos_tela = tuple(nova_pos)

