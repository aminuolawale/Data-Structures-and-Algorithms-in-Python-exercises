def reverse_array(array):
    reversed_array=[]
    for i in range(0,len(array)):
        reversed_array.append(array[len(array) -i -1])
    return reversed_array

print(reverse_array([1,2,3,4,5,6]))