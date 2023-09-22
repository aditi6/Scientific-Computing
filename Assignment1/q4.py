import math

# Defining the given function
def f(x):
    return (2/(1+19*math.exp((-10)*x)))-1

# Secant Method
def secant(x_prev,x):
    i=0 # i counts the number of iterations
    while True:
        # Next iteration
        xn = x - f(x)*((x-x_prev)/(f(x)-f(x_prev)))
        i+=1

        # Checking for the case where exact root is found
        if(f(xn)==0):
            print(xn,i)     
            return xn,i
        
        # Checking for the case where relative error tolerance is reached
        if(abs(xn-x)/abs(xn)<0.0001):
            print("Root is", xn , ", No. of iterations are" , i)     
            return xn,i
        
        # Values for next iteration
        x_prev=x
        x=xn
   
    
ans,i=secant(1,1/12)