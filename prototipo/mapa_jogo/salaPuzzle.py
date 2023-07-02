from .sala import Sala

class SalaPuzzle(Sala):
    def __init__(self, aparencia, sala_portas, powerups, puzzle):
        super().__init__(self, aparencia, sala_portas)
        self.__puzzle = puzzle
    
    def desenhar_resto(self):
        self.__puzzle.desenhar()
    
    def atualizar_resto(self):
        self.__puzzle.atualizar()
