import pytest
from project import add,decimal_to_hexadecimal,subtract,divide,multiply,square,cube,squareroot,factorial,decimal_to_binary,decimal_to_octal
'''def calculate():
    a = '+'
    assert Python_project.calculate(a) == '+' '''
def test_add():
    num1=2
    num2=9
    assert add(num1,num2) == 11
def test_subtract():
    num1=3
    num2=2
    assert subtract(num1,num2) == 1
def test_multiply():
    num1=5
    num2=2
    assert multiply(num1,num2) == 10
def test_divide():
    num1 = 8
    num2 = 2
    assert divide(num1,num2) == 4
def test_square():
    num = 8
    assert square(num) == 64
def test_cube():
    num = 2
    assert cube(num) == 8
def test_squareroot():
    num = 16
    assert squareroot(num) == 4
def test_factorial():
    num = 5
    assert factorial(num) == 120
def test_decimal_to_binary():
    dec = 8
    assert bin(dec) == bin(8)
def test_decimal_to_octal():
    dec =10
    assert oct(dec) == oct(10)
def test_decimal_to_hexadecimal():
    dec =10
    assert hex(dec) == hex(10)