"""
Question 19
Practical Worksheet 2018-19
"""

print("Input date:")
d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

mon = {1:"JAN", 2:"FEB", 3:"MAR", 4:"APR", 5:"MAY", 6:"JUN", 7:"JUL", 8:"AUG", 9:"SEP", 10:"OCT", 11:"NOV", 12:"DEC"}

print(str(d) + "-" + mon[m] + "-" + str(y))
