from .inimigo import Inimigo
from jogo.jogador.projetil import Projetil
import pygame as pg
from jogo.jogador.jogador import Jogador
import math

class InimigoQueAtira(Inimigo):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador, nivel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador)
        self.__nivel = nivel
        self.__projeteis = []
        self.__cadencia = 0
        self.__forca_tiro = 0
        self.__tempo_ultimo_tiro = 0
        self.__tempo_ultimo_movimento = 0

        self.__valores_projetil = {0: (3000, 0.5, 7) ,
                               1: (2700, 0,5, 9) , 
                               2: (2450, 1, 10) ,
                               3: (2400, 1 , 11)}
         # Crie um objeto Clock para controlar o tempo
        self.__clock = pg.time.Clock()
        self.set_valores()
    
        self.__distancia_min_jogador = self.set_distancia_min_jogador()

    def set_valores(self):
        self.__cadencia = self.__valores_projetil[self.__nivel][0]
        self.__forca_projetil = self.__valores_projetil[self.__nivel][1]
        self.__velocidade_projetil = self.__valores_projetil[self.__nivel][2]

    def atualizar(self, eventos):
        self.__pode_mexer = True
        # parte igual ao super:
        self.__colidindo = False
        #trata eventos:
        self.tratar_eventos(eventos)

        # dados de movimento:
        self.set_direction()
        self.set_velocidade()

        #limitando movimento
        self.verificar_movimentacao()
        """
        if self.get_distancia(self, self.alvo) < self.__distancia_min_jogador:
            #self.movimentacao(-1)
            self.se_afastar()
            self.__pode_mexer = False"""

        if self.__pode_mexer:
            self.movimentacao()

        #verifica se tá vivo ainda
        self.verificar_vida()

        self.atualizar_meus_tiros(eventos)
        self.atirar()

    def se_afastar(self):
        periodo_afastamento = 10
        if pg.time.get_ticks() - self.__tempo_ultimo_movimento > periodo_afastamento:
            self.__tempo_ultimo_movimento = pg.time.get_ticks()
            self.movimentacao(-1)

    def atualizar_meus_tiros(self, eventos):

        for projetil in self.__projeteis:
            projetil.atualizar(eventos)

        projeteis_rem = []
        for p in self.__projeteis:
            if not p.ativo:
                projeteis_rem.append(p)

        for projetil in projeteis_rem:
            self.__projeteis.remove(projetil)

    def atirar(self):
        if pg.time.get_ticks() - self.__tempo_ultimo_tiro > self.__cadencia:
            self.__tempo_ultimo_tiro = pg.time.get_ticks()
            projetil_direcao = math.degrees(self.direction)
            self.__projeteis.append(Projetil(self.tela, self.pos_tela,
                                   (self.telaW()*20/1980, self.telaH()*20/1080) , 
                                   projetil_direcao, True, self.__forca_projetil, self.__velocidade_projetil))

    def set_distancia_min_jogador(self):
        minha_diagonl = math.sqrt(self.dimensoes[0]**2 + self.dimensoes[1]**2)
        alvo_diagonal = math.sqrt(self.alvo.dimensoes[0]**2 + self.alvo.dimensoes[1]**2)

        d_min = (minha_diagonl + alvo_diagonal)/2 + 200

        return d_min
 
    def verificar_movimentacao(self):
        distancia_atual = self.get_distancia(self, self.alvo)
        distancia_minima = int(self.__distancia_min_jogador)
        for i in range (distancia_minima - 1, distancia_minima +1):
            if distancia_atual < i: 
                self.se_afastar()
                #print("distancia atual:", distancia_atual, "distancia minima:",  distancia_minima, "i:", i)
                self.__pode_mexer = False

    def desenhar(self):
        super().desenhar()

        for t in self.__projeteis:
            t.desenhar()

    def getColisores(self):
        return self.projeteis
    

    @property
    def projeteis(self):
        return self.__projeteis