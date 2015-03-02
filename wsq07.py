"""Efrain Duarte Lopez A01113813"""
print ("We will calculate the sum of the integers in the range you provide")
print("Enter the lower bound")
x=int(input())
print("Enter the upper bound")
y=int(input())
l=x
u=y

if y < x:
    l=y
    u=x
    print("You introduce the numbers in the wrong order, but we can fix it")
s=0
z=u-l+1
i=0
while i != z:
    s=s+l
    l=l+1
    i=i+1
print("the sum of integers in the range you provided is:",s)
