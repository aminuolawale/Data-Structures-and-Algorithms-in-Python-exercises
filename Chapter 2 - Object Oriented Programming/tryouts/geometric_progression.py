from progression import Progression

class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self.base = base
    def _advance(self):
        self.current*=self.base

GeometricProgression(4).print_progression(10)