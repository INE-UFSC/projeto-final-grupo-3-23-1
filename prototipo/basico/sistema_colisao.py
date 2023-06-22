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
    def removerSobreposicoes(colisores: list[EntidadeTela]):
        for k in range(10):
            passos = {}

            solidos = [] 
            for colisor in colisores:
                if colisor.solido:
                    solidos.append(colisor)

            for i in range(len(solidos)):
                for j in range(i+1, len(solidos)):
                    a = solidos[i]
                    b = solidos[j]

                    if not (a.movel or b.movel):
                        continue

                    if not SistemaColisao.colidiu(a, b):
                        continue

                    delta_x = b.pos_tela[0] - a.pos_tela[0]
                    delta_y = b.pos_tela[1] - a.pos_tela[1]

                    tamanho = sqrt(delta_x**2 + delta_y**2)

                    if tamanho == 0:
                        vetor_ab = (0, 1)
                    else:
                        vetor_ab = (delta_x/tamanho, delta_y/tamanho)

                    vel = 1

                    if a.movel:
                        passo_atual = [0, 0]
                        passo_atual[0] += -vetor_ab[0]*vel
                        passo_atual[1] += -vetor_ab[1]*vel

                        if a in passos:
                            passos[a][0] += passo_atual[0]
                            passos[a][1] += passo_atual[1]
                        else:
                            passos[a] = passo_atual
                    if b.movel:
                        passo_atual = [0, 0]
                        passo_atual[0] += vetor_ab[0]*vel
                        passo_atual[1] += vetor_ab[1]*vel

                        if b in passos:
                            passos[b][0] += passo_atual[0]
                            passos[b][1] += passo_atual[1]
                        else:
                            passos[b] = passo_atual

            for ent in passos:
                nova_pos = list(ent.pos_tela)
                nova_pos[0] += passos[ent][0]
                nova_pos[1] += passos[ent][1]
                ent.pos_tela = tuple(nova_pos)

    @staticmethod
    def colocarDentroDaTela(colisores, tela):
        tela_rect = tela.get_rect()

        for colisor in colisores:
            rect = colisor.getRect()

            if rect.left < 0:
                rect.left = 0
            if rect.right > tela_rect.w:
                rect.right = tela_rect.w
            if rect.top < 0:
                rect.top = 0
            if rect.bottom > tela_rect.h:
                rect.bottom = tela_rect.h

            colisor.pos_tela = rect.center

