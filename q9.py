"""
Question 9
Practical Worksheet 2018-19
"""

u = int(input("Units consumed: "))
price = 0
if(u <= 100):
    price = 40*u
else:
    price = 40*100
    u = u-100

if(u <= 200):
    price = price + 50*u
else:
    price = price + 50*200
    u = u-200

price = price + 60*u

print("Charges: ", (price/100)+50)
