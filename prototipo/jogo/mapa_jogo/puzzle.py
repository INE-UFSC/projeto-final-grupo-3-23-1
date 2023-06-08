from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo
from basico.evento import EventoApertouBotaoEsquerdo, EventoColisao, EventoApertouTecla
import pygame as pg
from menu.botao import Botao

class Puzzle(EntidadeTela):
    def __init__(self, tela, enigma, resposta):
        super().__init__(tela,
                        (tela.get_width()/2, tela.get_height()/2),
                        (tela.get_width()/8, tela.get_height()/8),
                        DesenhavelRetangulo(tela, (128, 128, 128)))
        self.__enigma = enigma
        self.__resposta = resposta
        self.__resolvido = False
        self.__modo = 1
        self.criar_elementos()
    
    def criar_elementos(self):
        self.__caixa_resposta = DesenhavelRetangulo(self.tela, (128, 64, 64))
        self.__botao_responder = Botao(self.tela, (self.tela.get_width()*2/3, self.tela.get_height()/6), 
                                       (self.tela.get_width()/12, self.tela.get_height()/16),
                                       DesenhavelRetangulo(self.tela, (128, 64, 64)),
                                       'Responder', 40 / 1080)
        
    
    def atualizar(self, eventos):
        if self.__modo == 1:
            for evento in eventos:
                from jogo.jogador.jogador import Jogador
                if isinstance(evento, EventoColisao) \
                    and evento.possui(self) \
                    and evento.possuiTipo(Jogador):
                    self.__modo = 2
        
        elif self.__modo == 2:
            for evento in eventos:
                if isinstance(evento, EventoApertouBotaoEsquerdo):
                    rect = pg.Rect((0, 0), (self.tela.get_width()/3, self.tela.get_height()/6)) 
                    rect.center = (self.tela.get_width()/12, self.tela.get_height()/16)
                    if rect.collidepoint(evento.pos_mouse): 
                        self.__modo = 3
        elif self.__modo == 3:
            self.__chute = ''
            for evento in eventos:
                if isinstance(evento, EventoApertouTecla):
                    self.__chute += evento.unicode
            self.__botao_responder.atualizar()
            if self.__botao.apertou:
                self.__modo = 4
        elif self.__modo == 4:
            if self.__chute == self.__resposta:
                self.__resolvido = True
                print('ok')

    
    def desenhar(self):
        self.desenhavel.desenhar(self.pos_tela, self.dimensoes)
        if self.__modo == 2 or self.__modo == 3:
            font = pg.font.Font('freesansbold.ttf', 32)
            text = font.render(self.__enigma, True, (0, 0, 0), (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (self.tela.get_width()/2, self.tela.get_height()/4)
            self.tela.blit(text, textRect)
            self.__caixa_resposta.desenhar((self.tela.get_width()/3, self.tela.get_height()/6), 
                                       (self.tela.get_width()/12, self.tela.get_height()/16))
            self.__botao_responder.desenhar()
            if self.__modo == 3:
                rect = pg.Rect((0, 0), (self.tela.get_width()/3, self.tela.get_height()/6)) 
                rect.center = (self.tela.get_width()/12, self.tela.get_height()/16)
                self.tela.blit(self.__chute, pg.Rect(0, 0), rect)
 
            


    @property
    def resolvido(self):
        return self.__resolvido
