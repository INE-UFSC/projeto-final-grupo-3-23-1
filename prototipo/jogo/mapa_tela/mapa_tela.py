import pygame as pg
from basico.entidade import Entidade
from basico.desenhavel import DesenhavelRetangulo
from jogo.mapa_jogo.sala_porta import *

class MapaTela(Entidade):
    def __init__(self, tela, salas):
        self.tela = tela
        self.salas = salas
        self.marcadores = []

        self.desenhavel_sala = DesenhavelRetangulo(tela, (255, 255, 255))
        self.desenhavel_porta = DesenhavelRetangulo(tela, (0, 255, 0))
        self.desenhavel_marcador = DesenhavelRetangulo(tela, (0, 0, 255))

        self.dimens_mapa = tela.get_size()

    def atualizar(eventos):
        pass
        """
        for evento in eventos:
            if isinstance(evento, EventoClique):
                pos = evento.pos

                qtd_lin = len(self.salas)
                qtd_col = len(self.salas[0])

                for i in range(qtd_lin):
                    for j in range(qtd_col):
                        x0 = expessura_porta + j*(comprimento_sala + expessura_porta)
                        y0 = expessura_porta + i*(comprimento_sala + expessura_porta)

                        if x0 <= pos[0] <= x0 + comprimento_sala \
                                and y0 <= pos[1] <= y0 + comprimento_sala:
                            marcador_rem = None
                            for marcador in self.marcadores:
                                if marcador.pos == pos:
                                    marcador_rem = marcador

                            if marcador_rem is None:
                                self.marcadores.append(Marcador((i, j)))
                            else:
                                self.marcadores.remove(marcador)
        """

    def desenhar(self):
        qtd_lin = len(self.salas)
        qtd_col = 0
        for linha in self.salas:
            if len(linha) > qtd_col:
                qtd_col = len(linha)
        qtd_salas = max(qtd_lin, qtd_col)

        dimens_min = min(self.dimens_mapa)
        unidade = dimens_min / (3*qtd_salas+1)

        """
        print(unidade)
        print(dimens_min)
        """

        for i in range(qtd_salas):
            for j in range(qtd_salas):
                try:
                    self.salas[i][j]
                except:
                    continue

                offset_x = 3*unidade
                offset_y = 3*unidade

                tam_sala = 2*unidade
                tam_porta = unidade

                self.desenhavel_sala.desenhar(
                    (tam_porta + tam_sala/2 + i*offset_x, tam_porta + tam_sala/2 + j*offset_y),
                    (2*unidade, 2*unidade)
                )

                pos = {
                    SalaPortaEsquerda:  (tam_porta/2 + i*offset_x, tam_porta + tam_sala/2 + j*offset_y),
                    SalaPortaCima:     (tam_porta + tam_sala/2 + i*offset_x, tam_porta/2 + j*offset_y),
                    SalaPortaDireita: (tam_porta + tam_sala + tam_porta/2 + i*offset_x, tam_porta + tam_sala/2 + j*offset_y),
                    SalaPortaBaixo:    (tam_porta + tam_sala/2 + i*offset_x, tam_porta + tam_sala + tam_porta/2 + j*offset_y)
                }

                dimensoes = {
                    SalaPortaDireita:  (tam_porta, tam_sala),
                    SalaPortaEsquerda: (tam_porta, tam_sala),
                    SalaPortaCima:     (tam_sala, tam_porta),
                    SalaPortaBaixo:    (tam_sala, tam_porta)
                }

                def possui(sala, tipo_porta):
                    return any(isinstance(x, tipo_porta) for x in sala.sala_portas)

                for tipo_porta in pos:
                    if possui(self.salas[i][j], tipo_porta):
                        self.desenhavel_porta.desenhar(
                            pos[tipo_porta],
                            dimensoes[tipo_porta]
                        )

                for marcador in self.marcadores:
                    pos = (tam_porta + tam_sala/2 + i*offset_x, tam_porta + tam_sala/2 + j*offset_y),
                    dimens = (2*unidade, 2*unidade)

                    if marcador.pos == (i, j):
                        self.desenhavel_marcador.desenhar(
                            pos,
                            dimens
                        )
                    else:
                        self.desenhavel_sala.desenhar(
                            pos,
                            dimens
                        )

class Marcador:
    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    cor_i = 0

    def __init__(self, pos):
        self.pos = pos
        self.cor = self.cores[self.cor_i]

        self.cor_i = (self.cor_i + 1) % len(self.cores)

