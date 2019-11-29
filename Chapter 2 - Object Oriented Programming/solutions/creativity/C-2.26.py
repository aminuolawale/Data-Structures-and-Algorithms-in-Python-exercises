#The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. Implement a class named 
# ReversedSequenceIterator that serves as a reverse iterator for any Python sequence type. The ﬁrst call to next should 
# return the last element of the sequence, the second call to next should return the second-to-last element, and so forth.

class SequenceIterator:
    def _init__(self, sequence):
        self._sequence = sequence
        self._k = len(sequence)

    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return self._sequence[self._k]
        else:
            raise StopIteration('Index out of bounds')
    def __iter__(self):
        return self
         