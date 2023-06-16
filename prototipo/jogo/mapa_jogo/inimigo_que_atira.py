from mapa_jogo.inimigo import Inimigo
from jogo.jogador.tiro import Tiro
import pygame as pg
from jogo.jogador.jogador import Jogador

class inimigo_que_atira(Inimigo):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador, nivel):
        super().__init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador)
        self.__nivel = nivel
        self.__tiros = []
        self.__cadencia = 0
        self.__forca_tiro = 0
        self.__tempo_ultimo_tiro = 0
        self.__valores_tiro = {0: (400, 0.5, 7) ,
                               1: (500, 0,5, 9) , 
                               2: (500, 1, 10) ,
                               3: (600, 1 , 11)}
        self.set_valores()

    def set_valores(self):
        self.__cadencia = self.__valores_tiro[self.__nivel][0]
        self.__forca_tiro = self.__valores_tiro[self.__nivel][1]
        self.__velocidade_tiro = self.__valores_tiro[self.__nivel][2]

    def atualizar(self, eventos):
        super().atualizar(eventos)
        self.atualizar_meus_tiros(eventos)

    def atualizar_meus_tiros(self, eventos):
        for tiro in self.tiros:
            tiro.atualizar(eventos)

        tiros_rem = []
        for t in self.tiros:
            if not t.ativo:
                tiros_rem.append(t)

        for tiro in tiros_rem:
            self.tiros.remove(tiro)

    def atirar(self):
        if pg.time.get_ticks() - self.__tempo_ultimo_tiro > self.__cadencia:
            self.__tempo_ultimo_tiro = pg.time.get_ticks()
            self.__tiros.append(Tiro(self.tela, self.pos_tela,
                                   (self.tela.get_width()*20/1980, self.tela.get_height()*20/1080),
                                    self.__direction, self.__forca_tiro, self.__velocidade_tiro))


    def desenhar(self):
        super().desenhar()

        for t in self.tiros:
            t.desenhar()
