#from basico.entidadeTela import EntidadeTela

class Porta:
    def __init__(self, sala_portas: list):
        self.__sala_portas = sala_portas
        self.__aberta = False
    
    def abrir(self):
        self.__aberta = True
    
    def fechar(self):
        self.__aberta = False
