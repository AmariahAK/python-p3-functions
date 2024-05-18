#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    name = input()
    print("Hello,", name)

def greet_with_default(name="programmer"):
    name = input()
    if name != 'programmer':
        print("Hello", name)
    else:
        print("Hello programmer")

def add(num1, num2):
    num1 = int(input())
    num2 = int(input())
    add = num1 + num2
    print(add)

def halve(number):
    number = int(input())
    halve = number // 2
    print(halve)
