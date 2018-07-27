#PART 1
s=input("Enter string: ")
print("Frequency: ")
unique=""
#Making a string with unique chars
for i in (s):
    if unique.find(i)<0:
        unique+=i
#Finding occurences of unique chars in original
for i in unique:
    print(i,":",s.count(i))
print("\n")

#PART 2
maxLen=0
maxWord=""
currentWord=""
currentLen=0
isWord=False
#Checking what is a word and storing length of each to compare against current highest
for i in s:
    if i.isalpha():
        currentLen+=1
        currentWord+=i
        if not isWord:
            isWord=True
    else:
        if isWord:
            currentLen=0
            currentWord=""
        isWord=False
    if currentLen>maxLen:
        maxLen=currentLen
        maxWord=currentWord
print("Longest word: ",maxWord)
print("\n")

#PART 3
s2 = " "+s
newS=""
for i in range(1,len(s2)):
    #Capitalizing chars with spaces before them
    if s2[i-1].isspace() and s2[i].isalpha():
        newS += s2[i].upper()
    else:
        newS += s2[i]
print("Title Case: ",newS)
print("\n")

#PART 4
name=input("Enter name: ")
name=" "+name
newS=""
#Making a reversed string
for i in range(len(name)):
    newS+=name[-i-1]
#Storing last name as is in reverse
space=newS.find(" ")
S=""
S+=newS[0:space-1]+newS[space-1].upper()
newS=newS[space:len(newS)]
for i in range(len(newS)-1):
    #Storing capitalized 1st letters of all other parts in reverse
    if newS[i+1].isspace():
        S+=" "+newS[i].upper() 
#Reversing back to normal order
initials=""
for i in range(len(S)):
    initials+=S[-i-1]
print("Initials: ",initials)
