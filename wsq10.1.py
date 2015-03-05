"""Efrain Duarte Lopez"""
print("You will give us floating numbers, and it will show you average and standard deviation of those numbers.")

import statistics

numbers=[]
r="yes"
while r=="yes":
    while True:
        try:

            x=float(input("please enter a  number: "))
            numbers.append(x)
            break
        except ValueError:
            print("thats not a number, try again: ")    
    r=input("do you want to ad an other number? yes or no?: ")
    while r != "yes" and r !="no":
        r=input("sorry,that is not an option,try again(yes or no): ")

s=sum(numbers)
a=statistics.mean(numbers)
standar=statistics.stdev(numbers)

print("the total is: %s"%s)
print("the average of the numbers is: %s"%a)
print("The standard desviation is: %s"%standar)
