from entidade_tela import EntidadeTela
class Inimigo(EntidadeTela):
    def __init__(self):
        self.__dano = float
        self.__velocidade = float

    @property
    def dano(self):
        return self.__dano
    



