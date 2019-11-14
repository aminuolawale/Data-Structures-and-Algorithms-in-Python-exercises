class Vector:
    _data=[]

    def __repr__(self):
        return f'Vector->{self._data}'

    def _right_push(self,*value):
        for entry in value:
            self._data.append(entry)
    
    def _left_push(self, *value):
        if len(self._data) != 0:
            x = self._data
            self._data = [*value]
            self._data += x
        else:
            for entry in value:
                self._data.append(entry)


v = Vector()
v._right_push(5,6,7,8,9,10)
v._left_push(0,9,1)
print(v)