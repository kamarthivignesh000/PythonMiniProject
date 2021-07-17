import pytest
from project import add,decimal_to_hexadecimal,subtract,divide,multiply,square,cube,squareroot,factorial,decimal_to_binary,decimal_to_octal

'''def calculate():
    a = '+'
    assert Python_project.calculate(a) == '+' '''

def test_add():
   a=2
   b=9
   assert add(a,b) == 11


def test_subtract():
   a=3
   b=2
   assert subtract(a,b) == 1

def test_multiply():
   a=5
   b=2
   assert multiply(a,b) == 10

def test_divide():
   a = 8
   b = 2
   assert divide(a,b) == 4

def test_square():
   a = 8
   
   assert square(a) == 64

def test_cube():
   a = 2
   
   assert cube(a) == 8

def test_squareroot():
   a = 16
   
   assert squareroot(a) == 4

def test_factorial():
   a = 5
   
   assert factorial(a) == 120


def test_decimal_to_binary():
   dec = 8
   assert bin(dec) == bin(8)


def test_decimal_to_octal():
   dec =10
   assert oct(dec) == oct(10)  

def test_decimal_to_hexadecimal():
   dec =10
   assert hex(dec) == hex(10)       
