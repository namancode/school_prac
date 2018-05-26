"""
Question 12
Practical Worksheet 2018-19
"""

n = int(input("Enter number of students: "))
ga, gb, gc, gd = 0, 0, 0, 0
for i in range(0, n):
    s = int(input("Enter age of student " + str(i+1) + ": "))
    if(s >= 12 and s < 15):
        ga += 1
    elif(s >= 15 and s < 17):
        gb += 1
    elif(s >= 17 and s < 19):
        gc += 1
    elif(s < 12):
        gd += 1

print("\nGroup A: 12 yrs and above but less than 15 yrs -",  ga, "\nGroup B: 15 yrs and above but less than 17 yrs -", gb, "\nGroup C: 17 yrs and above but less than 19 yrs -", gc, "\nGroup D: Lesser than 12 yrs                    -", gd)
