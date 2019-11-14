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
