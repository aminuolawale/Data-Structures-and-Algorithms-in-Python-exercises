class MyIterator:

    def __init__(self, sequence):
        self.seq = sequence
        self.index = -1

    def __next__(self):
        self.index+=1
        if self.index == len(self.seq):
            raise IndexError('Out of bounds')
        return self.seq[self.index]
    def __iter__(self):
        return(self)
``