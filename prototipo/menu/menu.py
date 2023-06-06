from basico.entidade import Entidade
from .botao import Botao
from basico.desenhavel import DesenhavelRetangulo

class Menu(Entidade):
    def __init__(self, tela):
        super().__init__(tela)
        self.tela = tela

        self.botoes = [Botao(tela, (tela.get_width()/2, 2*tela.get_height()/5), (500, 200), DesenhavelRetangulo(tela, (255, 0, 255)))]
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

    
