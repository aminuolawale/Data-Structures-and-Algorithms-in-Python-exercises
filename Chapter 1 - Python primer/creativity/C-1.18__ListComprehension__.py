#Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

def progression():
    return list(x*(x+1) for x in range(0,10))

print(progression())