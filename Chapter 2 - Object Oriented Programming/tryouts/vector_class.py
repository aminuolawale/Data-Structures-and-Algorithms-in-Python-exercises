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
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('vectors must be of equal length')
        rv = Vector(len(self))
        for i in range(len(rv)):
            rv[i] = self[i] - other[i]
        return rv
    def __repr__(self):
        return 'Vector->{}'.format(self._cords)

my_vector = Vector(3)
my_vector[2] = 5
my_vector_1 = Vector(3,4)
print(my_vector + my_vector_1)
print(my_vector - my_vector_1)
print(my_vector != my_vector_1)
my_vector_3 = Vector(4,3)
try:
    print(my_vector- my_vector_3)
except:
    print('hmmm')
for element in my_vector_3:
    print(element)