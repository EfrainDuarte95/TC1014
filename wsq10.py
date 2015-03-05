"""Efrain Duarte Lopez"""
print ("You will give us 10 floating numbers, and it will show you average and standard deviation of those numbers.")

import statistics

numbers=[]

for i in range(10):
    while True:
        try:
            x=float(input("please enter a number: "))
            numbers.append(x)
            break
        except ValueError:
            print("")

s=sum(numbers)

a=s/10.0
standar=statistics.stdev(numbers)

print ("the total is: %s"%s)
print ("the average of the numbers is: %s"%a)
print ("The standard deviation is: %s"%standar)
