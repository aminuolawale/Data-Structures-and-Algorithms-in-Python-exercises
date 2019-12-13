#Write a short Python program that takes two arrays a and b of length n storing int values, 
# and returns the dot product of a and b. That is,it returns an array c of length n such that c[i]=a[i]·b[i], 
# for i = 0,...,n−1.

def dot_product(v1,v2):
    return sum(x*y for x,y in zip(v1,v2))

print(dot_product([1,2,3],[3,5,7]))