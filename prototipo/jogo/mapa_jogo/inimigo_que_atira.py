from mapa_jogo.inimigo import Inimigo
from jogo.jogador.tiro import Tiro

class inimigo_que_atira(Inimigo):
    def __init__(self, nivel):
        super().__init__()
        self.__nivel = nivel

   
    def atirar(self):
        self.__tiros.append(Tiro(
            self.tela,
            self.pos_tela,
            (20, 20),
            self.__direction
        ))

