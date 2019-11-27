#The collections.Sequence abstract base class does not provide support for comparing two sequences to each other. 
# Modify our Sequence class from Code Fragment 2.14 to include a deﬁnition for the eq method, so that expression 
# seq1 == seq2 will return True precisely when the two sequences are element by element equivalent.

from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self):
        """ """

    @abstractmethod
    def __getitem__(self, j):
        """ """

    def __contains__(self, item):
        for j in range(len(self)):
            if self[j] ==  item:
                return True
        return False
    def __eq__(self, other):
        for j in range(len(self)):
            if self[j] != other[j]:
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
