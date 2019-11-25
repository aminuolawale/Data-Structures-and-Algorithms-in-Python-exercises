#Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair 
# of numbers in the sequence whose product is odd.


def odd_product_pair(data):
    data = set(data)
    for i in data:
        for j in data:
            if i == j :
                continue
        if i*j % 2 == 1:
            return True
    return False


print(odd_product_pair([2,4,6,8,9,10]))