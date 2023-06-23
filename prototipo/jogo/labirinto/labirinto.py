from basico.entidade import Entidade
from .sala import Sala
from .porta import Porta
from basico.evento import *
from jogo.labirinto.aparencia import Aparencia
from jogo.labirinto.musica import Musica
from jogo.labirinto.textura import Textura
from jogo.labirinto.inimigo import Inimigo
from jogo.labirinto.sala_inimigo import SalaInimigo
from jogo.labirinto.sala_porta import *
from jogo.labirinto.puzzle import Puzzle
from jogo.labirinto.powerup import *
from jogo.labirinto.sala_final import SalaFinal
from jogo.labirinto.obstaculo import *

class Labirinto(Entidade):
    def __init__(self, tela, jogador):
        super().__init__(tela)
        self.__coord_sala_atual = [0, 0]
        self.__salas = []
        self.__portas = []
        self.initLabirinto(tela, jogador)

    def getSala(self):
        i, j = self.coord_sala_atual
        return self.__salas[i][j]
    
    def getCoorSala(self, sala):
        for i, linha in enumerate(self.__salas):
            for j, coluna in enumerate(linha):
                if coluna == sala:
                    return [i, j]

    def atualizar(self, eventos):
        self.getSala().atualizar(eventos)
        self.tentarMudarSala(eventos)
    
    def desenhar(self):
        # @incompleto: mover para Aparencia da Sala
