s = str(input("Enter parent string: "))
x = str(input("Enter string to check: "))

if(s.find(x) == 0):
    print("Given string is prefix")
elif(len(s) - len(x) == s.find(x)):
    print("Given string is postfix")
else:
    print("Given string is neither postfix nor prefix")