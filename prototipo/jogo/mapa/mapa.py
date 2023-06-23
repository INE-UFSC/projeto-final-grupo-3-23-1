import pygame as pg
from basico.entidade import Entidade
from basico.desenhavel import DesenhavelRetangulo
from jogo.labirinto.sala_porta import *
from basico.evento import *

class Mapa(Entidade):
    def __init__(self, tela, salas):
        self.__tela = tela
        self.__salas = salas
        self.__marcadores = []
        self.__marcador_ativo = 0

        self.__dimens_tela = tela.get_size()

        self.__cor_sala = (255, 255, 255)
        self.__cor_porta = (0, 255, 0)

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
                        pos, dimens = self.getPosDimensPorta(i, j)

                        desenhavel = DesenhavelRetangulo(self.tela, self.cor_porta, dimens)
                        desenhavel.desenhar(pos[tipo_porta])

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
                    desenhavel = DesenhavelRetangulo(self.tela, self.cor_sala, dimens)
                else:
                    desenhavel = DesenhavelRetangulo(self.tela, marcador.cor, dimens)

                desenhavel.desenhar(pos)

    def posParaSala(self, x, y):
        for i in range(self.getQtdSalas()):
            for j in range(self.getQtdSalas()):
                pos, dimens = self.getPosDimensSala(i, j)

                rect = pg.Rect((0, 0), dimens)
                rect.center = pos

                if rect.collidepoint(x, y):
                    return i, j
        return None


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


    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        self.__tela = tela

    @property
    def salas(self):
        return self.__salas

    @salas.setter
    def salas(self, salas):
        self.__salas = salas

    @property
    def marcadores(self):
        return self.__marcadores

    @marcadores.setter
    def marcadores(self, marcadores):
        self.__marcadores = marcadores

    @property
    def marcador_ativo(self):
        return self.__marcador_ativo

    @marcador_ativo.setter
    def marcador_ativo(self, marcador_ativo):
        self.__marcador_ativo = marcador_ativo

    @property
    def dimens_tela(self):
        return self.__dimens_tela

    @dimens_tela.setter
    def dimens_tela(self, dimens_tela):
        self.__dimens_tela = dimens_tela

    @property
    def cor_sala(self):
        return self.__cor_sala

    @cor_sala.setter
    def cor_sala(self, cor_sala):
        self.__cor_sala = cor_sala

    @property
    def cor_porta(self):
        return self.__cor_porta

    @cor_porta.setter
    def cor_porta(self, cor_porta):
        self.__cor_porta = cor_porta

class Marcador:
    cores = [(255, 255, 0), (0, 255, 255), (255, 0, 255)]
    cor_i = 0

    def __init__(self, pos):
        self.__pos = pos
        self.__cor = self.cores[self.cor_i]

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

