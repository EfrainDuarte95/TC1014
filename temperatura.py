print ("What is the temperature in Fahrenheit? ")
x= int(input())
c=5*(x-32)/9
print ("the temperature of %s degrees Fahrenheit is: %s Celsius" %(x,c))
if c>=100:
    print ("Water does boil at this temperature (under typical conditions)")
    print ("be careful, you can burn")
else:
    print("Water does not boil at this temperature (under typical conditions)")




