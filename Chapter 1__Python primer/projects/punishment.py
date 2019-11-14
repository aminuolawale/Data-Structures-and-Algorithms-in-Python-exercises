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
    