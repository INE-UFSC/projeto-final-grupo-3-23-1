from basico.entidade import Entidade
from basico.desenhavel import DesenhavelImagem, DesenhavelTexto, DesenhavelRetangulo
from menu.botao import Botao
import os

class TelaGameOver(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        caminho_im = os.path.join('imagens', 'game_over.jpg')
        self.__desenhavel = DesenhavelImagem(tela, caminho_im, (self.telaW(), self.telaH()))

        dimens_botao = (self.telaW()/4, self.telaH()/16)
        self.__botoes = [Botao(tela, (6*self.telaW()/8, 15*self.telaH()/16),
                                  dimens_botao,
                                  DesenhavelRetangulo(tela, (128, 64, 64), dimens_botao),
                                  'Sair', 40/1080),
                        Botao(tela, (6*self.telaW()/8, 13*self.telaH()/16),
                                  dimens_botao,
                                  DesenhavelRetangulo(tela, (128, 64, 64), dimens_botao),
                                  'Voltar ao menu', 40/1080)]

        #criando mensagem de game over:
        mensagem = 'Você não se manteve firme em sua missão\ne foi dominado pelos obstáculos.\nPerdeu seu foco e sucumbiu aos testes de sua mente'
        linhas = mensagem.split('\n')
        self.__superficies = []
        for linha in linhas:
            self.__superficies.append(DesenhavelTexto(tela, linha, cor_texto=(0, 0, 0)))
        self.__superficies.reverse()


    def desenhar(self):
        self.__desenhavel.desenhar((self.telaW()/2, self.telaH()/2))

        espaco_linha = (-1) * self.__superficies[0].espaco_linha
        altura = 0
        for s in self.__superficies:
            altura += espaco_linha
            s.desenhar((self.telaW()/2, self.telaH()/2 + altura))

        for botao in self.__botoes:
            botao.desenhar()

    def atualizar(self, eventos):
        for botao in self.__botoes:
            botao.atualizar(eventos)

    @property
    def botoes(self):
        return self.__botoes