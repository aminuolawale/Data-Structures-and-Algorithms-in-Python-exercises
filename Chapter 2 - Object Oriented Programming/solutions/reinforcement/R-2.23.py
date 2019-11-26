#In similar spirit tothe previous problem, augment theSequence class with method lt , to support lexicographic comparison seq1 < seq2.
class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self):

    @abstractmethod
    def __getitem__(self, j):

    def __contains__(self, item):
        for j in range(len(self)):
            if self[j] ==  item:
                return True
        return False
    def __eq__(self, other):
        for j in range(len(self)):
            if self[j] == other[j]:
                return False
        return True
    def __lt__(self, other):
        for j in range(len(self)):
            if self[j] > other[j]:
                return False
        return True
    def index(self, item):
        for j in range(len(self)):
            if self[j] ==  item:
                return j
        raise ValueError('value not in sequence')
    def count(self, item):
        k = 0
        for j in range(len(self)):
            if self[j] == item:
                k+=1
        return k