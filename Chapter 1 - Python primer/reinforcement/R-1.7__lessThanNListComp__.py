# Give a single command that computes the sum from Exercise R-1.6, relying on Python’s 
# comprehension syntax and the built-in sum function.

def odd_squares_sum(n):
    return sum(x*x for x in range(1,n) if x%2==1)


print(odd_squares_sum(6))