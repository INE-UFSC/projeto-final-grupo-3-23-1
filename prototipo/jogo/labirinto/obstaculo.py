from basico.entidade_tela import EntidadeTela

class Obstaculo(EntidadeTela):
    def __init__(self, tela, pos_tela, dimensoes, desenhavel):
        super().__init__(tela, pos_tela, dimensoes, desenhavel, solido=True, movel=False)


