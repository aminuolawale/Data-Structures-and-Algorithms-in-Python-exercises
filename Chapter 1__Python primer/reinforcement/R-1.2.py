# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, 
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators. 
def is_even(k):
    if k == 0 :
        return True
    elif k == 1:
        return False
    else:
        return is_even(k-2)


print(is_even(601))