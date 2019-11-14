def factors(n):
    for k in range(1, n+1):
        if n % k ==0:
            yield k

for p in factors(5):
    print( p)