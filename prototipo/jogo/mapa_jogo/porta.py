#from basico.entidadeTela import EntidadeTela

class Porta:
    def __init__(self):
        self.__sala_portas = []
        self.__aberta = False
    
    def abrir(self):
        self.__aberta = True
    
    def adicionar_sala_porta(self, sala_porta):
        self.__sala_portas.append(sala_porta)
    
    @property
    def aberta(self):
        return self.__aberta