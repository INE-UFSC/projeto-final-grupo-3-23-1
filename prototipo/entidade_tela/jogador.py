from entidadeTela import EntidadeTela

class Jogador(EntidadeTela):
    def __init__(self, pos_tela, dimensoes, arma):
        super().__init__(pos_tela, dimensoes)
        self.vida = 3
        self.arma = arma
        self.powerups = []

    def atualizar(eventos: list):
        for evento in eventos:
            pass

    def eventoColisao(self, outro):
        if isinstance(outro, Inimigo):
            self.vida -= 1

        if isinstance(outro, SalaPortaCima):
            pass
        if isinstance(outro, SalaPortaBaixo):
            pass
        if isinstance(outro, SalaPortaEsquerda):
            pass
        if isinstance(outro, SalaPortaDireita):
            pass
