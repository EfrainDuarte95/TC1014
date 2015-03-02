def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a//b

def rem(a,b):
    return a%b

x=int(input("please enter the firs number: "))
y=int(input("please enter the second number: "))

suma(x,y)
resta(x,y)
mult(x,y)
div(x,y)
rem(x,y)
print ("The sum of the two numbers is: %s "%(x+y))
print ("The diference of the two numbers is: %s "%(x-y))
print ("The product of the two numbers is: %s "%(x*y))
print ("The integer based division of the two numbers is: %s "%(x//y))
print ("The remainder of the integer division of the two numbers is: %s "%(x%y))