#        t_sala_atual = tuple(self.coord_sala_atual)
#
#        if t_sala_atual == (0, 0):
#            cor_fundo = (255, 255, 255)
#        elif t_sala_atual == (0, 1):
#            cor_fundo = (0, 0, 0)
#        elif t_sala_atual == (1, 0):
#            cor_fundo = (200, 230, 255)
#        elif t_sala_atual == (1, 1):
#            cor_fundo = (232, 202, 45)
#
#        self.tela.fill(cor_fundo)

        #print(self.coord_sala_atual)

        self.getSala().desenhar()

    def initLabirinto(self, tela, jogador):
        self.__salas = []
        self.__portas = [Porta(), Porta(), Porta(), Porta(), Porta(), Porta(), Porta(), Porta(), Porta()]

        dimens_powerup = (self.telaW()/1980*40, self.telaH()/1080*40)
        powerups =        [PowerupVelocidadeTiro(tela, (self.telaW()/1980*300, self.telaH()/1080*400),
                                                dimens_powerup, DesenhavelRetangulo(tela, (255, 255, 0), dimens_powerup), 2),
                           PowerupCadencia(tela, (self.telaW()/1980*300, self.telaH()/1080*600),
                                          dimens_powerup, DesenhavelRetangulo(tela, (115, 41, 165), dimens_powerup), 200),
                           PowerupDano(tela, (self.telaW()/1980*300, self.telaH()/1080*800), 
                                      dimens_powerup, DesenhavelRetangulo(tela, (149, 27, 27), dimens_powerup), 1)]

        dimens_obstaculo = (self.telaW()/1980*100, self.telaH()/1080*100)
        obstaculos = [
            Obstaculo(
                tela,
                (self.telaW()/1980*500, self.telaH()/1080*800), 
                dimens_obstaculo,
                DesenhavelRetangulo(tela, (27, 27, 27), dimens_obstaculo)
            ),
            Obstaculo(
                tela,
                (self.telaW()/1980*500, self.telaH()/1080*900), 
                dimens_obstaculo,
                DesenhavelRetangulo(tela, (27, 27, 27), dimens_obstaculo)
            ),
            Obstaculo(
                tela,
                (self.telaW()/1980*599, self.telaH()/1080*800), 
                dimens_obstaculo,
                DesenhavelRetangulo(tela, (27, 27, 27), dimens_obstaculo)
            )
        ]

        for i in range(2):
            linha = []
            for j in range(2):
                linha.append(SalaInimigo(tela, 'definir desenhavel', [], jogador))

            self.__salas.append(linha)
        
        self.__salas[0].append(SalaPuzzle(tela, 'definir desenhavel', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a', jogador))
        self.__salas[1].append(SalaPuzzle(tela, 'definir desenhavel', 'responda b', 'b', jogador))
        self.sala_final = SalaFinal(tela, 'definir desenhavel', jogador)
        self.__salas.append([self.sala_final])
        self.__salas[0][0].powerups = powerups
        self.__salas[0][0].obstaculos = obstaculos

        def adicionarSalaPorta(sala, porta, tipo):
            sala_porta = tipo(tela, sala, porta)
            porta.adicionarSalaPorta(sala_porta)
            sala.adicionarSalaPorta(sala_porta)

        # 0,0 -0- 0,1
        #  |       |
        #  3       1 
        #  |       |
        # 1,0 -2- 1,1

        adicionarSalaPorta(self.__salas[0][0], self.__portas[0], SalaPortaDireita)
        adicionarSalaPorta(self.__salas[0][1], self.__portas[0], SalaPortaEsquerda)
        adicionarSalaPorta(self.__salas[0][1], self.__portas[1], SalaPortaBaixo)
        adicionarSalaPorta(self.__salas[1][1], self.__portas[1], SalaPortaCima)
        adicionarSalaPorta(self.__salas[1][1], self.__portas[2], SalaPortaEsquerda)
        adicionarSalaPorta(self.__salas[1][0], self.__portas[2], SalaPortaDireita)
        adicionarSalaPorta(self.__salas[1][0], self.__portas[3], SalaPortaCima)
        adicionarSalaPorta(self.__salas[0][0], self.__portas[3], SalaPortaBaixo)
        adicionarSalaPorta(self.__salas[0][1], self.__portas[4], SalaPortaDireita)
        adicionarSalaPorta(self.__salas[0][2], self.__portas[4], SalaPortaEsquerda)
        adicionarSalaPorta(self.__salas[0][2], self.__portas[5], SalaPortaBaixo)
        adicionarSalaPorta(self.__salas[1][2], self.__portas[5], SalaPortaCima)
        adicionarSalaPorta(self.__salas[1][2], self.__portas[6], SalaPortaEsquerda)
        adicionarSalaPorta(self.__salas[1][1], self.__portas[6], SalaPortaDireita)
        adicionarSalaPorta(self.__salas[2][0], self.__portas[7], SalaPortaCima)
        adicionarSalaPorta(self.__salas[1][0], self.__portas[7], SalaPortaBaixo)

        adicionarSalaPorta(self.__salas[1][0], self.__portas[8], SalaPortaEsquerda)
        adicionarSalaPorta(self.__salas[1][2], self.__portas[8], SalaPortaDireita)

    def tentarMudarSala(self, eventos):
        from jogo.jogador.jogador import Jogador

        for evento in eventos:
            if isinstance(evento, EventoColisao) \
                    and evento.possuiTipo(SalaPorta) \
                    and evento.possuiTipo(Jogador) \
                    and evento.getElemDoTipo(SalaPorta).porta.aberta:
                
                sala_porta_colidida = evento.getElemDoTipo(SalaPorta)
                porta_colidida = sala_porta_colidida.porta
                for s in porta_colidida.sala_portas:
                    if s != sala_porta_colidida:
                        prox_sala_porta = s
                        break
                self.coord_sala_atual = self.getCoorSala(prox_sala_porta.sala)
                if isinstance(prox_sala_porta.sala, SalaInimigo):
                    prox_sala_porta.sala.definirLocalInimigo(prox_sala_porta.tela, eventos)
                return True
        return False
    
        '''
                movimentacao = {
                    SalaPortaEsquerda: [0, -1],
                    SalaPortaDireita:  [0, 1],
                    SalaPortaCima:     [-1, 0],
                    SalaPortaBaixo:    [1, 0]
                }

                tipo_sala_porta = type(evento.getElemDoTipo(SalaPorta))

                for i in range(len(self.coord_sala_atual)):
                    self.coord_sala_atual[i] = (self.coord_sala_atual[i] + movimentacao[tipo_sala_porta][i]) % 2

                    if self.coord_sala_atual[i] < 0:
                        self.coord_sala_atual[i] += 2
                return True
        return False


    
        '''

    @property
    def coord_sala_atual(self):
        return self.__coord_sala_atual

    @coord_sala_atual.setter
    def coord_sala_atual(self, coord_sala_atual):
        self.__coord_sala_atual = coord_sala_atual

    @property
    def salas(self):
        return self.__salas

    @salas.setter
    def salas(self, salas):
        self.__salas = salas

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas

