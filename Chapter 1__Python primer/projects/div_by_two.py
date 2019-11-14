def div_by_two(number):
    count=0
    while number >= 2:
        number/=2
        count+=1

    return count


print(div_by_two(9))