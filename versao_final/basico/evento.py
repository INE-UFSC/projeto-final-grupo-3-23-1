from abc import ABC

class Evento(ABC):
    pass

class EventoColisao(Evento):
    def __init__(self, a, b):
        self.__colisores = [a, b]

    @property
    def colisores(self):
        return self.__colisores

    @colisores.setter
    def colisores(self, colisores):
        self.__colisores = colisores

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
        self.__tecla = tecla

    @property
    def tecla(self):
        return self.__tecla

    @tecla.setter
    def tecla(self, tecla):
        self.__tecla = tecla

class EventoApertouTecla(Evento):
    def __init__(self, tecla, unicode):
        self.__tecla = tecla
        self.__unicode = unicode

    @property
    def tecla(self):
        return self.__tecla

    @tecla.setter
    def tecla(self, tecla):
        self.__tecla = tecla

    @property
    def unicode(self):
        return self.__unicode

    @unicode.setter
    def unicode(self, unicode):
        self.__unicode = unicode

class EventoApertouBotaoEsquerdo(Evento):
    def __init__(self, pos_mouse):
        self.__pos_mouse = pos_mouse

    @property
    def pos_mouse(self):
        return self.__pos_mouse

    @pos_mouse.setter
    def pos_mouse(self, pos_mouse):
        self.__pos_mouse = pos_mouse
