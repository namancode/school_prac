"""
Question 14
Practical Worksheet 2018-19
"""

num = int(input("Enter number to check: "))

m = num
l = 0
while(m>0):
    l += 1
    m = m//10

rev = 0

for i in range(l, 0, -1):
    rev += ((num%(10**i) - num%(10**(i-1)))/(10**(i-1))) * (10**(l-i))


if(int(rev) == num):
    print("It's a palindrome!")
else:
    print("It's not a palindrome")
