#Write a Python program that can take a positive integer greater than 2 as input 
# and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.

def div_by_two(number):
    count=0
    while number >= 2:
        number/=2
        count+=1

    return count


print(div_by_two(9))