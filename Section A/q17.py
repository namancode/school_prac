"""
Question 17
Practical Worksheet 2018-19
"""

from random import randint

ideal_n = randint(1, 20)

name = input("Hello! What is your name?\n")
print('Well, {}, I have chosen a number between 1 and 20.'.format(name))

n = int(input('Take a guess\n'))
cnt = 1
while(ideal_n != n):
    if(n < ideal_n):
        print("Your guess is too low.")
    elif(n > ideal_n):
        print("Your guess is too high")
    n = n = int(input('Take a guess.\n'))
    cnt += 1
print("Good job, {}! You guessed my number in {} guesses!".format(name, cnt))
