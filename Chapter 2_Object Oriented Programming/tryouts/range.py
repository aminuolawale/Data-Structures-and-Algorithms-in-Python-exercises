class MyRange:
    def __init__(self,start, stop=None, step=1):
        if step == 0:
            raise ValueError('Index cannot be 0')
        if not stop:
            stop,start = start,0
        self.length = (stop + step - 1 - start)//step
        self.start = start
        self.step = step
        self.stop = stop
    def __len__(self):
        return self.length
    def __getitem__(self, j):
        if -1 < j < len(self):
            return self.start + self.step*j
    def printRange(self):
        for i in range(self.length):
            print(self[i])
            
    
MyRange(2,10,1).printRange()