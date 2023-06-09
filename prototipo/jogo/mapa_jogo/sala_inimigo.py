from .sala import Sala
import random

from basico.desenhavel import DesenhavelRetangulo


class SalaInimigo(Sala):
    def __init__(self, tela, desenhavel, powerups, jogador):
        super().__init__(desenhavel)
        self.__powerups = powerups
        self.__inimigos = []
        self.criarInimigos(jogador, tela)
        
    def criarInimigos(self, jogador, tela):
        from .inimigo import Inimigo
        for i in range(random.randrange(2, 5)):
            i = random.randrange(tela.get_width())
            j = random.randrange(tela.get_height())
            posicoes = (i, j)
            self.__inimigos.append(Inimigo(
                            tela,
                            posicoes,
                            [50, 50],
                            DesenhavelRetangulo(tela, (255, 0, 0)),
                            3, 1, 1,
                            jogador))

    def definirLocalInimigo(self, tela, eventos):
        for inimigo in self.__inimigos:
            inimigo.alvo.atualizar(eventos)
            if inimigo.ativo:
                while inimigo.pos_tela[0] >= inimigo.alvo.pos_tela[0]-inimigo.alvo.dimensoes[0]-inimigo.dimensoes[0] \
                    and inimigo.pos_tela[0] <= inimigo.alvo.pos_tela[0]+inimigo.alvo.dimensoes[0]+inimigo.dimensoes[0] \
                    and inimigo.pos_tela[1] >= inimigo.alvo.pos_tela[1]-inimigo.alvo.dimensoes[1]-inimigo.dimensoes[1] \
                    and inimigo.pos_tela[1] <= inimigo.alvo.pos_tela[1]+inimigo.alvo.dimensoes[1]+inimigo.dimensoes[1]:
                    i = random.randrange(tela.get_width())
                    j = random.randrange(tela.get_height())
                    inimigo.pos_tela = (i, j)

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
