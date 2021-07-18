'''Importing pytest'''
import pytest
'''Adding two numbers'''
def add(num1, num2):
    return num1+num2
'''def sub():
    Subtracting two numbers'''
def subtract(num1, num2):
    return num1 - num2
'''def mul():
    Multiplying two numbers'''
def multiply(num1, num2):
    return num1*num2
'''def div():
    Dividing two numbers'''
def divide(num1, num2):
    return num1/num2
'''def square():
    Squaring two numbers'''
def square(num):
    return num * num
'''def cube():
    Cubing two numbers'''
def cube(num):
    return num*num*num
def squareroot(num):
    return num**0.5
def factorial(num):
    # single line to find factorial
    return 1 if (num==1 or num==0) else num * factorial(num - 1)
def decimal_to_binary(dec):
    decimal = int(dec)
    return decimal
def decimal_to_octal(dec):
    decimal = int(dec)
    return decimal
def decimal_to_hexadecimal(dec):
    decimal = int(dec)
    return decimal
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
sq for Square
cube for Cube
sqrt for Square root
fact to find Factorial of a number
Bin for decimal to binary
Oct for decimal to octal
Hex for decimal to Hexadecimal
''')
    if operation == '+':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "+", num2, "=", add(num1, num2))
        output = str(add(num1,num2) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == '-':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "-", num2, "=", subtract(num1, num2))
        output = str(subtract(num1,num2) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == '*':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "*", num2, "=", multiply(num1, num2))
        output = str(multiply(num1,num2) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == '/':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "/", num2, "=", divide(num1, num2))
        output = str(divide(num1,num2) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'sq':
        number = float(input("Please Enter any numeric Value : "))
        sqre = square(number)
        print("The Square of a Given Number {0}  = {1}".format(number, sqre))
        output = str(square(number) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'cube':
        number = float(input("Please Enter any numeric Value : "))
        cubes = cube(number)
        print("The Cube of a Given Number {0}  = {1}".format(number, cubes))
        output = str(cube(number) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'sqrt':
        number = float(input("Please Enter any numeric Value : "))
        sqrt = squareroot(number)
        print("The Square of a Given Number {0}  = {1}".format(number, sqrt))
        output = str(squareroot(number) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'fact':
        num = float(input("Please Enter any numeric Value : "))
        print ("Factorial of",num,"is",factorial(num))
        output = str(factorial(num) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'Bin':
        decimal = int(input("Enter any decimal number: "))
        print(decimal, " in Binary : ", bin(decimal))
        output = str(bin(decimal) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'Oct':
        decimal = int(input("Enter any decimal number: "))
        print(decimal, "in Octal : ", oct(decimal))
        output = str(oct(decimal) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    elif operation == 'Hex':
        decimal = int(input("Enter any decimal number: "))
        print(decimal, " in Hexadecimal : ", hex(decimal))
        output = str(hex(decimal) )
        filename = open("demofile3.txt", "w+")
        filename.write(output)
        filename.close()
    else:
        print('You have not typed a valid operator, please run the program again.')
    # Add again() function to calculate() function
    again()
def again():
    calc_again = input('''
Please type Y for YES or N for NO.
to continue
''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
calculate()
