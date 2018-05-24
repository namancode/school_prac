"""
Question 7
Practical Worksheet 2018-19
"""

l = int(input("Enter number of legs: "))
h = int(input("Enter number of heads: "))

r = int((l-2*h)/2)
c = int(h-r)

print("Number of rabbits is", r, "\nNumber of chickens is", c)
