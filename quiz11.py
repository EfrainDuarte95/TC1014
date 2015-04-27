#Efrain Duarte Lopez
def readNumbersFromFile(x):
    f=open(x,"r")
    t=0
    n=0
    numbers=[]
    for line in f:
        a=int(line[0:len(line)])
        t=t+a
        n=n+1
        numbers.append(a)
        print (line)
    av=t/n
    sm=0
    for i in numbers:
        su=(i-av)**2
        sm=sm+su
    st=(sm/(n-1))**(0.5)
    print ("the total of the values is: ",t)
    print ("The number of values is: ",n)
    print ("The average of the values is: ",av)
    print ("the standard deviation of the values is: ",st)

readNumbersFromFile("numbers.txt")
