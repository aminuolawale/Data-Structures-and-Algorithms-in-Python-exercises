# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
# and returns the smallest and largest numbers, in the form of a tuple of length two. Do not
# use the built-in functions min or max in implementing your solution. 

def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return [smallest, largest]


print(minmax([3,4,5,6,2,1,3,98,4,5,5,5,2,1,1,-1000]))

