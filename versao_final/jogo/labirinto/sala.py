import pygame as pg
from pygame.locals import *

from basico.entidade import Entidade
from .aparencia import Aparencia


class Sala(Entidade):
    def __init__(self, tela, desenhavel):
        super().__init__(tela)
        self.__desenhavel = desenhavel
        self.__sala_portas = []

    def getColisores(self):
        colisores = []
        colisores.extend(self.__sala_portas)

        return colisores

    def desenhar(self):
        from basico.desenhavel import DesenhavelImagem
        if isinstance(self.__desenhavel, DesenhavelImagem):
            self.__desenhavel.desenhar((self.telaW()/2, self.telaH()/2))
        for sala_porta in self.sala_portas:
            sala_porta.desenhar()

    def atualizar(self, eventos):
        for sala_porta in self.__sala_portas:
            sala_porta.atualizar(eventos)

    def adicionarSalaPorta(self, sala_porta):
        from .sala_porta import SalaPorta
        if isinstance(sala_porta, SalaPorta):
            self.__sala_portas.append(sala_porta)

    @property
    def desenhavel(self):
        return self.__desenhavel
    
    @property
    def sala_portas(self,):
        return self.__sala_portas


    
