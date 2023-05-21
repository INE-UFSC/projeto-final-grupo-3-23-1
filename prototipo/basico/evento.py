from abc import ABC
import pygame
class Evento(ABC):
    # lembrar que no pygame eventos são coletados de forma geral, não estão ligados a uma entidade.
    def __init__(self,  o):
        # para poder acessar todos os dados jo jogo, precisa ter o jogo como atributo
        self.__jogo = jogo
        #verifica eventos coletados pelo pygame no frame:
        self.__eventos = pygame.event.get()
        self.processar_eventos(self.__eventos)

    #processa os eventos coletados:
    def processar_eventos(eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                ...

            #interar com dmais tipos de eventos

    def verificarColisão_2(self, entidade_eu, atributo_entidade_outro):
        #pode verificar colisão entre tipos de objetos específicos
        #acessa objeto ou lista de objetos específica da sala a ser analizada a colisão:
        atributo_entidade_outro = self.__jogo.mapa_jogo.sala_atual.atributo_entidade_outro
        #se for uma lista de objetos (por exemplos, vários inimigos, ou vários tiros), vai verificar a colisão com cada um:
        if atributo_entidade_outro.type == list:
            for entidade in  atributo_entidade_outro: 
                self.colisao(entidade_eu, entidade)
        else: self.colisao(entidade_eu,  atributo_entidade_outro)

    #verifica se duas entidades colidiram:
    def colisao(entidade_eu, entidade_outro):
        return entidade_eu.colliderect(entidade_outro)
            

class EventoColisao(Evento):
    def __init__(self, outro):
        self.outro = outro

class EventoPygame(Evento):
    def __init__(self, evento_pygame):
        self.evento_pygame = evento_pygame

