from .sala import Sala
import random

from basico.desenhavel import DesenhavelRetangulo
from .powerup import *


class SalaInimigo(Sala):
    def __init__(self, tela, desenhavel, powerups, jogador):
        super().__init__(desenhavel)
        self.__inimigos = []
        self.criarInimigos(jogador, tela)

        self.__powerups = [PowerupVelocidadeTiro(tela, (300, 400), (40, 40), DesenhavelRetangulo(tela, (255, 255, 0)), 2),
                           PowerupCadencia(tela, (300, 600), (40, 40), DesenhavelRetangulo(tela, (115, 41, 165)), 100),
                           PowerupDano(tela, (300, 800), (40, 40), DesenhavelRetangulo(tela, (149, 27, 27)), 1)]

    def criarInimigos(self, jogador, tela):
        from .inimigo import Inimigo
        for i in range(random.randrange(2, 5)):
            i = random.randrange(tela.get_width())
            j = random.randrange(tela.get_height())
            posicoes = (i, j)
            self.__inimigos.append(Inimigo(tela,posicoes, [tela.get_width()*50/1960, tela.get_height()*50/1080], 
                                           DesenhavelRetangulo(tela, (255, 0, 0)), 1, 2, 3, jogador))
            

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

        for powerup in self.powerups:
            if powerup.ativo:
                powerup.desenhar()
    
    def atualizar_resto(self, eventos):
        for inimigo in self.__inimigos:
            if inimigo.ativo:
                inimigo.atualizar(eventos)

        for powerup in self.powerups:
            if powerup.ativo:
                powerup.atualizar(eventos)

    @property
    def inimigos(self):
        return self.__inimigos
    
    @property
    def powerups(self):
        return self.__powerups