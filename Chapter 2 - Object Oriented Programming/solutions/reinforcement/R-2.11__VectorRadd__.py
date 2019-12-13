#In Section 2.3.3, we note that our Vector class supports a syntax such as v = u + [5, 3, 10,−2, 1], in which the sum of 
# a vector and list returns a new vector. However, the syntax v = [5, 3, 10,−2, 1] + u is illegal. Explain how the Vector 
# class deﬁnition can be revised so that this syntax generates a new vector.


# We would implement an __radd__ method for right addition

class Vector:
    _cords = []
    
    def __init__(self, n,j=0):
        self._cords = [j for _ in range(n)]
    def __len__(self):
        return len(self._cords)
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
    def __neq__(self, other):
        for i in range(len(self)):
            if self[i] != other[i]:
                return True
        return False
    def __setitem__(self,index, value):
        self._cords[index] = value
    def __getitem__(self, index):
        return self._cords[index]
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError('vectors must be of equal length')
        rv = Vector(len(self))
        for i in range(len(rv)):
            rv[i] = self[i] + other[i]
        return rv
    def __radd__(self,other):
        if len(self) != len(other):
            raise ValueError('vectors must be of equal length')
        rv = Vector(len(self))
        for i in range(len(rv)):
            rv[i] = self[i] + other[i]
        return rv
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('vectors must be of equal length')
        rv = Vector(len(self))
        for i in range(len(rv)):
            rv[i] = self[i] - other[i]
        return rv
    def __neg__(self):
        rv = Vector(len(self))
        for i in range(len(self)):
            rv[i] = -self[i]
        return rv
    def __repr__(self):
        return 'Vector->{}'.format(self._cords)

v = Vector(5,3)
v = -v
w = [1,2,3,4,5] + v
print(w)