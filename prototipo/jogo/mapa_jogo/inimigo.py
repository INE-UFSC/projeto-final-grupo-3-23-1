from basico.entidade_tela import EntidadeTela
from basico.evento import Evento, EventoColisao
from jogo.jogador.jogador import Jogador
import pygame as pg
from math import atan2, cos, sin, radians, pi
from basico.sistema_colisao import SistemaColisao
from .obstaculo import Obstaculo

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
        self.__colidindo = False
        self.__pode_mexer = True

    @property
    def dano(self):
        return self.__dano
    
    def atualizar(self,eventos):
        self.__pode_mexer = True
        #trata eventos:
        self.tratar_eventos(eventos)

        # movimento:
        self.set_direction()
        self.set_velocidade()
        
        if self.__pode_mexer:
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
                elif evento.colisores[1] == self:
                    self.eventoColisao(evento.colisores[0])

    def eventoColisao(self, colisor):
        from jogo.jogador.tiro import Tiro
        #verificar se está colidindo com alguma entidade, para não se movimentar para cima dela:
        if type(colisor) == Inimigo:
            self.ver_se_pode_mexer(colisor)
            #self.movimento_desvio(colisor)

            #while SistemaColisao.colidiu(self, colisor) == True:
                #self.movimento_desvio(colisor)

        # se for tiro, perde vida:
        if type(colisor) == Tiro:
            self.__vida -= colisor.dano
            if self.__vida <= 0:
                self.ativo = False

        #se for jogador, não sobrepoe ele:
        if type(colisor)== Jogador:
            while SistemaColisao.colidiu(self, colisor) == True:
                self.movimentacao(-1)
            
        """if type(colisor)== Obstaculo:
            self.__pode_mexer = False
            self.movimento_desvio(colisor)"""
                


                    

    def movimentacao(self, sentido = 1):
        sentido = sentido
        self.__x += (self.__velocidade * cos(self.__direction))*sentido
        self.__y += (self.__velocidade * sin(self.__direction))*sentido
        nova_posicao = [self.__x, self.__y]
        self.pos_tela = tuple(nova_posicao)
     

    def calculo_desvio(self, colisor):
        
        alvo_x = self.__alvo.pos_tela[0]
        alvo_y = self.__alvo.pos_tela[1]

        colisor_x = colisor.pos_tela[0]
        colisor_y = colisor.pos_tela[1]

        #calculo coordenada menor (direção): 
        dx_ideal = colisor.dimensoes[0] + self.dimensoes[0]
        dy_ideal = colisor.dimensoes[1] + self.dimensoes[1]

        dx_atual = abs(colisor_x - self.__x)
        dy_atual = abs(colisor_y - self.__y)

        if dy_atual < dy_ideal: 
            a = "y"

        if dx_atual < dx_ideal: 
            a = "x"

        else:
            a = "diagonal"

        return a

    def movimento_desvio(self, colisor):

        #calcular sinal movimento x :
        if  sin(self.__direction) > 0:
            sinal_x = 1
        elif sin(self.__direction) < 0:
            sinal_x = -1

        #calcular sinal movimento y:
        if cos(self.__direction) > 0:
            sinal_y = 1
        elif cos(self.__direction) > 0:
            sinal_y = 1
        
        if self.get_distancia(self, self.alvo) > self.get_distancia(colisor, self.alvo):
            a = self.calculo_desvio(colisor)

            if a == "y":
                self.__y += (self.__velocidade * sin(self.__direction))

            elif a == "x":
                self.__x += (self.__velocidade * cos(self.__direction))

            else:
                self.__y += (self.__velocidade * sin(self.__direction))

            nova_posicao = [self.__x, self.__y]
            self.pos_tela = tuple(nova_posicao)

    def ver_se_pode_mexer(self, colisor):
        if self.get_distancia(self, self.alvo) > self.get_distancia(colisor, self.alvo):
            self.__pode_mexer = False

    def calcular_sobreposicao(self,colisor):
        a = 2
        colisor_x = colisor.pos_tela[0]
        colisor_y = colisor.pos_tela[1]

        dx_ideal = colisor.dimensoes[0] + a + self.dimensoes[0]
        dy_ideal = colisor.dimensoes[1] + a + self.dimensoes[1]

        dx_atual = abs(colisor_x - self.__x) +  (colisor.dimensoes[0]/2) + (self.dimensoes[0]/2)
        dy_atual = abs(colisor_y - self.__y) +  (colisor.dimensoes[1]/2) + (self.dimensoes[1]/2)

        sobreposicao_x = abs(dx_ideal - dx_atual)
        sobreposicao_y = abs(dy_ideal - dy_atual)
        sobreposicao = [sobreposicao_x, sobreposicao_y]

        return sobreposicao


    def movimento_nao_sobressair(self, colisor):
            
            sobreposicao = self.calcular_sobreposicao(colisor)

            if colisor.pos_tela[0] >= self.__x:
                self.__x -= sobreposicao[0]
            
            elif colisor.pos_tela[0] <= self.__x:
                self.__x += sobreposicao[0]

            if colisor.pos_tela[1] <= self.__y:
                self.__y += sobreposicao[1]

            elif colisor.pos_tela[1] >= self.__y:
                self.__y -= sobreposicao[1]

            nova_posicao = [self.__x, self.__y]
            self.pos_tela = tuple(nova_posicao)


#agradecimento de código ao grupo 4. [Artur Soda e xxxxxx]
    def set_direction(self):
        alvo_x = self.__alvo.pos_tela[0]
        alvo_y = self.__alvo.pos_tela[1]

        dx = alvo_x - self.__x
        dy = alvo_y - self.__y
        angle = atan2(dy, dx) 
        self.__direction = angle

    def set_velocidade(self):
        niveis_velocidade = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        self.__velocidade = niveis_velocidade[self.__nivel_velocidade]

    # se a vida for 0, inimigo morre:
    def verificar_vida(self):
        if self.__vida == 0:
            self.ativo = False

    @property
    def alvo(self):
        return self.__alvo
    
    @property
    def direction(self):
        return self.__direction





