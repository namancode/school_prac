"""
Question 10
Practical Worksheet 2018-19
"""

num = str(input("Enter number: "))
l = [int(i) for i in num] #cant use arrays

add = 0
mul = 1
for s in range(0, len(l)):
    if(s%2 == 0):
        mul = mul * l[s]
    else:
        add = add + l[s]

print("Sum of odd positioned digits:", add, "\nProduct of even positioned digits:", mul, "\nSum of above two results:", add+mul)
