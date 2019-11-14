#In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. 
# The third of those implementations, from page 41, was the most efﬁcient, but we noted that it did not yield the factors 
# nincreasing order. Modifythegeneratorsothatitreports factors in increasing order, while maintaining its general 
# performance advantages

def factors(n):
    k=1
    p = None
    while k*k  < n:
        if n % k == 0:
            if k == p :
                break
            yield k
            p = n // k
            yield p
            if k == p :
                break
        k+=1

def sorted_factors(n):
    k=1
    while k*k  < n:
        if n % k == 0:
            yield k
        k+=1
    if k*k == n:
        yield k
    
    while k <= n//2:
        k+=1
        if n % k == 0:
            yield k
    yield n

for factor in sorted_factors(512):
    print(factor)
