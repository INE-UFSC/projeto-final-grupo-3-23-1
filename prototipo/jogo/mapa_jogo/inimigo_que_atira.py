from .inimigo import Inimigo
from jogo.jogador.tiro import Tiro
import pygame as pg
from jogo.jogador.jogador import Jogador
import math

class inimigo_que_atira(Inimigo):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador, nivel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador)
        self.__nivel = nivel
        self.__tiros = []
        self.__cadencia = 0
        self.__forca_tiro = 0
        self.__tempo_ultimo_tiro = 0
        self.__valores_tiro = {0: (3000, 0.5, 7) ,
                               1: (2700, 0,5, 9) , 
                               2: (2450, 1, 10) ,
                               3: (2400, 1 , 11)}
        self.set_valores()
    
        self.__distancia_min_jogador = self.set_distancia_min_jogador()

    def set_valores(self):
        self.__cadencia = self.__valores_tiro[self.__nivel][0]
        self.__forca_tiro = self.__valores_tiro[self.__nivel][1]
        self.__velocidade_tiro = self.__valores_tiro[self.__nivel][2]

    def atualizar(self, eventos):
        # parte igual ao super:
        self.__colidindo = False
        #trata eventos:
        self.tratar_eventos(eventos)

        
        # dados de movimento:
        self.set_direction()
        self.set_velocidade()

        #limitando movimento

        while  self.get_distancia(self, self.alvo) < self.__distancia_min_jogador:
            self.movimentacao(-1)
        
        self.movimentacao()

        #verifica se tá vivo ainda
        self.verificar_vida()

        self.atualizar_meus_tiros(eventos)
        self.atirar()

    def atualizar_meus_tiros(self, eventos):

        for tiro in self.__tiros:
            tiro.atualizar(eventos)

        tiros_rem = []
        for t in self.__tiros:
            if not t.ativo:
                tiros_rem.append(t)

        for tiro in tiros_rem:
            self.__tiros.remove(tiro)

    def atirar(self):
        if pg.time.get_ticks() - self.__tempo_ultimo_tiro > self.__cadencia:
            self.__tempo_ultimo_tiro = pg.time.get_ticks()
            tiro_direcao = math.degrees(self.direction)
            self.__tiros.append(Tiro(self.tela, self.pos_tela,
                                   (self.tela.get_width()*20/1980, self.tela.get_height()*20/1080) , 
                                   tiro_direcao, self.__forca_tiro, self.__velocidade_tiro))

    def set_distancia_min_jogador(self):
        minha_diagonl = math.sqrt(self.dimensoes[0]**2 + self.dimensoes[1]**2)
        alvo_diagonal = math.sqrt(self.alvo.dimensoes[0]**2 + self.alvo.dimensoes[1]**2)

        d_min = (minha_diagonl + alvo_diagonal)/2 + 200

        return d_min
 

    def desenhar(self):
        super().desenhar()

        for t in self.__tiros:
            t.desenhar()
