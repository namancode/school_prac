# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:41:31 2018

@author: amity
"""
f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
o = str(input("Enter operator: "))

if o == "+":
    print(f+s)
elif o == "-":
    print(f-s)
elif o == "*":
    print(f*s)
elif o == "/":
    print(f/s)