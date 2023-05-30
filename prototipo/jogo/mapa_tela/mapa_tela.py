import pygame as pg
from basico.entidade import Entidade

class MapaTela(Entidade):
    def __init__(self, tela, salas):
        self.tela = tela
        self.salas = salas
        self.marcadores = []

        self.comprimento_sala = 20
        self.expessura_porta = 10 

    def atualizar(eventos):
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

    def desenhar():
        qtd_lin = len(self.salas)
        qtd_col = len(self.salas[0])


        cor_porta = (255, 255, 255)

        cor_porta_aberta = (0, 0, 255)
        cor_porta_fechada = (255, 0, 0)

        x = 0
        y = 0
        for i, linha in enumerate(self.salas):
            for j, sala in enumerate(linha):
                def tem(sala, tipo_porta):
                    return any(isinstance(x, tipo_porta) for x in sala.sala_portas)

                cor_parede = (0, 255, 0)

                if not tem(sala, SalaPortaCima):
                    pg.draw.rect(tela, cor_parede, (
                        x, y, 
                        self.comprimento_sala, self.expessura_porta
                    ))

                if not tem(sala, SalaPortaBaixo):
                    pg.draw.rect(tela, cor_parede, (
                        x, y + self.expessura_porta + self.comprimento_sala,
                        self.comprimento_sala, self.expessura_porta
                    ))

                if not tem(sala, SalaPortaEsquerda):
                    pg.draw.rect(tela, cor_parede, (
                        x, y,
                        self.expessura_porta, self.comprimento_sala
                    ))

                if not tem(sala, SalaPortaDireita):
                    pg.draw.rect(tela, cor_parede, (
                        x + self.expessura_porta + self.comprimento_sala, y
                        self.expessura_porta, self.comprimento_sala
                    ))

                for marcador in self.marcadores:
                    cor = (0, 0, 0)
                    if marcador.pos == (i, j):
                        cor = marcador.cor

                    pg.draw.rect(tela, cor, (
                        x + self.expessura_porta, y + self.expessura_porta,
                        self.comprimento_sala, self.comprimento_sala
                    ))

class Marcador:
    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    cor_i = 0

    def __init__(self, pos):
        self.pos = pos
        self.cor = self.cores[self.cor_i]

        self.cor_i = (self.cor_i + 1) % len(self.cores)

