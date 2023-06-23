
class Porta:
    def __init__(self):
        self.__sala_portas = []
        self.__aberta = False
    
    def abrir(self):
        self.__aberta = True
    
    def adicionarSalaPorta(self, sala_porta):
        from .sala_porta import SalaPorta
        if isinstance(sala_porta, SalaPorta):
            self.__sala_portas.append(sala_porta)
    
    @property
    def aberta(self):
        return self.__aberta
    
    @property
    def sala_portas(self):
        return self.__sala_portas