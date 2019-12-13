#The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector 
# with all coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a 
# parameter that is some iterable type representing a sequence of numbers, and to create a vector with dimension 
# equal to the length of that sequence and coordinates equal to the sequence values. For example, Vector([4, 7, 5]) 
# would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these 
# forms is acceptable; that is, if a single integer is sent, it produces a vector of that dimension with all zeros, but 
# if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.

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
