from basico.entidadeTela import EntidadeTela
from basico.evento import Evento
from jogador.tiro import Tiro
from  jogador.jogador import Jogador
class Inimigo(EntidadeTela):

    def __init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade, vida_inicial, jogador: Jogador ):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_atual = super.pos_tela
        self.__dano = dano
        self.__velocidade = velocidade
        self.__vida = vida_inicial
        self.__ativo = True
        self.__alvo = jogador


    @property
    def dano(self):
        return self.__dano
    
    def eventoColisão(self, outro):

        if isinstance(outro, Tiro):
            self.__vida -= 1

    def atualizar(self):
        
        # movimento:
        self.movimentacao()
        
        self.verificar_vida()

    def movimentacao(self):
        # deve perseguir jogador. 
        """Falta: Deve andar a cada unidade de tempo(?) !!!"""

        #verificar se jogador está à esquerda ou à direita (x):
        if self.__alvo.pos_tela[0] < self.pos_tela[0]:
            self.pos_tela[0]-=1
        elif self.__alvo.pos_tela[0] > self.pos_tela[0]:
            self.pos_tela[0] += 1

        #verificar se jogador está acima ou abaixo (y):
        if self.__alvo.pos_tela[1] < self.pos_tela[1]:
            self.pos_tela[1]-= 1
        elif self.__alvo.pos_tela[1] > self.pos_tela[1]:
            self.pos_tela += 1

    def verificar_vida(self):
        if self.__vida == 0:
            self.__ativo = False

    




