def find_threes(numbers):
    suma=0
    for i in numbers:
        y=i%3
        if y==0:
            suma=suma+i
    return suma

print("this program will calculate the sum of all the numbers that are divisibles by 3 in the list")
lista=[]
r="yes"
while r=="yes":
    while True:
        try:
            x=int(input("please enter a value for the list: "))
            lista.append(x)
            break
        except ValueError:
            print("sorry, It has to be a non-negative integer number")
    while x<0:
        while True:
            try:
                x=int(input("please enter a value for the list: "))
                lista.append(x)
                break
            except ValueError:
                print("sorry, It has to be a non-negative integer number")

    r=input("do you want to ad an other number to the list? yes or no?: ")
    while r != "yes" and r !="no":
            r=input("sorry,that is not an option,try again(yes or no): ")
c=find_threes(lista)
print("the list is: %s"%(lista))
print ("the sum of all of the numbers that are divisibles by 3 is: %s"%c)
