from basico.desenhavel import *
from basico.entidade import Entidade
from .botao import Botao

class Instrucoes(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        self.__titulo = DesenhavelTexto(tela, 'Instruções', 75/1080)
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
                if not superficie.rect.width < self.telaW()*8/10:
                    self.__explicacao.append(superficie)
                    linha = ''
        if superficie.rect.width < self.telaW()*8/10:
            self.__explicacao.append(superficie)
        
        dimens_botao_voltar = (self.telaW()/8, self.telaH()/10)

        self.__botao_voltar = Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimens_botao_voltar, 
                               DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao_voltar), 'Voltar')

    def desenhar(self):
        self.__titulo.desenhar((self.telaW()/2, self.telaH()/10))
        espaco_linha = self.__titulo.espaco_linha*2

        for superficie in self.__teclas:
            superficie.desenharSuperiorDireito((self.telaW()/10, espaco_linha))
            espaco_linha += superficie.espaco_linha

        for superficie in self.__explicacao:
            espaco_linha += superficie.espaco_linha
            superficie.desenhar((self.telaW()/2, espaco_linha))
        
        self.__botao_voltar.desenhar()

    def atualizar(self, eventos):
        self.__botao_voltar.atualizar(eventos)

    @property
    def botao_voltar(self):
        return self.__botao_voltar
