from Musica import Musica
from Textura import Textura

class Aparencia:
    def __init__(self, musica: Musica, textura: Textura):
        self.__musica = musica
        self.__textura = textura
    
    @property
    def musica(self):
        return self.__musica
    
    @property
    def textura(self):
        return self.__textura
