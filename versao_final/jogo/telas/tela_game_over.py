from basico.entidade import Entidade
from basico.desenhavel import DesenhavelImagem, DesenhavelRetangulo
from menu.botao import Botao
import os

class TelaGameOver(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        caminho_im = os.path.join('imagens', 'game_over.png')
        self.__desenhavel = DesenhavelImagem(tela, caminho_im, (self.telaW(), self.telaH()))

        arq_botao_sair = os.path.join('imagens', 'botoes', 'sair_preto.png')
        arq_botao_voltar_ao_menu = os.path.join('imagens', 'botoes', 'voltar_ao_menu_preto.png')
        dimens_botao = (self.telaW()/6, self.telaH()/9)
        self.__botoes = [Botao(tela, (self.telaW()/2, 25*self.telaH()/32),
                                  dimens_botao,
                                  DesenhavelImagem(tela, arq_botao_sair, dimens_botao), ''),
                        Botao(tela, (self.telaW()/2, 29*self.telaH()/32),
                                  dimens_botao,
                                  DesenhavelImagem(tela, arq_botao_voltar_ao_menu, dimens_botao), '')]

    def desenhar(self):
        self.__desenhavel.desenhar((self.telaW()/2, self.telaH()/2))

        for botao in self.__botoes:
            botao.desenhar()

    def atualizar(self, eventos):
        for botao in self.__botoes:
            botao.atualizar(eventos)

    @property
    def botoes(self):
        return self.__botoes