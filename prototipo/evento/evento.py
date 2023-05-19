from abc import ABC

class Evento(ABC):
    pass

class EventoColisao(Evento):
    def __init__(self, outro):
        self.outro = outro

class EventoPygame(Evento):
    def __init__(self, evento_pygame):
        self.evento_pygame = evento_pygame

