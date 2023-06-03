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

class MapaJogo(Entidade):
    def __init__(self, tela, jogador):
        self.coord_sala_atual = [0, 0]
        self.initMapaJogo(tela, jogador)

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

        print(self.coord_sala_atual)

        self.getSala().desenhar()

    def initMapaJogo(self, tela, jogador):
        self.__salas = []
        self.__portas = [Porta(), Porta(), Porta(), Porta()]

        aparencia = Aparencia(Musica(), Textura())

        for i in range(2):
            linha = []
            for j in range(2):
                posicoes = [
                    [0, 0],
                    [0, 200],
                    [300, 400]
                ]

                inimigos = []
                if i == 0 and j == 0:
                    for inimigo_i in range(3):
                        inimigos.append(Inimigo(
                            tela,
                            posicoes[inimigo_i], [50, 50],
                            DesenhavelRetangulo(tela, (255, 0, 0)),
                            3, 1, 1,
                            jogador
                        ))

                linha.append(SalaInimigo(
                    Aparencia(Musica(), Textura()),
                    [],
                    inimigos
                ))

            self.__salas.append(linha)

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