#Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device.
#  That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on 
# a separate line. After each such input, you should output to the Python console what would be displayed on your 
# calculator.

def calculator():
    operation = []
    
    while True:
        operand = input(': ')
        if operand == '=':
            break
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
        




