import numpy as np
import matplotlib.pyplot as plt
import math

# Defining the given function
def f(x):
    return (x**3) - (0.165*(x**2)) + (3.993*(10**(-4)))

# Bisection Method
def bisection(a,b): # a and b are initial points
    i=0 # i counts the number of iterations

    #First iteration
    x_n = (a + b)/2 
    i+=1

    # Checking for the case where exact root is found
    if(f(x_n)==0): 
            print("Found exact solution.")
            print(x_n,i)
            return x_n
    # Two cases of bisection method
    elif(f(a)*f(x_n)<0):
            b = x_n
    elif(f(b)*f(x_n)<0):
            a = x_n

    # Second iteration
    x_prev=x_n  # Storing the value of previous iteration (to calculate tolerance)  
    x_n = (a + b)/2 
    i+=1 # Increasing iteration count

    # Iterating until tolerance is reached
    while(abs(x_n-x_prev)/abs(x_n)>0.0001): #Relative Error Tolerance expression

        # Checking for the case where exact root is found
        if(f(x_n)==0):
            print("Found exact solution.")
            print("Root is", x_n, ", No. of iterations are" , i)
            return x_n
        # Two cases of bisection method
        elif(f(a)*f(x_n)<0):
            b = x_n
        elif(f(b)*f(x_n)<0):
            a = x_n

        # Next iteration
        x_prev=x_n  # Storing the value of previous iteration (to calculate tolerance)  
        x_n = (a + b)/2
        i+=1 # Increasing iteration count

    # Printing and returning final root and number of iterations after exiting the loop    
    print("Root is", x_n, ", No. of iterations are" , i)
    return x_n,i

# Initial Points
a=0
b=0.1
ans,i=bisection(a,b)



                                      