from progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self,increment, start=0):
        super().__init__(start)
        self.increment = increment

    def _advance(self):
        self.current+= self.increment

ArithmeticProgression(2,3).print_progression(10)
    
        