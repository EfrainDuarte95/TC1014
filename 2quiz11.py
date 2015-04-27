#Efrain Duarte Lopez
def check_banana(x):
    f=open(x,"r")
    sm=0
    for line in f:
        y=line.lower()
        z=y.find("banana")
        while z != (-1):
            sm=sm+1
            z=y.find("banana",(z+1))
    print (sm)
check_banana("banana.txt")
