from basico.entidadeTela import EntidadeTela
from basico.evento import Evento
from jogador.tiro import Tiro
from  jogador.jogador import Jogador
import pygame as pg
from basico.evento import EventoColisao

class Inimigo(EntidadeTela):

    def __init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador ):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_atual = super.pos_tela
        self.__dano = dano
        self.__velocidade = velocidade
        self.__vida = vida_inicial
        self.__ativo = True
        self.__alvo = jogador
        # Crie um objeto Clock para controlar o tempo
        self.__clock = pg.time.Clock()

    @property
    def dano(self):
        return self.__dano
    
    def eventoColisao(self, colisor):
        # se for tiro, perde vida:
        if type(colisor) == Tiro:
            self.__vida -= 1

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
                    

                    
    def checagem_tempo(self):
        borda_clock = False
        # Atualize o tempo acumulado
        tempo_acumulado += self.__clock.get_time()
        # Defina o intervalo de tempo desejado (em milissegundos)
        intervalo_tempo =  100  #  0,1 segundos
        # Variável para controlar a contagem do tempo
        tempo_acumulado = 0
        if tempo_acumulado >= intervalo_tempo:
            borda_clock = True
        tempo_acumulado = 0  # Reinicie o tempo acumulado
        return borda_clock
    
    def movimentacao(self):
        if self.checagem_tempo():
            # deve perseguir jogador. 

            #verificar se jogador está à esquerda ou à direita (x):
            if self.__alvo.pos_tela[0] < self.pos_tela[0]:
                self.pos_tela[0]-=25
            elif self.__alvo.pos_tela[0] > self.pos_tela[0]:
                self.pos_tela[0] += 25

            #verificar se jogador está acima ou abaixo (y):
            if self.__alvo.pos_tela[1] < self.pos_tela[1]:
                self.pos_tela[1]-= 25
            elif self.__alvo.pos_tela[1] > self.pos_tela[1]:
                self.pos_tela += 25

    # se a vida for 0, inimigo morre:
    def verificar_vida(self):
        if self.__vida == 0:
            self.__ativo = False

    




