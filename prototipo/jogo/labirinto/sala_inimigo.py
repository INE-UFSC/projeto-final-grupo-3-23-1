from .sala import Sala
import random

from basico.desenhavel import DesenhavelRetangulo


class SalaInimigo(Sala):
    def __init__(self, tela, desenhavel, powerups, jogador):
        super().__init__(tela, desenhavel)
        self.__powerups = powerups
        self.__inimigos = []
        self.__obstaculos = []
        self.criarInimigos(jogador, tela)

    def criarInimigos(self, jogador, tela):
        from .inimigo import Inimigo
        from .inimigo_que_atira import InimigoQueAtira

        for i in range(random.randrange(2, 5)):
            i = random.randrange(tela.get_width())
            j = random.randrange(tela.get_height())
            posicoes = (i, j)

            dimens_inimigo = (self.telaW()*50/1960, self.telaH()*50/1080)
            self.__inimigos.append(Inimigo(tela, posicoes, dimens_inimigo, 
                                           DesenhavelRetangulo(tela, (255, 0, 0), dimens_inimigo), 1, 2, 3, jogador))
            
        self.__inimigos.append(InimigoQueAtira(tela, posicoes, dimens_inimigo, 
                                           DesenhavelRetangulo(tela,  (255, 192, 203), dimens_inimigo), 1, 2, 3, jogador, 1))
            

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

    @powerups.setter
    def powerups(self, powerups):
        self.__powerups = powerups

    @obstaculos.setter
    def obstaculos(self, obstaculos):
        self.__obstaculos = obstaculos

    
