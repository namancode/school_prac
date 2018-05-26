"""
Question 11
Practical Worksheet 2018-19
"""

for i in range(2000, 3201):
    if((i%7 == 0) and (i%5 != 0)):
        print(i, end=', ')