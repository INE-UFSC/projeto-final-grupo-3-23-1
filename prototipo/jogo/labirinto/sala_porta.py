from abc import ABC, abstractmethod
from .sala import Sala
from .porta import Porta
from basico.entidade_tela import EntidadeTela
from basico.desenhavel import DesenhavelImagem
from .sala_inimigo import SalaInimigo
from .sala_puzzle import SalaPuzzle
import os

class SalaPorta(EntidadeTela, ABC):
    @abstractmethod
    def __init__(self, tela, sala: Sala, porta: Porta, pos_tela, dimensoes, arq_im_porta_trancada, arq_im_porta_aberta):
        desenhavel = DesenhavelImagem(tela, arq_im_porta_trancada, dimensoes, (0, 0, 0))
        super().__init__(tela, pos_tela, dimensoes, desenhavel, solido=True, movel=False)
        self.__sala = sala
        self.__porta = porta
        self.__arq_im_porta_aberta = arq_im_porta_aberta
        self.__desenhavel_sala_porta_trancada = DesenhavelImagem(self.tela, arq_im_porta_trancada, self.dimensoes)
    
    def atualizar(self, eventos):
        if not self.__porta.aberta:
            if isinstance(self.__sala, SalaInimigo):
                abrir = True
                for inimigo in self.__sala.inimigos:
                    if inimigo.ativo:
                        abrir = False
                        break
                if abrir:
                    self.abrir()

            elif isinstance(self.__sala, SalaPuzzle):
                if self.__sala.puzzle.resolvido:
                    self.abrir()
            else:
                from .sala_final import SalaFinal
                if not isinstance(self.__sala, SalaFinal):
                    self.abrir()

    def abrir(self):
        self.__porta.abrir()
        for sala_porta in self.__porta.sala_portas:
            sala_porta.desenhavel = DesenhavelImagem(self.tela, self.__arq_im_porta_aberta, self.dimensoes)

    def fechar(self):
        self.__porta.fechar()
        for sala_porta in self.__porta.sala_portas:
            sala_porta.desenhavel = self.__desenhavel_sala_porta_trancada

    @property
    def porta(self):
        return self.__porta
    
    @property
    def sala(self):
        return self.__sala
    

class SalaPortaBaixo(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (tela.get_width()/2, tela.get_height())
        dimensoes = (tela.get_height()/4, tela.get_width()/15)
        arq_im_porta_aberta = os.path.join('imagens', 'portas', 'porta_horizontal.png')
        arq_im_porta_trancada = os.path.join('imagens', 'portas', 'porta_baixo_trancada.png')
        super().__init__(tela, sala, porta, pos_tela, dimensoes, arq_im_porta_trancada, arq_im_porta_aberta)


class SalaPortaCima(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (tela.get_width()/2, 0)
        dimensoes = (tela.get_height()/4, tela.get_width()/15)
        arq_im_porta_aberta = os.path.join('imagens', 'portas', 'porta_horizontal.png')
        arq_im_porta_trancada = os.path.join('imagens', 'portas', 'porta_cima_trancada.png')
        super().__init__(tela, sala, porta, pos_tela, dimensoes, arq_im_porta_trancada, arq_im_porta_aberta)

class SalaPortaDireita(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (tela.get_width(), tela.get_height()/2)
        dimensoes = (tela.get_width()/15, tela.get_height()/4)
        arq_im_porta_aberta = os.path.join('imagens', 'portas', 'porta_vertical.png')
        arq_im_porta_trancada = os.path.join('imagens', 'portas', 'porta_vertical_trancada.png')
        super().__init__(tela, sala, porta, pos_tela, dimensoes, arq_im_porta_trancada, arq_im_porta_aberta)

class SalaPortaEsquerda(SalaPorta):
    def __init__(self, tela, sala: Sala, porta: Porta):
        pos_tela = (0, tela.get_height()/2)
        dimensoes = (tela.get_width()/15, tela.get_height()/4)
        arq_im_porta_aberta = os.path.join('imagens', 'portas', 'porta_vertical.png')
        arq_im_porta_trancada = os.path.join('imagens', 'portas', 'porta_vertical_trancada.png')
        super().__init__(tela, sala, porta, pos_tela, dimensoes, arq_im_porta_trancada, arq_im_porta_aberta,)
