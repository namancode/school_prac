"""
Question 8
Practical Worksheet 2018-19
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
