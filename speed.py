# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:17:22 2018

@author: amity
"""

s = int(input("Speed: "))
b = str(input("Is it your birthday? "))

if(b.lower()=="yes"):
    f = 5
else:
    f = 0
    
if(s <= 60+f):
    print(0)
elif(s <= 80+f):
    print(1)
elif(s > 80+f):
    print(2)