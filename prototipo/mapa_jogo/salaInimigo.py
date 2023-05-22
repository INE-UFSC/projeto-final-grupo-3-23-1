from sala import Sala

class SalaInimigo(Sala):
    def __init__(self, aparencia, sala_portas, powerups, inimigos):
        super().__init__(self, aparencia, sala_portas)
        self.__powerups = powerups
        self.__inimigos = inimigos
    
    def desenhar_resto(self):
        for inimigo in self.__inimigos:
            if inimigo.ativo:
                inimigo.desenhar()
        #desenhar powerups quando forem implementados
    
    def atualizar_resto(self):
        for inimigo in self.__inimigos:
            inimigo.atualizar()

    @property
    def inimigos(self):
        return self.__inimigos