"""Efrain Duarte Lopez A01113813"""
def factorial(x):
    s=x
    y=x
    for i in range (x-1):
        s=s*(y-1)
        y=y-1
    print ("The factorial of %s is %s." %(x,s))
r="yes"
while r == "yes":
    while  True:
        try:
            q=int(input("Please enter a non-negative integer number: "))
            break
        except ValueError:
            print("this is not a integer number, try again: ")
    while q<0:
        try:
            q=int(input("this is not a positive number,try again: "))
        except ValueError:
            print ("this is not a integer number, try again:  ")
            while True:
                try:
                    q=int(input("Please enter a non-negative integer number: "))
                    break
                except ValueError:
                    print ("this is not a integer number, try again: ")
    if  q==0:
        print("the factorial of 0 is: 1")
    else:
        factorial(q)
    r=input("would you like to calculate the factorial of an other number?(answer yes or no) ")
    while r != "yes" and r !="no":
        r=input("that is not an option, write yes or no: ")
