#Exercise R-2.12 uses the mul method to support multiplying a Vector by a number, while Exercise R-2.14 uses the mul method to support computing a 
# dot product of two vectors. Give a single implementation of Vector. mul that uses run-timetypechecking tosupportbothsyntaxes u vand u k,where u
#  and v designate vector instances and k represents a number

class Vector:
    _cords = []
    
    def __init__(self, n, j=0):
        if type(n) == type([]):
            self._cords = [element for element in n]
        else:
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
    def __mul__(self, other):
        if type(self) == type(other):
            rv = 0
            for i in range(len(self)):
                rv += self[i] * other[i]
                return rv
        rv = Vector(len(self))
        for i in range(len(self)):
            rv[i] = self[i] * other
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
v1 = Vector([1,2,3,4,1,3,3,2])
print(v)
print(v1)