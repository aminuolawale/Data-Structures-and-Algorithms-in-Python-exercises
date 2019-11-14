def vowel_counter(s):
    s= s.lower()
    count=0
    for letter in s:
        if letter in ['a','e','i','o','u']:
            count+=1
    return (count)


print(vowel_counter('baaeeeeaat'))