from basico.evento import EventoColisao

class SistemaColisao:
    def __init__(self):
        self.colisores = []

    def adicionarColisor(self, colisor):
        self.colisores.append(colisor)

    @staticmethod
    def colidiu(a, b):
        rect_a = pg.Rect(*a.pos_tela, *a.dimensoes) 
        rect_b = pg.Rect(*b.pos_tela, *b.dimensoes) 

        return rect_a.colliderect(rect_b)
        
    def getColisoes(self):
        eventos = []
        for i in range(len(self.colisores)):
            for j in range(i+1, len(self.colisores)):
                a = self.colisores[i]
                b = self.colisores[j]
                if self.colidiu(a, b):
                    eventos.append(EventoColisao(a, b))
        return eventos

    def removerNaoAtivos(self):
        colisores_rem = []
        for colisor in self.colisores:
            if not colisor.ativo:
                colisores_rem.append(colisor)
        
        for rem in colisores_rem:
            self.colisores.remove(rem)

