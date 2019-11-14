#Write a short Python function that takes a strings,representing a sentence, and returns a copy 
# of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", 
# this function would return "Lets try Mike".

def punctuation_remover(s):
    alphabets = list(chr(97+x) for x in range(0,26))
    t =''
    for letter in s:
        if letter.lower() in alphabets or letter==' ':
            t+=letter
    return t


print(punctuation_remover('I am, a ....boss'))


