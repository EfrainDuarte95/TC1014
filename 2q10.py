def dotProduct(v1,v2):
    y=len(v1)
    y1=len(v2)
    if y != y1:
        print("the size of the vectors are different")
    else:

        x=0
        for i in range (len(v1)):
            x=x+(v1[i]*v2[i])

        return x
v=[1,2,3,5]
V=[2,4,5,6]
x=dotProduct(v,V)
print(x)
