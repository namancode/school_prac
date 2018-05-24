# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:47:53 2018

@author: amity
"""

num = str(input("Enter number: "))
l = [int(i) for i in num]

add = 0
mul = 1
for s in range(0, len(l)):
    if(s%2 == 0):
        mul = mul * l[s]
    else:
        add = add + l[s]

print("Sum of odd positioned digits:", add, "\nProduct of even positioned digits:", mul, "\nSum of above two results:", add+mul)