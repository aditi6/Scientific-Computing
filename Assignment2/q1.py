import math

# Function Definition
def g(x):
    return 0.0549*math.sin(x)+((1597/1967.04)*2*math.pi)

# Initial Point
x=1.5*math.pi
i=0 # Counts the no. of iterations

while True:
    xn=g(x)
    i+=1

    # Check if relative tolerance is reached
    if(abs(xn-x)/abs(xn)<10**(-8)):
        break
    x=xn 

print("Root is", xn , ", No. of iterations are" , i)

# Coordinates
a=384400 
b = 383820
x= a*(math.cos(xn)-0.0549)
y=b*math.sin(xn)
print("x coordinate is", x , ", y coordinate is " , y)
