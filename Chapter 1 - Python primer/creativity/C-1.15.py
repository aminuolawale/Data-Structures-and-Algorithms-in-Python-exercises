#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from 
# each other (that is, they are distinct).
def has_distinct_elements(data):
    s = set(data)
    if len(data) != len(s):
        return False
    else:
        return True

def has_distinct_elements_1(data):
    s=[]
    for d in data:
        if d in s:
            return False
        else:
            s.append(d)
    return True

# def compare_speed(func_1, func_2):
#     before = t
print(has_distinct_elements([1,2,3,4,5,6,7,8]))
print(has_distinct_elements_1([1,2,3,4,5,6,7,8]))
