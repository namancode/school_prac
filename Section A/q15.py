"""
Question 15
Practical Worksheet 2018-19
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while(a != b):
    if(a > b):
        a = a-b
    else:
        b = b-a

print("HCF of the two numbers is:", a)
