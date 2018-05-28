"""
Question 14
Practical Worksheet 2018-19
"""

num = int(input("Enter number to check: "))
i, fin = 1, 0

while(num%(10**(i-1)) != num):
    n = ((num%(10**i))-(num%(10**(i-1))))/(10**(i-1))
    fin = (fin + n)*10
    i += 1

if(int(fin/10) == num):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
