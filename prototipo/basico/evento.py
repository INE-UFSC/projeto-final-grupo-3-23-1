from abc import ABC

class Evento(ABC):
    pass

class EventoColisao(Evento):
    def __init__(self, a, b):
        self.colisores = [a, b]

    def possuiTipo(self, tipo):
        return any(isinstance(x, tipo) for x in self.colisores)

    def possui(self, elem):
        return any(x == elem for x in self.colisores)

    def getElemDoTipo(self, tipo):
        for colisor in self.colisores:
            if isinstance(colisor, tipo):
                return colisor

class EventoTeclaApertada(Evento):
    def __init__(self, tecla):
        self.tecla = tecla

class EventoApertouTecla(Evento):
    def __init__(self, tecla):
        self.tecla = tecla

