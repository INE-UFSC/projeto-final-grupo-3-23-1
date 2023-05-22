from basico.entidadeTela import EntidadeTela
from basico.evento import Evento

class Inimigo(EntidadeTela):

    def __init__(self,tela, pos_tela, dimensoes, desenhavel, dano, velocidade ):
        super().__init__(tela, pos_tela, dimensoes, desenhavel)
        self.pos_atual = super.pos_tela
        self.__dano = dano
        self.__velocidade = velocidade
        self.__vida = 5


    @property
    def dano(self):
        return self.__dano
    
    def eventoColisão(self):
        if Evento.verificarColisão(self, "bala") == True:
            self.__vida =- 1




