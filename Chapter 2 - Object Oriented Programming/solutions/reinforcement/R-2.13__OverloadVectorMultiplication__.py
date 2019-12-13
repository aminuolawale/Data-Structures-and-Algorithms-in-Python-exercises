#Exercise R-2.12 asks for an implementation of mul , for theVector class of Section 2.3.3, to provide support for the 
# syntax v*3. Implement the rmul method, to provide additional support for syntax 3*v.

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
    def __mul__(self, factor):
        rv = Vector(len(self))
        for i in range(len(self)):
            rv[i] = self[i] * factor
        return rv
    def __rmul__(self, factor):
        rv = Vector(len(self))
        for i in range(len(self)):
            rv[i] = self[i] * factor
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
w = 3*v
print(w)