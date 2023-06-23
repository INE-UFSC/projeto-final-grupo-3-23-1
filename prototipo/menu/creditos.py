from basico.desenhavel import *
from basico.entidade import Entidade
from basico.evento import Evento
from .botao import Botao

class Creditos(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        self.__titulo = DesenhavelTexto(tela, 'Créditos', 75/1080)
        self.__desenvolvedores = [DesenhavelTexto(tela, 'Jogo desenvolvido por:'),
                                  DesenhavelTexto(tela, '- Bianca Mazzuco Verzola'),
                                  DesenhavelTexto(tela,  '- Davi Menegaz Junkes'),
                                  DesenhavelTexto(tela, '- Felipe Elton Pazini Savi'),
                                  DesenhavelTexto(tela, '-  Rita Louro Barbosa')]

        dimens_botao_voltar = (self.telaW()/8, self.telaH()/10)
        self.__botao_voltar = Botao(tela, (self.telaW()/2, self.telaH()*9/10),
                               dimens_botao_voltar, 
                               DesenhavelRetangulo(tela, (153, 76, 0), dimens_botao_voltar), 'Voltar')

    def desenhar(self):
        self.__titulo.desenhar((self.telaW()/2, self.telaH()/10))
        espaco_linha = self.__titulo.espaco_linha*2

        for superficie in self.__desenvolvedores:
            superficie.desenharSuperiorDireito((self.telaW()/10, espaco_linha))
            espaco_linha += superficie.espaco_linha

        self.__botao_voltar.desenhar()

    def atualizar(self, eventos):
        self.__botao_voltar.atualizar(eventos)

    @property
    def botao_voltar(self):
        return self.__botao_voltar
        
