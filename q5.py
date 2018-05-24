"""
Question 5
Practical Worksheet 2018-19
"""

n = int(input("What is the amount in Rupees? "))
t = int(n/1000)
n = n%1000
f = int(n/500)
n = n%500
h = int(n/100)
n = n%100
fi = int(n/50)
n = n%50
te = int(n/10)
n = n%10
fiv = int(n/5)
n = n%5
tw = int(n/2)
n = n%2
o = int(n)
print("Rs. 1000:", t, "\n Rs. 500:", f, "\n Rs. 100:", h, "\n Rs. 50:", fi,
      "\n Rs. 10:", te, "\n Rs. 5:", fiv, "\n Rs. 2:", tw, "\n Rs. 1:", o)
