import pygame as pg

from abc import ABC, abstractmethod

class Desenhavel:
    def __init__(self, tela):
        self.tela = tela

    @abstractmethod
    def desenhar(self):
        pass

class DesenhavelRetangulo(Desenhavel):
    def __init__(self, tela, cor):
        super().__init__(tela)
        self.cor = cor

    def desenhar(self, pos_tela, dimensoes):
        rect = pg.Rect((0, 0), dimensoes)
        rect.center = pos_tela

        pg.draw.rect(self.tela, self.cor, rect)

class DesenhavelTexto(Desenhavel):
    def __init__(self, tela, texto, tamanho_fonte = 40/1080,
                  nome_fonte = "Comic Sans MS",
                  cor_texto = (255, 255, 255)):
        super().__init__(tela)
        fonte = pg.font.SysFont(nome_fonte, int(tamanho_fonte*self.tela.get_height()))
        self.__superficie = fonte.render(texto, True, cor_texto)
        self.__espaco_linha = fonte.get_linesize()
        self.__rect = self.__superficie.get_rect()
    
    def desenharSuperiorDireito(self, pos_tela):
        self.tela.blit(self.__superficie, pos_tela)

    def desenhar(self, pos_tela):
        self.__rect.center = pos_tela
        self.tela.blit(self.__superficie, self.__rect)

    @property
    def espaco_linha(self):
        return self.__espaco_linha
    
    @property
    def rect(self):
        return self.__rect

