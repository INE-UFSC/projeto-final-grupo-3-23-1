from .sala import Sala
import random

from basico.desenhavel import DesenhavelRetangulo


class SalaInimigo(Sala):
    def __init__(self, tela, desenhavel, powerups, jogador):
        super().__init__(desenhavel)
        self.__powerups = powerups
        self.__inimigos = []

        #criando inimigos aleatoriamente
        from .inimigo import Inimigo
        for i in range(random.randrange(2, 5)):
            i = random.randrange(500)
            j = random.randrange(400)
            posicoes = [i, j]
            self.__inimigos.append(Inimigo(
                            tela,
                            posicoes,
                            [50, 50],
                            DesenhavelRetangulo(tela, (255, 0, 0)),
                            3, 1, 1,
                            jogador))

    def getColisores(self):
        colisores = super().getColisores()
        
        for inimigo in self.__inimigos:
            if inimigo.ativo:
                colisores.append(inimigo)

        colisores.extend(self.__powerups)

        return colisores
    
    def desenhar_resto(self):
        for inimigo in self.__inimigos:
            if inimigo.ativo:
                inimigo.desenhar()
        #desenhar powerups quando forem implementados
    
    def atualizar_resto(self, eventos):
        for inimigo in self.__inimigos:
            if inimigo.ativo:
                inimigo.atualizar(eventos)

    @property
    def inimigos(self):
        return self.__inimigos
