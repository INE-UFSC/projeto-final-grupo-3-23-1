from basico.entidade import Entidade
from .sala import Sala
from .porta import Porta
from basico.evento import *
from jogo.labirinto.inimigo import Inimigo
from jogo.labirinto.inimigo_que_atira import InimigoQueAtira
from jogo.labirinto.inimigo_que_segue import *
from jogo.labirinto.sala_inimigo import SalaInimigo
from jogo.labirinto.sala_porta import *
from jogo.labirinto.computador import Computador
from jogo.labirinto.powerup import *
from jogo.labirinto.sala_final import SalaFinal
from jogo.labirinto.obstaculo import *
import random
import os

import pygame as pg

class Labirinto(Entidade):
    def __init__(self, tela, jogador):
        super().__init__(tela)
        self.__coord_sala_atual = [0, 0]
        self.__salas = []
        self.__portas = []
        self.__ganhou = False
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
        sala = self.getSala()
        if not self.__ganhou and isinstance(sala, SalaFinal):
            self.__ganhou = True
            for sala_porta in sala.sala_portas:
                sala_porta.fechar() 

            pg.mixer.music.load('musica/victory-epic-music.mp3')
            pg.mixer.music.play(-1)

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
        from basico.desenhavel import DesenhavelImagem

        def adicionarSalaPorta(sala, porta, tipo):
            sala_porta = tipo(tela, sala, porta)
            porta.adicionarSalaPorta(sala_porta)
            sala.adicionarSalaPorta(sala_porta)

        def formatarPosDim(val_str):
            valores = val_str.split(',')
            w = valores[0].split('/')
            h = valores[1].split('/')
            return (self.telaW()*int(w[0])/int(w[1]), self.telaH()*int(h[0])/int(h[1]))

        def definirCorImagem(cor):
            if cor in dict_info.keys():
                if dict_info[cor] == 'branco':
                    cor_im = (255, 255, 255)
                elif dict_info[cor] == 'preto':
                    cor_im = (0, 0, 0)
            else:
                cor_im = None
            return cor_im
        
        def criarSalaInimigo(linha):
            indice = random.randrange(0, len(info_inimigo))
            dict_info = info_inimigo[indice]

            imagens = imagens_inimigo[indice]
            
            sala = SalaInimigo(tela,
                                imagens['fundo'],
                                jogador)
            linha.append(sala)

            dimen_obs = formatarPosDim(dict_info['dim_obs'])
            for num_obs in range(int(dict_info['quant_obs'])):
                pos_obs = formatarPosDim(dict_info[f'pos_obs_{num_obs}'])
                sala.addObstaculo(Obstaculo(tela, pos_obs, dimen_obs,
                                            imagens['im_obs']))

            dimen_power = (self.telaW()/35, self.telaW()/35)
            for num_power in range(int(dict_info['quant_power'])):
                pos_power = formatarPosDim(dict_info[f'pos_power_{num_power}'])
                tipo = dict_info[f'tipo_power_{num_power}']
                if tipo == 'd':
                    caminho_im_dano = os.path.join('imagens', 'powerup', 'dano.png')
                    powerup = PowerupDano(tela, pos_power, dimen_power,
                                        imagens_powerup['power_d'],
                                        0.5)
                elif tipo == 'v':
                    caminho_im_vel = os.path.join('imagens', 'powerup', 'velocidade.png')
                    powerup = PowerupVelocidadeTiro(tela, pos_power, dimen_power,
                                        imagens_powerup['power_v'],
                                        1)
                elif tipo == 'c':
                    caminho_im_cad = os.path.join('imagens', 'powerup', 'cadencia.png')
                    powerup = PowerupCadencia(tela, pos_power, dimen_power,
                                        imagens_powerup['power_c'],
                                        25)
                elif tipo == 'f':
                    caminho_im_vida = os.path.join('imagens', 'powerup', 'vida.png')
                    powerup = PowerupVida(tela, pos_power, dimen_power,
                                            imagens_powerup['power_f'],
                                            1)
                sala.addPowerup(powerup)

            dim_ini = (self.telaW()*75/1960, self.telaH()*75/1080)
            dano_ini = 1
            vel_ini = 2
            vida_ini = 3
            for num_ini in range(int(dict_info['quant_ini'])):
                pos_ini = formatarPosDim(dict_info[f'pos_ini_{num_ini}'])
                sala.addInimigo(InimigoQueSegue(self.tela, pos_ini, dim_ini, imagens['im_ini'],
                                        dano_ini, vel_ini, vida_ini, jogador))

            for num_ini_ati in range(int(dict_info['quant_ini_ati'])):
                pos_ini_ati = formatarPosDim(dict_info[f'pos_ini_ati_{num_ini_ati}'])
                nivel = int(dict_info[f'nivel_ini_ati_{num_ini_ati}'].strip())
                sala.addInimigo(InimigoQueAtira(tela, pos_ini_ati, dim_ini,
                                        imagens['im_ini'],
                                        dano_ini, vel_ini, vida_ini, jogador, nivel))
            return linha
        
        def criarSalaPuzzle(linha):
            indice = random.randrange(0, len(info_puzzle))
            puzz = info_puzzle[indice]
            arq_im_puzz = os.path.join('imagens', 'computador', puzz[1])
            linha.append(SalaPuzzle(tela,
                        DesenhavelImagem(tela, caminho_im_fundo, (self.telaW(), self.telaH())),
                        imagens_puzzle['pc'], dimen_pc, 
                        DesenhavelImagem(tela, arq_im_puzz, dimen_pc, (255, 255, 255)),
                        imagens_puzzle['acertou'], imagens_puzzle['errou'],
                        puzz[2].strip(), jogador))
            info_puzzle.pop(indice)
            return linha
        
        arq_opcoes_mapas = os.path.join('jogo', 'labirinto', 'opcoes_mapa.txt')
        with open(arq_opcoes_mapas, "r") as arquivo_opcoes_mapas:
            opcoes = arquivo_opcoes_mapas.readlines()
        mapa = opcoes[random.randrange(0, len(opcoes))].strip()

        arq_mapa = os.path.join('jogo', 'labirinto', mapa)
        with open(arq_mapa, "r") as arquivo_mapa:
            linhas = arquivo_mapa.readlines()
        
        n_linhas = len(linhas)-2
        n_colunas = int(len(linhas[0])/2 - 1)
        coord_sala_inicial = linhas[n_linhas].split()
        self.coord_sala_atual = [int(coord_sala_inicial[0]), int(coord_sala_inicial[1])]
        coord_sala_final = linhas[n_linhas+1].split()

        arq_puzz = os.path.join('jogo', 'labirinto', 'info_salas_puzzle.txt')
        with open(arq_puzz, "r") as arquivo_puzzles:
            l_puzzle = arquivo_puzzles.readlines()

        info_puzzle = []
        for i in range(len(l_puzzle)):
            puzz = l_puzzle[i]
            #l_puzzle.remove(puzz)
            puzz = puzz.split(' / ')
            caminho_im_fundo = os.path.join('imagens', 'fundos_sala_puzz', puzz[0])
            des = DesenhavelImagem(tela, caminho_im_fundo, (self.telaW(), self.telaH()))
            info_puzzle.append((des, puzz[1], puzz[2]))

        arq_ini = os.path.join('jogo', 'labirinto', 'info_salas_inimigo.txt')
        with open(arq_ini, "r") as arquivo_inimigos:
            info_salas_ini = arquivo_inimigos.readlines()

        # pre-carregamento de imagens. Essa eh provavelmente a parte que esta fazendo o jogo demorar para carregar
        info_inimigo = []
        for indice in range(len(info_salas_ini)):
            info_sala = info_salas_ini[indice]
            #info_salas_ini.remove(info_sala)
            lista_info = info_sala.split(' / ')
            dict_info = {}
            for elem in lista_info:
                lista_elem = elem.split(' - ')
                dict_info[lista_elem[0]] = lista_elem[1]
            info_inimigo.append(dict_info)

        imagens_powerup = {}
        dimen_power = (self.telaW()/35, self.telaW()/35)
        caminho_im_dano = os.path.join('imagens', 'powerup', 'dano.png')
        imagens_powerup['power_d'] = DesenhavelImagem(tela, caminho_im_dano, dimen_power, (0, 0, 0))

        caminho_im_vel = os.path.join('imagens', 'powerup', 'velocidade.png')
        imagens_powerup['power_v'] = DesenhavelImagem(tela, caminho_im_vel, dimen_power, (0, 0, 0))

        caminho_im_cad = os.path.join('imagens', 'powerup', 'cadencia.png')
        imagens_powerup['power_c'] = DesenhavelImagem(tela, caminho_im_cad, dimen_power, (0, 0, 0))

        caminho_im_vida = os.path.join('imagens', 'powerup', 'vida.png')
        imagens_powerup['power_f'] = DesenhavelImagem(tela, caminho_im_vida, dimen_power, (0, 0, 0))

        imagens_inimigo = []
        for indice in range(len(info_salas_ini)):
            imagens = {} 

            dict_info = info_inimigo[indice]

            caminho_im_fundo = os.path.join('imagens', 'fundos_sala_ini', dict_info['fundo'])
            imagens['fundo'] = DesenhavelImagem(tela, caminho_im_fundo, (self.telaW(), self.telaH()))

            dimen_obs = formatarPosDim(dict_info['dim_obs'])
            caminho_im_obs = os.path.join('imagens', 'obstaculos', dict_info['im_obs'])
            cor_im_obs = definirCorImagem('cor_im_obs')
            imagens['im_obs'] = DesenhavelImagem(tela, caminho_im_obs, dimen_obs, cor_im_obs)

            caminho_im_ini = os.path.join('imagens', 'inimigos', dict_info['im_ini'])
            cor_im_ini = definirCorImagem('cor_im_ini')
            dim_ini = (self.telaW()*75/1960, self.telaH()*75/1080)
            imagens['im_ini'] = DesenhavelImagem(tela, caminho_im_ini, dim_ini, cor_im_ini)

            imagens_inimigo.append(imagens)

        imagens_puzzle = {}
        dimen_pc = (self.telaW()/2, self.telaH()*2/3)
        arq_im_pc = os.path.join('imagens', 'computador', 'computador.png')
        imagens_puzzle['pc'] = DesenhavelImagem(tela, arq_im_pc, dimen_pc, (255, 255, 255))
        arq_im_acertou = os.path.join('imagens', 'computador', 'im_acertou.png')
        imagens_puzzle['acertou'] = DesenhavelImagem(tela, arq_im_acertou, dimen_pc, (255, 255, 255))
        arq_im_errou = os.path.join('imagens', 'computador', 'im_errou.png')
        imagens_puzzle['errou'] = DesenhavelImagem(tela, arq_im_errou, dimen_pc, (255, 255, 255))

        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                if i == int(coord_sala_final[0]) and j == int(coord_sala_final[1]):
                    arq_sala_final = os.path.join('imagens', 'sala_final', 'fundo_sala_final.jpg')
                    des_sala_final = DesenhavelImagem(tela, arq_sala_final, (self.telaW(), self.telaH()))
                    self.sala_final = SalaFinal(tela, 
                                                des_sala_final,
                                                jogador)
                    linha.append(self.sala_final)
                elif [i, j] == self.coord_sala_atual:
                    caminho_im_fundo = os.path.join('imagens', 'fundo_sala_inicial.jpg')
                    des_sala_inicial = DesenhavelImagem(tela, caminho_im_fundo, (self.telaW(), self.telaH()))
                    linha.append(Sala(tela, des_sala_inicial))
                else:
                    a = random.randint(0, 1)
                    if a == 0:
                        if len(info_puzzle) != 0:
                            linha = criarSalaPuzzle(linha)
                        else:
                            linha = criarSalaInimigo(linha)
                    else:
                        if len(info_inimigo) != 0:
                            linha = criarSalaInimigo(linha)
                        else:
                            linha = criarSalaPuzzle(linha)
             
            self.__salas.append(linha)

        SalaPortaBaixo.iniciarClasse(tela)
        SalaPortaCima.iniciarClasse(tela)
        SalaPortaDireita.iniciarClasse(tela)
        SalaPortaEsquerda.iniciarClasse(tela)

        self.__portas = []
        for n, linha in enumerate(linhas[:n_linhas]):
            p = 0
            q = 0
            for m, carac in enumerate(linha[1:]):
                if carac == '|':
                    porta = Porta()
                    self.__portas.append(porta)
                    adicionarSalaPorta(self.__salas[n][p], porta, SalaPortaDireita)
                    if m == len(linha)-3:
                        adicionarSalaPorta(self.__salas[n][0], porta, SalaPortaEsquerda)

                    else:
                        adicionarSalaPorta(self.__salas[n][p+1], porta, SalaPortaEsquerda)

                elif carac == '_':
                    porta = Porta()
                    self.__portas.append(porta)
                    adicionarSalaPorta(self.__salas[n][p], porta, SalaPortaBaixo)
                    if n == n_linhas-1:
                        adicionarSalaPorta(self.__salas[0][p], porta, SalaPortaCima)

                    else:
                        adicionarSalaPorta(self.__salas[n+1][p], porta, SalaPortaCima)

                q += 1
                if q%2 == 0:
                    p += 1


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

    @property
    def sala_final(self):
        return self.__sala_final

    @sala_final.setter
    def sala_final(self, sala):
        self.__sala_final = sala
