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
            nova_pos = list(colisor.pos_tela)

            x, y = colisor.pos_tela
            w, h = colisor.dimensoes

            if x - w/2 < 0:
                nova_pos[0] = w/2
            if x + w/2 > tela_rect.w:
                nova_pos[0] = tela_rect.w - w/2
            if y - h/2 < 0:
                nova_pos[1] = h/2
            if y + h/2 > tela_rect.h:
                nova_pos[1] = tela_rect.h - h/2

            colisor.pos_tela = tuple(nova_pos)

