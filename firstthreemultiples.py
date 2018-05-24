# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:13:21 2018

@author: amity
"""
n = int(input("Number: "))
sum = 0
for x in range(1,4):
    sum = sum + x*n
print("Sum of first 3 multiples of n is: ", sum)