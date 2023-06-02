from basico.entidade import Entidade
from .botao import Botao
from basico.desenhavel import DesenhavelRetangulo

class Menu(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        self.tela = tela

        self.botoes = [Botao(tela, (150, 125), (20,20), DesenhavelRetangulo(tela, (255, 0, 0)))]
        self.modo = ""

    def atualizar(self, eventos: list):
        for botao in self.botoes:
            botao.atualizar(eventos)

    def desenhar(self):
        for botao in self.botoes:
            botao.desenhar()

    def rodar(self):
        cor_fundo = (255, 255, 255)

        self.tela.fill(cor_fundo)

        self.atualizar()
        self.desenhar()

    
