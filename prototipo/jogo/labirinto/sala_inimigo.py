from .sala import Sala
import random

from basico.desenhavel import DesenhavelRetangulo


class SalaInimigo(Sala):
    def __init__(self, tela, desenhavel, jogador):
        super().__init__(tela, desenhavel)
        self.__powerups = []
        self.__inimigos = []
        self.__obstaculos = []

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
        from .inimigo_que_atira import InimigoQueAtira
        colisores = super().getColisores()
        
        for inimigo in self.__inimigos:
            if inimigo.ativo:
                colisores.append(inimigo)
            if type(inimigo) == InimigoQueAtira and inimigo.ativo:
                colisores.extend(inimigo.getColisores())

        for powerup in self.powerups:
            if powerup.ativo:
                colisores.append(powerup)

        colisores.extend(self.obstaculos)

        return colisores
    
    def desenharResto(self):
        for powerup in self.powerups:
            if powerup.ativo:
                powerup.desenhar()

        for obstaculo in self.obstaculos:
            obstaculo.desenhar()

        for inimigo in self.__inimigos:
            if inimigo.ativo:
                inimigo.desenhar()
    
    def atualizarResto(self, eventos):
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
    
    @property
    def obstaculos(self):
        return self.__obstaculos

    def addInimigo(self, inimigo):
        from .inimigo import Inimigo
        if isinstance(inimigo, Inimigo):
            self.__inimigos.append(inimigo)

    def addPowerup(self, powerup):
        from .powerup import Powerup
        if isinstance(powerup, Powerup):
            self.__powerups.append(powerup)

    def addObstaculo(self, obs):
        from .obstaculo import Obstaculo
        if isinstance(obs, Obstaculo):
            self.__obstaculos.append(obs)
