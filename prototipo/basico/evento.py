from abc import ABC

class Evento(ABC):
    pass

class EventoColisao(Evento):
    def __init__(self, a, b):
        self.colisores = [a, b]

class EventoTeclaApertada(Evento):
    def __init__(self, tecla):
        self.tecla = tecla

class EventoApertouTecla(Evento):
    def __init__(self, tecla):
        self.tecla = tecla

