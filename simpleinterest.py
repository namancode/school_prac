# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:00:28 2018

@author: amity
"""
p = int(input("What's your principal amount (in Rs.)? "))
r = int(input("What's your interest rate (%)? "))
t = int(input("What's the duration of deposit (in years)? "))

print("Simple Interest is: ", (p*r*t)/100, "Rupees")