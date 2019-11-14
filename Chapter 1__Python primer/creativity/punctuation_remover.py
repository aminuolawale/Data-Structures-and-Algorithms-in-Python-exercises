def punctuation_remover(s):
    alphabets = list(chr(97+x) for x in range(0,26))
    t =''
    for letter in s:
        if letter.lower() in alphabets or letter==' ':
            t+=letter
    return t


print(punctuation_remover('I am, a ....boss'))


