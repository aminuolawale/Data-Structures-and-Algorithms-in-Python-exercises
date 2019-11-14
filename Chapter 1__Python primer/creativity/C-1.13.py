#Write a pseudo-code description of a function that reverses a list of n integers, 
# so that the numbers are listed in the opposite order than they were before, and compare 
# this method to an equivalent Python function for doing the same thing.



# pseudocode
# funtion(list):
#     reversed_list = []
#     for i in range(0, reversed_list_length):
#         append list[i] to reversed_list
#     return reversed_list


def reverse_list_of_integers(list):
    reversed_array=[]
    for i in range(0, len(list)):
        reversed_array.append(list[len(list)-i-1])
    return reversed_array

print(reverse_list_of_integers([1,2,3,4,5]))

