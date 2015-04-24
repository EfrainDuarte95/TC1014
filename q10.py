def findthrees(numbers):
    s=0
    for i in numbers:
        x=i%3
        if x == 0:
            s=s+i
    return s
number=[0,4,2,6,9,8,3,12]
x=findthrees(number)
print(x)
