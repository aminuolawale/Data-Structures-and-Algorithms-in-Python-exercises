import random
from random import choice, randint

def stringify_list(l):
    m=''
    for digit in l:
        m+=digit

    return m

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

    
def my_shuffle(original_list):
    shuffled_list = []
    while len(shuffled_list) < len(original_list):
        is_distinct = False
        while not is_distinct:
            randomly_chosen = original_list[randint(0,len(original_list)-1)]
            if randomly_chosen in shuffled_list:
                randomly_chosen = original_list[randint(0,len(original_list)-1)]
            else:
                shuffled_list.append(randomly_chosen)
                break
    return shuffled_list

def permute_string(s):
    chars = s.split(' ')
    permuted_strings = []
    for _ in range(0, factorial(len(chars))):
        permuted = my_shuffle(chars)
        while permuted in permuted_strings:
            permuted = my_shuffle(chars)
        permuted_strings.append(stringify_list(permuted))
    return permuted_strings



for permutation in permute_string('c a t d o g'):
    print(permutation)
