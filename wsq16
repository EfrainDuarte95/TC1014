fr=open("93cars.dat.txt","r")
cmpg=0
hmpg=0
mp=0
f=1
car=0
for line in fr:
    if f%2==1:
        cmpg=cmpg+float(line[52:54])
        hmpg=hmpg+float(line[55:57])
        mp=mp+float(line[42:46])
        car=car+1
    f=f+1

a=round(cmpg/car,5)
b=round(hmpg/car,5)
c=round(mp/car,5)

print("the average gas mileage in city is: " ,a)
print("the average gas mileage on highway is: " ,b)
print("the average midrange price of the vehicles in the set is: " ,c)
