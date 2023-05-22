from abc import ABC, abstractmethod

class Desenhavel:
    @abstractmethod
    def desenhar(self, tela, pos_tela, dimensoes):
        pass

class DesenhavelRetangulo(Desenhavel):
    def __init__(self, cor):
        self.cor = cor

    def desenhar(self, tela, pos_tela, dimensoes):
        pg.draw.rect(tela, self.cor, (*pos_tela, *dimensoes))

