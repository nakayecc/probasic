import sys

def plus (a,b):
    return a+b
def minus (a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division (a,b):
    return a/b

num1 = None
num2 = None
op = None

while True:
    try:
        num1 = int(input("Enter a number (or a letter to exit):"))
    except ValueError:
        break
    op = input("Enter an operation:")
    num2 = int(input("Enter another number:"))

    if(op == "+"):
       print("Result: " + str(plus(num1,num2)))
    if(op == "-"):
       print("Result: " + str(minus(num1,num2)))
    if(op == "*"):
       print("Result: " + str(multiplication(num1,num2)))
    if(op == "/"):
       print("Result: " + str(division(num1,num2)))