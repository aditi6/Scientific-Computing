import math
def f(x):
    return x**2 + math.cos(30*2.718*x)

# Bisection Method
def bisection(a,b): # a and b are initial points
    i=0 # i counts the number of iterations
    x_prev=a

    while True:
        # Next iteration
        xn = (a + b)/2 
        i+=1

        # Checking for the case where exact root is found
        if(f(xn)==0): 
            print("Found exact solution.")

        # Checking for the case where relative error tolerance is reached
        if(abs(xn-x_prev)/abs(xn)<10**(-6)):
            # print("Root is", xn , ", No. of iterations are" , i)    
            return xn

        if f(a)*f(b) > 0:
            return -1
        # Two cases of bisection method
        elif(f(a)*f(xn)<0):
            b = xn
        elif(f(b)*f(xn)<0):
            a = xn

        x_prev=xn 

        # No root found after 500 iterations
        if(i==50):
            return -1


# Initial Points
a, delta = 0, 0.005 
roots=[]

# Finding roots in [0,1] by looking at intervals of length delta
while a + delta < 1:
    if f(a)*f(a+delta)<0: # By IVT, there is no root if f(a)*f(a+delta)>0 (assuming the interval is small enough)
        roots.append(bisection(a, a+delta)) # Finding the root in the interval [a, a+delta]
    a += delta # Moving to the next interval

print(f'The roots are {roots}, and there are {len(roots)} of them.')

       

        
          



