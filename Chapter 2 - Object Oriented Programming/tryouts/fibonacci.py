from tryouts.progression import Progression

class Fibonacci(Progression):
    def __init__(self, first=0, second=1):
        self.prev = second - first
        super().__init__(first)

    def _advance(self):
        self.prev, self.current = self.current, self.current + self.prev

if __name__ == '__main__':
    Fibonacci(3,4).print_progression(10)
