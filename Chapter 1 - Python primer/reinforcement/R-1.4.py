# Write a short Python function that takes a positive integer n and returns the sum of the squares of 
# all the positive integers smaller than n. 

def squares_sum(n):
    sum = 0
    for number in range(0,n):
        sum+=number**2
    return sum

print(squares_sum(3)) 