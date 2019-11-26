# Give a single command that computes the sum from Exercise R-1.4, relying on Python’s 
# comprehension syntax and the built-in sum function.

def squares_sum(n):
    return sum(x*x for x in range(1,n))


print(squares_sum(50)) 