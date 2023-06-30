from basico.desenhavel import *
from basico.entidade import Entidade
from .botao import Botao
import os

class Instrucoes(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        
        arq_fundo = os.path.join('imagens', 'menu', 'instrucoes.png')
        self.__fundo = DesenhavelImagem(tela, arq_fundo, (self.telaW(), self.telaH()))
        
        dimens_botao_voltar = (self.telaW()/8, self.telaH()/10)

        self.__botao_voltar = Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimens_botao_voltar, 
                               DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao_voltar), 'Voltar')

    def desenhar(self):
        self.__fundo.desenhar((self.telaW()/2, self.telaH()/2))
        self.__botao_voltar.desenhar()

    def atualizar(self, eventos):
        self.__botao_voltar.atualizar(eventos)

    @property
    def botao_voltar(self):
        return self.__botao_voltar
