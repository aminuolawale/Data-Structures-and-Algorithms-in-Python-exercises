a = [1,11,3]
b = [4,5,6]
c = [7,5,9]
def disjoint(A,B,C):
    for a in A:
        is_in_b = False
        if B.count(a) > 0:
            is_in_b = True
        if is_in_b:
            is_in_c = False
            if C.count(a) >0:
                is_in_c = True
            if is_in_b and is_in_c:
                return False
    return True
print(disjoint(a,b,c))

