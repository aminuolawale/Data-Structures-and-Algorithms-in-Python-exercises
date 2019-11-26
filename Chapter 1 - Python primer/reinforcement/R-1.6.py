# Write a short Python function that takes a positive integer n and returns 
# the sum of the squares of all the odd positive integers smaller than n

def squared_odd_sum(n):
    sum = 0
    for number in range(n):
        if number%2 == 0:
            continue
        sum += number**2
    return sum

print(squared_odd_sum(5))
