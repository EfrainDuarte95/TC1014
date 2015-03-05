"""Efrain Duarte Lopez A01113813"""
print("We will select a random number from 0 to 100. lets see in how many tries you get it")
import random
x= random.randrange(0,100)
print("please enter the guess of the number")
y=int(input())
i=1
while y != x:
    if y > x:
        print("To hight,try again")
        i=i+1
        y=int(input())
    if y < x:
        print("To low,try again")
        i=i+1
        y=int(input())
print("You got it! the The right answer is indeed %s " %y)
print("You made %s guesses to get the right number" %i)
