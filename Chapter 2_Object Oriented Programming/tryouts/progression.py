class Progression:
    def __init__(self, start=0):
        self.current = start

    def _advance(self):
        self.current+=1

    def __next__(self):
        if self.current == None:
            raise StopIteration('out of bounds')
        value = self.current
        self._advance()
        return value

    def __iter__(self):
        return self
    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)) )
        

if __name__ == '__main__':
    Progression().print_progression(5)
    
