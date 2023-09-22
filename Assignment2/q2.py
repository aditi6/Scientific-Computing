import math
import numpy as np
import matplotlib.pyplot as plt

# Defining the given function
def f(x):
    return math.cos(x)-(x*math.exp(x))

def secant(x_prev,x):
    i=0 # i counts the number of iterations
    rel_error=[]
    iterations=[]
    while True:
        # Next iteration
        xn = x - f(x)*((x-x_prev)/(f(x)-f(x_prev)))
        i+=1
        iterations.append(i)
        
        # Checking for the case where relative error tolerance is reached
        error=abs(xn-x)/abs(xn)
        rel_error.append(error)

        if(error<10**(-6)):
            print("Root is", xn , ", No. of iterations are" , i)     
            return xn,i,iterations,rel_error
        
        # Values for next iteration
        x_prev=x
        x=xn       

ans,i,iterations_secant,rel_error_secant = secant(0,1)    




def mullers(x0,x1,x2): 

    rel_error=[]
    iterations=[]

    xn=0 
    i=0 #Counts the no. of iterations

    a=0
    b=0
    c=0
    while True:
        a=(((x1-x2)*(f(x0)-f(x2)))-((x0-x2)*(f(x1)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
        b=((((x0-x2)**2)*(f(x1)-f(x2)))-(((x1-x2)**2)*(f(x0)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
        c=f(x2)

        # Next Iteration
        xn=x2-(2*c)/(b+np.sign(b)*math.sqrt(b**2-4*a*c))
        i+=1
        iterations.append(i)

        # Checking for the case where relative error tolerance is reached
        error=abs(xn-x2)/abs(xn)
        rel_error.append(error)

        if(error<10**(-6)):
            print("Root is", xn , ", No. of iterations are" , i)     
            return xn,i,iterations,rel_error
    
        x0=x1
        x1=x2
        x2=xn

ans,i,iterations_muller,rel_error_muller=mullers(0,0.5,1)

plt.plot(iterations_secant,rel_error_secant,label="Secant Method",linestyle='--',marker='o')
plt.plot(iterations_muller,rel_error_muller,label="Muller's Method",linestyle='--',marker='o')
plt.xlabel("Number of Iterations")
plt.ylabel("Relative Error")
plt.legend()
plt.savefig('.\plot2.jpg')