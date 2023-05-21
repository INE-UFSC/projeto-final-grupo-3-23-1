from sala import Sala

class SalaInimigo(Sala):
    def __init__(self, aparencia, sala_portas, powerups, inimigos):
        super().__init__(self, aparencia, sala_portas)
        self.__powerups = powerups
        self.__inimigos = inimigos
    
    def desenhar_resto(self):
        for inimigo in self.__inimigos:
            inimigo.desenhar()
    
    def atualizar_resto(self):
        for inimigo in self.__inimigos:
            inimigo.atualizar()
