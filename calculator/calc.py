#!/usr/bin/env python3

def add(a, b):
    """
    add 2 numbers
    """
    if a and b:
        res = a + b
    else:
        res = "2 integers required as argument"
    
    return res

def subtract(a, b):
    """
    subtract a number
    """
    if a and b:
        res = a - b
    else:
        res = "2 integers required as argument"
    
    return res

def division(a, b):
    if b and b == 0:
            return 0
    if a:
        res = a / b
    else:
        res = "2 integers required as argument"
    
    return res

def multiply(a, b):
    if a and b:
        res = a * b
    else:
        res = "2 integers required as arguments"
    
    return res

while True:
    try:
        num1 = int(input("Enter num1: "))
        operation = input("Enter operand('+', '-', '*', '/'): ")
        num2 = int(input("Enter num2: "))
        
        if operation == '+':
            print(add(num1, num2))
        elif operation == '-':
            print(subtract(num1, num2))
        elif operation == '*':
            print(multiply(num1, num2))
        elif operation == '/':
            print(division(num1, num2))
        else:
            print("Enter valid operand")
    except ValueError:
        print("Please enter valid integers for num1 and num2.")
    except ZeroDivisionError:
        print('0')
    except Exception as e:
        print(f"An error occured {e}")

