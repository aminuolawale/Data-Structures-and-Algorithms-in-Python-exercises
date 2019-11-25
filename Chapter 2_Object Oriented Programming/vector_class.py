class Vector:
    _data=[]

    def __repr__(self):
        return f'Vector->{self._data}'

    def right_push(self,*value):
        for entry in value:
            self._data.append(entry)
    
    def left_push(self, *value):
        if len(self._data) != 0:
            x = self._data
            self._data = [*value]
            self._data += x
        else:
            for entry in value:
                self._data.append(entry)


v = Vector()
v.right_push(5,6,7,8,9,10)
v.left_push(0,9,1)
print(v)