"""
Question 10
Practical Worksheet 2018-19
"""

num = int(input("Enter number: "))
l = 1

add = 0
mul = 1
while(num%(10**(l-1)) != num):
    if(l%2 == 0):
        add += ((num%(10**l))-(num%(10**(l-1))))/(10**(l-1))
    else:
        mul *= ((num%(10**l))-(num%(10**(l-1))))/(10**(l-1))
    l += 1        
print("Sum of odd positioned digits:", add, "\nProduct of even positioned digits:", mul, "\nSum of above two results:", add+mul)
