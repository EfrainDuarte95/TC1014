def triangulo (size):
    for i in range(1,size+1):
        for c in range(1,i+1):
            print('T',end="")
        print()
    for i in range(size-1,0,-1):
        for c in range(1,i+1):
            print('T',end="")
        print()
print("this programm will made a triangles, the size of the triangle depends of you")
x=int(input("please enter the number of the size that you wanted: "))
c=triangulo(x)
print(c)
