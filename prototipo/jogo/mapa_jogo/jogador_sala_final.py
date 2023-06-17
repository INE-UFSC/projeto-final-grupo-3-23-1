from basico.entidade_tela import EntidadeTela

class JogadorSalaFinal(EntidadeTela):
    def __init__(self, tela, jogador):
        super().__init__(tela, 
                         (tela.get_width()/2, tela.get_height()/2), 
                         jogador.dimensoes, 
                         jogador.desenhavel)

    def desenhar(self):
        super().desenhar()
