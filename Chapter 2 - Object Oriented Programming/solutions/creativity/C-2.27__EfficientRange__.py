#In Section 2.3.5, we note that our version of the Range class has implicit support for iteration, due to its explicit 
# support of both len and getitem . The class also receives implicit support of the Boolean test, “k in r” for Range r. 
# This test is evaluated based on a forward iteration through the range, as evidenced by the relative quickness of the 
# test 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a more efﬁcient implementation of the contains
#  method to determine whether a particular value lies within a given range. The running time of your method should be 
# independent of the length of the range.

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
        if -1 < j < self.length:
            return self.start + self.step*j
        raise IndexError('index out of range')
    def __contains__(self, item):
        if self.start <= item < self.stop and int(item/self.step) == item/self.step:
            return True
        return False

    def printRange(self):
        for i in range(self.length):
            print(self[i])

r = MyRange(2,1000,0.01)
print(2 in r)