# Python’s random module includes a function choice(data) that returns a 
# random element from a non-empty sequence. The random module includes a 
# more basic function randrange, with parameterization similar to the built-in range function, 
# that return a random choice from the given range. Using only the randrange function, implement 
# your own version of the choice function.

from random import randrange

def my_choice(data):
    x = randrange(0,len(data))
    return data[x]


print(my_choice([1,2,3,4,5,6,7]))