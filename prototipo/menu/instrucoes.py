from basico.desenhavel import DesenhavelImagem
from basico.entidade import Entidade
from .botao import Botao

class Instrucoes(Entidade):
    def __init__(self, tela, arq_im_fundo, arq_imagem_voltar):
        super().__init__(tela)

        self.__im_fundo = DesenhavelImagem(tela, arq_im_fundo, (self.telaW(), self.telaH()))
        
        dimens_botao_voltar = (self.telaW()/8, self.telaH()/12)

        self.__botao_voltar = Botao(tela, (self.telaW()/2, self.telaH()*12/13),
                               dimens_botao_voltar, 
                               DesenhavelImagem(tela, arq_imagem_voltar, dimens_botao_voltar), '')

    def desenhar(self):
        self.__im_fundo.desenhar((self.telaW()/2, self.telaH()/2))
        self.__botao_voltar.desenhar()

    def atualizar(self, eventos):
        self.__botao_voltar.atualizar(eventos)

    @property
    def botao_voltar(self):
        return self.__botao_voltar
