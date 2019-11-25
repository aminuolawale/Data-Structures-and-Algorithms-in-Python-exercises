#Write a Python program that simulates a handheld calculator. Your program should process input from the Python console 
# representing buttons that are “pushed,” and then output the contents ofthe screenafter each operation isperformed. 
# Minimally, your calculator should beable toprocess the basic arithmetic operations and a reset/clear operation.

def calculator():
    operation = []
    
    while True:
        operand = input(': ')
        if operand == '=':
            break
        if operand == 'd':
            operation.pop()
            print(operation)
            continue
        if operand == 'c':
            operation = []
            continue
        operation.append(operand)
        result = int(operation[0])
    for i in range(0, len(operation)):
        if operation[i+1] == '+':
            result += int(operation[i+2])
        if operation[i+1] == '-':
            result -= int(operation[i+2])
        if operation[i+1] == '*':
            result *= int(operation[i+2])
        if operation[i+1] == '/':
            result /= int(operation[i+2])
        if i+3 < len(operation):
            i+=3
        else:
            return result
print(calculator())