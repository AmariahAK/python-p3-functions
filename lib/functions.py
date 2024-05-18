#!/usr/bin/env python3

def greet_programmer():
    return "Hello, programmer!"

def greet(name):
    return f"Hello, {name}"

def greet_with_default(name="programmer"):
    if name != "programmer":
        return f"Hello, {name}"
    else:
        return "Hello programmer"

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number // 2



# Usage of greet function with user input
name = input("Enter your name: ")
print(greet(name))

# Usage of greet_with_default function with user input
name_with_default = input("Enter your name or press enter to use default: ")
if name_with_default == "":
    print(greet_with_default())
else:
    print(greet_with_default(name_with_default))

# Usage of add function with user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(add(num1, num2))

# Usage of halve function with user input
number = int(input("Enter a number to halve: "))
print(halve(number))
