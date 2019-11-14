#Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, 
# and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D)
def line_reader_and_reverser():
    lines=[]
    while True:
        x= input()
        if x == '':
            break
        lines.append(x)
    lines = reversed(lines)
    for line in lines:
        print(line)

line_reader_and_reverser()
