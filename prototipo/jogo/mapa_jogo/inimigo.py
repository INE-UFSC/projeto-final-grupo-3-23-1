from basico.entidade_tela import EntidadeTela
from basico.evento import Evento, EventoColisao
from jogo.jogador.jogador import Jogador
import pygame as pg
from math import atan2, cos, sin, radians, pi

class Inimigo(EntidadeTela):

    def __init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador ):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_atual = self.pos_tela
        self.__dano = dano
        self.__direction = 0
        self.__nivel_velocidade = velocidade
        self.__velocidade = 0
        self.__vida = vida_inicial
        self.__alvo = jogador
        # Crie um objeto Clock para controlar o tempo
        #self.__clock = pg.time.Clock()
        self.__x = self.pos_tela[0]
        self.__y = self.pos_tela[1]

    @property
    def dano(self):
        return self.__dano
    
    def eventoColisao(self, colisor):
        from jogo.jogador.tiro import Tiro

        # se for tiro, perde vida:
        if type(colisor) == Tiro:
            self.__vida -= 1
            if self.__vida <= 0:
                self.ativo = False

    def atualizar(self,eventos):
         
        #trata eventos:
        self.tratar_eventos(eventos)
        
        # movimento:
        self.movimentacao()
        
        #verifica se tá vivo ainda
        self.verificar_vida()

    def tratar_eventos(self, eventos):
        #checa a lista de eventos:
        for evento in eventos:
            #se for um evento de colisão:
            if type(evento)== EventoColisao:
                #se um dos colisores for o self inimigo:
                if evento.colisores[0] == self:
                    self.eventoColisao(evento.colisores[1])
                if evento.colisores[1] == self:
                    self.eventoColisao(evento.colisores[0])
                    

    def movimentacao(self):
        self.set_direction()
        self.__x += self.speed * cos(radians(self.__direction))
        self.__y += self.speed * sin(radians(self.__direction))
     
        """
        #verificar se jogador está à esquerda ou à direita (x):
        if self.__alvo.pos_tela[0] < self.pos_tela[0]:
            self.pos_tela[0] -= 1
        elif self.__alvo.pos_tela[0] > self.pos_tela[0]:
            self.pos_tela[0] += 1

        #verificar se jogador está acima ou abaixo (y):
        if self.__alvo.pos_tela[1] < self.pos_tela[1]:
            self.pos_tela[1]-= 1
        elif self.__alvo.pos_tela[1] > self.pos_tela[1]:
            self.pos_tela[1] += 1"""

    def set_direction(self):
        alvo_x = self.__alvo.pos_tela[0]
        alvo_y = self.__alvo.pos_tela[1]

        angle = atan2(alvo_y-self.__y, alvo_x-self.__x) 
        self.__direction = int(180*angle/pi)

    def set_velocidade(self):
        niveis_velocidade = {1: 3, 2: 3, 3: 5, 4: 7, 5: 9}
        self.__velocidade = niveis_velocidade[self.__nivel_velocidade]

    # se a vida for 0, inimigo morre:
    def verificar_vida(self):
        if self.__vida == 0:
            self.ativo = False

                    

    
    




