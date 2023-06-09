from abc import ABC

class Evento(ABC):
    pass

class EventoColisao(Evento):
    def __init__(self, a, b):
        self.colisores = [a, b]

    def possuiTipo(self, tipo):
        return isinstance(self.colisores[0], tipo) or isinstance(self.colisores[1], tipo)

    def possui(self, elem):
        return self.colisores[0] == elem or self.colisores[1] == elem

    def getElemDoTipo(self, tipo):
        for colisor in self.colisores:
            if isinstance(colisor, tipo):
                return colisor

class EventoTeclaApertada(Evento):
    def __init__(self, tecla):
        self.tecla = tecla

class EventoApertouTecla(Evento):
    def __init__(self, tecla, unicode):
        self.tecla = tecla
        self.unicode = unicode

class EventoApertouBotaoEsquerdo(Evento):
    def __init__(self, pos_mouse):
        self.pos_mouse = pos_mouse

