from basico.entidadeTela import EntidadeTela

class Puzzle(EntidadeTela):
    def __init__(self):
        super.__init__() #???????
        self.__pergunta = str
        self.__resposta_correta = str
        self.__resolvido = False
    
    @property
    def resolvido(self):
        return self.__resolvido
