from random import randint

def my_shuffle(original_list):
    shuffled_list = []
    while len(shuffled_list) < len(original_list):
        is_distinct = False
        while not is_distinct:
            randomly_chosen = original_list[randint(0,len(original_list)-1)]
            if randomly_chosen in shuffled_list:
                randomly_chosen = original_list[randint(0,len(original_list)-1)]
            else:
                shuffled_list.append(randomly_chosen)
                break
    return shuffled_list

print(my_shuffle([1,2,3,4,5,6]))
            
