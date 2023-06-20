import pygame as pg
from basico.entidade import Entidade
from basico.desenhavel import DesenhavelRetangulo
from jogo.mapa_jogo.sala_porta import *
from basico.evento import *

class MapaTela(Entidade):
    def __init__(self, tela, salas):
        self.tela = tela
        self.salas = salas
        self.marcadores = []
        self.marcador_ativo = 0

        self.desenhavel_sala = DesenhavelRetangulo(tela, (255, 255, 255))
        self.desenhavel_porta = DesenhavelRetangulo(tela, (0, 255, 0))
        self.desenhavel_marcador = DesenhavelRetangulo(tela, (0, 0, 255))

        self.dimens_tela = tela.get_size()

    def posParaSala(self, x, y):
        for i in range(self.getQtdSalas()):
            for j in range(self.getQtdSalas()):
                pos, dimens = self.getPosDimensSala(i, j)

                rect = pg.Rect((0, 0), dimens)
                rect.center = pos

                if rect.collidepoint(x, y):
                    return i, j
        return None

    def atualizar(self, eventos):
        for evento in eventos:
            if isinstance(evento, EventoApertouBotaoEsquerdo):
                pos_mouse = evento.pos_mouse

                pos = self.posParaSala(*pos_mouse)

                if pos is None:
                    continue

                i, j = pos

                marcador = None
                for m in self.marcadores:
                    if m.pos == (i, j):
                        marcador = m

                if marcador is None:
                    self.marcadores.append(Marcador((i, j)))
                else:
                    self.marcadores.remove(marcador)
            elif isinstance(evento, EventoApertouTecla):
                tecla = evento.tecla

                if tecla == pg.K_1:
                    Marcador.cor_i = 0
                elif tecla == pg.K_2:
                    Marcador.cor_i = 1
                elif tecla == pg.K_3:
                    Marcador.cor_i = 2

    def getTamanhos(self):
        qtd_salas = self.getQtdSalas()

        dimens_min = min(self.dimens_tela)
        unidade = dimens_min / (3*qtd_salas+1)

        tam_sala = 2*unidade
        tam_porta = unidade

        return tam_sala, tam_porta

    def getPosDimensPorta(self, i, j):
        tam_sala, tam_porta = self.getTamanhos()
        offset = tam_sala + tam_porta

        pos = {
            SalaPortaEsquerda:  (tam_porta/2 + j*offset, tam_porta + tam_sala/2 + i*offset),
            SalaPortaCima:     (tam_porta + tam_sala/2 + j*offset, tam_porta/2 + i*offset),
            SalaPortaDireita: (tam_porta + tam_sala + tam_porta/2 + j*offset, tam_porta + tam_sala/2 + i*offset),
            SalaPortaBaixo:    (tam_porta + tam_sala/2 + j*offset, tam_porta + tam_sala + tam_porta/2 + i*offset)
        }

        dimensoes = {
            SalaPortaDireita:  (tam_porta, tam_sala),
            SalaPortaEsquerda: (tam_porta, tam_sala),
            SalaPortaCima:     (tam_sala, tam_porta),
            SalaPortaBaixo:    (tam_sala, tam_porta)
        }

        for tipo_porta in pos:
            pos[tipo_porta] = self.centralizar(pos[tipo_porta]) 

        return pos, dimensoes

    def getQtdSalas(self):
        qtd_lin = len(self.salas)
        qtd_col = 0
        for linha in self.salas:
            if len(linha) > qtd_col:
                qtd_col = len(linha)
        qtd_salas = max(qtd_lin, qtd_col)

        return qtd_salas

    def getPosDimensSala(self, i, j):
        tam_sala, tam_porta = self.getTamanhos()
        offset = tam_sala + tam_porta

        pos = (tam_porta + tam_sala/2 + j*offset, tam_porta + tam_sala/2 + i*offset)
        dimens = (tam_sala, tam_sala)

        pos = self.centralizar(pos)

        return pos, dimens

    def centralizar(self, pos):
        nova_pos = list(pos)
        dimens_min = min(self.dimens_tela)
        
        if self.dimens_tela[0] != dimens_min:
            nova_pos[0] += (self.dimens_tela[0]-dimens_min)/2
        if self.dimens_tela[1] != dimens_min:
            nova_pos[1] += (self.dimens_tela[1]-dimens_min)/2

        return tuple(nova_pos)

    def getTiposPorta(self):
        return [SalaPortaCima, SalaPortaEsquerda, SalaPortaDireita, SalaPortaBaixo]

    def desenhar(self):
        """
        print(unidade)
        print(dimens_min)
        """

        qtd_salas = self.getQtdSalas()

        for i in range(qtd_salas):
            for j in range(qtd_salas):
                try:
                    self.salas[i][j]
                except:
                    continue

                def possui(sala, tipo_porta):
                    return any(isinstance(x, tipo_porta) for x in sala.sala_portas)

                for tipo_porta in self.getTiposPorta():
                    if possui(self.salas[i][j], tipo_porta):
                        pos, dimensoes = self.getPosDimensPorta(i, j)

                        self.desenhavel_porta.desenhar(
                            pos[tipo_porta],
                            dimensoes[tipo_porta]
                        )

                marcador = None
                for m in self.marcadores:
                    if m.pos == (i, j):
                        marcador = m

                pos, dimens = self.getPosDimensSala(i, j)

                """
                print('i, j =', i, j)
                print('pos =', pos)
                """

                if marcador is None:
                    self.desenhavel_sala.desenhar(
                        pos,
                        dimens
                    )
                else:
                    desenhavel = DesenhavelRetangulo(self.tela, marcador.cor)

                    desenhavel.desenhar(
                        pos,
                        dimens
                    )

class Marcador:
    cores = [(255, 255, 0), (0, 255, 255), (255, 0, 255)]
    cor_i = 0

    def __init__(self, pos):
        self.pos = pos
        self.cor = self.cores[self.cor_i]

