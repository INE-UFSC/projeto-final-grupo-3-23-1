from basico.entidade import Entidade
from .sala import Sala
from .porta import Porta
from basico.evento import *
from jogo.mapa_jogo.aparencia import Aparencia
from jogo.mapa_jogo.musica import Musica
from jogo.mapa_jogo.textura import Textura
from jogo.mapa_jogo.inimigo import Inimigo
from jogo.mapa_jogo.sala_inimigo import SalaInimigo
from jogo.mapa_jogo.sala_porta import *
from jogo.mapa_jogo.puzzle import Puzzle
from jogo.mapa_jogo.powerup import *
from jogo.mapa_jogo.sala_final import SalaFinal
from jogo.mapa_jogo.obstaculo import *

class MapaJogo(Entidade):
    def __init__(self, tela, jogador):
        self.coord_sala_atual = [0, 0]
        self.tela_w = tela.get_width()
        self.tela_h = tela.get_height()
        self.initMapaJogo(tela, jogador)

    @property
    def salas(self):
        return self.__salas

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

    def initMapaJogo(self, tela, jogador):
        self.__salas = []
        self.__portas = [Porta(), Porta(), Porta(), Porta(), Porta(), Porta(), Porta(), Porta(), Porta()]

        powerups =        [PowerupVelocidadeTiro(tela, (self.tela_w/1980*300, self.tela_h/1080*400),
                                                (self.tela_w/1980*40, self.tela_h/1080*40), DesenhavelRetangulo(tela, (255, 255, 0)), 2),
                           PowerupCadencia(tela, (self.tela_w/1980*300, self.tela_h/1080*600),
                                          (self.tela_w/1980*40, self.tela_h/1080*40), DesenhavelRetangulo(tela, (115, 41, 165)), 200),
                           PowerupDano(tela, (self.tela_w/1980*300, self.tela_h/1080*800), 
                                      (self.tela_w/1980*40, self.tela_h/1080*40), DesenhavelRetangulo(tela, (149, 27, 27)), 1)]

        obstaculos = [Obstaculo(tela, (self.tela_w/1980*500, self.tela_h/1080*800), 
                                      (self.tela_w/1980*100, self.tela_h/1080*100), DesenhavelRetangulo(tela, (27, 27, 27))),
                      Obstaculo(tela, (self.tela_w/1980*500, self.tela_h/1080*900), 
                                      (self.tela_w/1980*100, self.tela_h/1080*100), DesenhavelRetangulo(tela, (27, 27, 27))),
                      Obstaculo(tela, (self.tela_w/1980*599, self.tela_h/1080*800), 
                                      (self.tela_w/1980*100, self.tela_h/1080*100), DesenhavelRetangulo(tela, (27, 27, 27)))]
        for i in range(2):
            linha = []
            for j in range(2):
                linha.append(SalaInimigo(tela, 'definir desenhavel', [], jogador))

            self.__salas.append(linha)
        
        self.__salas[0].append(SalaPuzzle('definir desenhavel', tela, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a', jogador))
        self.__salas[1].append(SalaPuzzle('definir desenhavel', tela, 'responda b', 'b', jogador))
        self.sala_final = SalaFinal(tela, 'definir desenhavel', jogador)
        self.__salas.append([self.sala_final])
        self.__salas[0][0].powerups = powerups
        self.__salas[0][0].obstaculos = obstaculos

        def adicionarSalaPorta(sala, porta, tipo):
            sala_porta = tipo(tela, sala, porta)
            porta.adicionar_sala_porta(sala_porta)
            sala.adicionar_sala_porta(sala_porta)

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
