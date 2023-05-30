from basico.entidade_tela import EntidadeTela
from basico.evento import Evento, EventoColisao
from jogador.jogador import Jogador
import pygame as pg

class Inimigo(EntidadeTela):

    def __init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador ):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_atual = self.pos_tela
        self.__dano = dano
        self.__velocidade = velocidade
        self.__vida = vida_inicial
        self.__alvo = jogador
        # Crie um objeto Clock para controlar o tempo
        self.__clock = pg.time.Clock()

    @property
    def dano(self):
        return self.__dano
    
    def eventoColisao(self, colisor):
        from jogador.tiro import Tiro

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
                    

                    
#    def checagem_tempo(self):
#        borda_clock = False
#        # Atualize o tempo acumulado
#        tempo_acumulado += self.__clock.get_time()
#        # Defina o intervalo de tempo desejado (em milissegundos)
#        intervalo_tempo =  100  #  0,1 segundos
#        # Variável para controlar a contagem do tempo
#        tempo_acumulado = 0
#        if tempo_acumulado >= intervalo_tempo:
#            borda_clock = True
#        tempo_acumulado = 0  # Reinicie o tempo acumulado
#        return borda_clock
    
    def movimentacao(self):
        #verificar se jogador está à esquerda ou à direita (x):
        if self.__alvo.pos_tela[0] < self.pos_tela[0]:
            self.pos_tela[0] -= 1
        elif self.__alvo.pos_tela[0] > self.pos_tela[0]:
            self.pos_tela[0] += 1

        #verificar se jogador está acima ou abaixo (y):
        if self.__alvo.pos_tela[1] < self.pos_tela[1]:
            self.pos_tela[1]-= 1
        elif self.__alvo.pos_tela[1] > self.pos_tela[1]:
            self.pos_tela[1] += 1

        

#        if self.checagem_tempo():
#            # deve perseguir jogador. 
#
#            #verificar se jogador está à esquerda ou à direita (x):
#            if self.__alvo.pos_tela[0] < self.pos_tela[0]:
#                self.pos_tela[0]-=25
#            elif self.__alvo.pos_tela[0] > self.pos_tela[0]:
#                self.pos_tela[0] += 25
#
#            #verificar se jogador está acima ou abaixo (y):
#            if self.__alvo.pos_tela[1] < self.pos_tela[1]:
#                self.pos_tela[1]-= 25
#            elif self.__alvo.pos_tela[1] > self.pos_tela[1]:
#                self.pos_tela += 25

    # se a vida for 0, inimigo morre:
    def verificar_vida(self):
        if self.__vida == 0:
            self.ativo = False

    




