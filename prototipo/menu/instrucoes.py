from basico.desenhavel import *
from basico.entidade import Entidade
from .botao import Botao

class Instrucoes(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        self.__tela_w = tela.get_width()
        self.__tela_h = tela.get_height()
        self.__titulo = DesenhavelTexto(tela, 'Como jogar', 75/1080)
        self.__teclas = [DesenhavelTexto(tela, 'Use as teclas:'),
                        DesenhavelTexto(tela, '- WASD para se movimentar Talam'),
                        DesenhavelTexto(tela, '- K para atirar bolinhas de luz com sua varinha'),
                        DesenhavelTexto(tela, '- TAB para abrir/fechar o mapa do labirinto')]
        explicacao = 'Você é o Talam! Movimente-se pelo labirinto de sua mente representado por salas até chegar em uma sala em que você alcançará o autoconhecimento. Mas cuidado! Durante essa jornada, você encontrará inimigos e para derrotá-los deve atirar bolinhas de luz com sua varinha até que eles percam o foco em lhe atacar. Além disso, também haverá enigmas para você decifrar!'
        self.__explicacao = []
        linha = ''
        for carac in explicacao:
            linha += carac
            superficie = DesenhavelTexto(self.tela, linha)
            if carac == ' ':
                if not superficie.rect.width < self.__tela_w*8/10:
                    self.__explicacao.append(superficie)
                    linha = ''
        if superficie.rect.width < self.__tela_w*8/10:
            self.__explicacao.append(superficie)
        
        self.__botao_x = Botao(tela, (self.__tela_w*9/10, self.__tela_h/10),
                               (self.__tela_w/10, self.__tela_h/10), 
                               DesenhavelRetangulo(tela, (153, 76, 0)), 'X')

    def desenhar(self):
        self.__titulo.desenhar((self.__tela_w/2, self.__tela_h/10))
        espaco_linha = self.__titulo.espaco_linha*2

        for superficie in self.__teclas:
            superficie.desenharSuperiorDireito((self.__tela_w/10, espaco_linha))
            espaco_linha += superficie.espaco_linha

        for superficie in self.__explicacao:
            espaco_linha += superficie.espaco_linha
            superficie.desenhar((self.__tela_w/2, espaco_linha))
        
        self.__botao_x.desenhar()

    def atualizar(self, eventos):
        self.__botao_x.atualizar(eventos)

    def getColisores(self):
        pass

    @property
    def botao_x(self):
        return self.__botao_x