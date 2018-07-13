s = str(input("Enter full name: "))
#PART 1
dict = {}
for n in s:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print("Frequency: ")
for key in dict:
    print (key, dict[key])
#PART 2
print("Longest word: ")
a = s.split(" ")
print(max(a, key=len))
#PART 3
print("Title case: ")
for i in a:
    print(i.capitalize(), end=" ")
#PART 4
print("\nInitials:")
for i in a:
    print(i.capitalize()[0], end="")
