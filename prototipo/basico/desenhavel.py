import pygame as pg

from abc import ABC, abstractmethod

class Desenhavel(ABC):
    def __init__(self, tela):
        self.__tela = tela

    @abstractmethod
    def desenhar(self, pos_tela):
        pass

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        self.__tela = tela

class DesenhavelRetangulo(Desenhavel):
    def __init__(self, tela, cor, dimensoes):
        super().__init__(tela)
        self.__cor = cor
        self.__dimensoes = dimensoes

    def desenhar(self, pos_tela):
        rect = pg.Rect((0, 0), self.dimensoes)
        rect.center = pos_tela

        pg.draw.rect(self.tela, self.cor, rect)

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

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
    def superficie(self):
        return self.__superficie

    @property
    def espaco_linha(self):
        return self.__espaco_linha
    
    @property
    def rect(self):
        return self.__rect

class DesenhavelImagem(Desenhavel):
    def __init__(self, tela, arquivo, dimensoes, cor_fundo=None):
        super().__init__(tela)
        self.__imagem = pg.image.load(arquivo).convert()

        if cor_fundo is not None:
            self.__imagem.set_colorkey(cor_fundo)
            self.__imagem.convert_alpha()

        self.__imagem = pg.transform.scale(self.__imagem, dimensoes)

    def desenhar(self, pos_tela):
        rect = self.imagem.get_rect()
        rect.center = pos_tela

        self.tela.blit(self.__imagem, rect)

    @property
    def imagem(self):
        return self.__imagem

    """
    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem
    """

    @property
    def dimensoes(self):
        return self.__dimensoes

    """
    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes
    """


