#A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone 
# program that will write out the following sentence one hundred times: “I will never spam my friends again.” 
# Your program should number each of the sentences and it should make eight different random-looking typos.

from random import randrange

text= 'I will never spam my friends again'

def line_generator(n):
    for _ in range(0,n):
        text_list = list(text)
        should_error = randrange(0,2)
        if should_error:
            while True:
                error_position = randrange(0, len(text_list))
                if text_list[error_position] != ' ':
                    break
            
            text_list[error_position] = chr(randrange(97,122))
        yield ''.join(text_list)

# for i in range(0,100):
#     print(line_generator())
for line in line_generator(100):
    print(line)
    