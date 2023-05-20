from basico.entidadeTela import EntidadeTela

class Tiro(EntidadeTela):
    def __init__(self, pos_tela, largura, comprimento, sprite, dano, velocidade):
        self.pos_tela = pos_tela
        self.largura = largura
        self.comprimento = comprimento
        self.sprite = sprite
        self.dano = dano
        self.velocidade = velocidade

