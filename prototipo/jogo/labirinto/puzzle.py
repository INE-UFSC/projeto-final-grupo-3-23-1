from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelRetangulo, DesenhavelTexto
from basico.evento import EventoApertouBotaoEsquerdo, EventoColisao, EventoApertouTecla
import pygame as pg
from menu.botao import Botao

class Puzzle(EntidadeTela):
    def __init__(self, tela, enigma, resposta, jogador):
        self.tela_w = tela.get_width()
        self.tela_h = tela.get_height()
        super().__init__(tela,
                        (self.tela_w/2, self.tela_h*5/8),
                        (self.tela_w/8, self.tela_h/8),
                        DesenhavelRetangulo(tela, (128, 128, 128)),
                        solido=False, movel=False)
        self.__enigma = enigma
        self.__resposta = resposta
        self.__chute = ''
        self.__resolvido = False
        self.__modo = 1
        self.__jogador = jogador

        self.__botao_responder = Botao(self.tela, (self.tela_w*25/32, self.tela_h/2), 
                                       (self.tela_w*3/16, self.tela_h/16),
                                       DesenhavelRetangulo(self.tela, (128, 64, 64)),
                                       'Responder', 40 / 1080)
        self.__botao_tentar_dnv = Botao(self.tela, (self.tela_w/2, self.tela_h/2), 
                                        (self.tela_w*3/16, self.tela_h/16),
                                       DesenhavelRetangulo(self.tela, (128, 64, 64)),
                                       'Tentar novamente', 40 / 1080)

        self.__caixa_resposta = pg.Rect((0, 0), (self.tela_w/2, self.tela_h/16))
        self.__caixa_resposta.center = (self.tela_w*3/8, self.tela_h/2)

        #cria as linhas da pergunta
        self.__superficies = []
        linha = ''
        for carac in self.__enigma:
            linha += carac
            superficie = DesenhavelTexto(self.tela, linha)
            if carac == ' ':
                if not superficie.rect.width < self.tela_w*6/8:
                    self.__superficies.append(superficie)
                    linha = ''
        if superficie.rect.width < self.tela_w*6/8 or carac != ' ':
            self.__superficies.append(superficie)
        self.__superficies.reverse()
        
    
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
                    if self.__caixa_resposta.collidepoint(evento.pos_mouse): 
                        self.__modo = 3

        elif self.__modo == 3:
            self.__jogador.ativo = False
            for evento in eventos:
                if isinstance(evento, EventoApertouTecla):
                    if evento.tecla == pg.K_BACKSPACE:
                        self.__chute = self.__chute[:-1]
                    elif evento.tecla == pg.K_RETURN or evento.tecla == pg.K_KP_ENTER:
                            self.__modo = 4
                    else:
                        self.__chute += evento.unicode
                        chute = DesenhavelTexto(self.tela, self.__chute)
                        if chute.rect.width > self.__caixa_resposta.width:
                            self.__chute = self.__chute[:-1]

                elif isinstance(evento, EventoApertouBotaoEsquerdo): #se clicar fora da caixa de resposta
                    if not self.__caixa_resposta.collidepoint(evento.pos_mouse): 
                        self.__modo = 2
                        self.__jogador.ativo = True

        elif self.__modo == 4:
            self.__jogador.ativo = True
            if self.__chute.strip().lower() == self.__resposta:
                self.__resolvido = True
                self.__modo = 5
            else:
                self.__modo = 6

        elif self.__modo == 6:
            self.__botao_tentar_dnv.atualizar(eventos)
            if self.__botao_tentar_dnv.apertou:
                self.__modo = 2
                self.__botao_tentar_dnv.resetApertou()
                self.__chute = ''

        self.__botao_responder.atualizar(eventos)
        if self.__botao_responder.apertou:
            self.__modo = 4
            self.__botao_responder.resetApertou()
    
    def desenhar(self):
        super().desenhar()
        if self.__modo == 2 or self.__modo == 3 or self.__modo == 4:

            #desenhar pergunta
            altura = self.tela_h*3/8
            for s in self.__superficies:
                s.desenhar((self.tela_w/2, altura))
                altura -= s.espaco_linha

            #desenhar caixa_reposta
            if self.__modo == 3: #caixa_resposta selecionada
                pg.draw.rect(self.tela, (128, 100, 100), self.__caixa_resposta)
            else:
                pg.draw.rect(self.tela, (128, 64, 64), self.__caixa_resposta)

            self.__botao_responder.desenhar()

            #desenhar escrita da caixa_resposta
            if self.__chute == '':
                text = DesenhavelTexto(self.tela,'Digite sua resposta')
                text.desenharSuperiorDireito(self.__caixa_resposta)
            else:
                text = DesenhavelTexto(self.tela, self.__chute)
                text.desenharSuperiorDireito(self.__caixa_resposta)
 
        elif self.__modo == 5:
            text = DesenhavelTexto(self.tela, 'Parabéns! Você acertou!')
            text.desenhar((self.tela_w/2, self.tela_h*3/8))
 
        elif self.__modo == 6:
            text = DesenhavelTexto(self.tela, 'Você errou!')
            text.desenhar((self.tela_w/2, self.tela_h*3/8))
            self.__botao_tentar_dnv.desenhar()

    @property
    def resolvido(self):
        return self.__resolvido
