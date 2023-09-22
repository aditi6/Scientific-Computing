
import matplotlib.pyplot as plt
import math

# First Function

# Defining the given function
def f1(x):
    return  (x + math.exp(-x**2)*math.cos(x))**2
# Defining the derivative of the given function
def df1(x):
    return 2*(x + math.exp(-x**2)*math.cos(x))*(1-(math.exp(-x**2)*math.sin(x))-(2*x*math.cos(x)*math.exp(-x**2)))
# Defining the second derivative of the given function
def d2f1(x):
    return  (2*math.exp(-2*x**2))*((math.sin(x))**2+((8*x*math.cos(x)+(4*x**2-2)*math.exp(x**2))))*(math.sin(x)) +((8*x**2-3)*(math.cos(x))**2)+((4*x**3-7*x)*math.exp(x**2)*math.cos(x))+(math.exp(2*x**2))

# Newton's Method

# Arrays to store the tolerance and iteration count for plotting
newton_tolerance=[]
iterations=[]

def Newtonf1():
    i=0 # i counts the number of iterations 
    x_prev=0 # Starting point

    # First iteration
    x=x_prev-(f1(x_prev)/df1(x_prev)) 
    i+=1

    # Calculating Relative Error Tolerance and storing it in the array
    tol=abs(x-x_prev)/abs(x) 
    newton_tolerance.append(tol)
    iterations.append(i)

    # Iterating until tolerance is reached
    while(tol>0.000001):

        # Checking for the case where exact root is found
        if(f1(x)==0):
            print("Found exact solution")
            print("Function 1 Newton's Method - Root is", x, ", No. of iterations are" , i)
            return(x)
        
        x_prev=x # Storing the value of previous iteration (to calculate tolerance)
        # Next iteration
        x=x_prev-(f1(x_prev)/df1(x_prev)) 
        i+=1

        # Calculating Relative Error Tolerance and storing it in the array
        tol=abs(x-x_prev)/abs(x)
        newton_tolerance.append(tol)
        iterations.append(i)

    # Printing and returning final root and number of iterations after exiting the loop    
    print("Function 1 Newton's Method - Root is", x, ", No. of iterations are" , i)
    return(x,newton_tolerance,iterations)

# Modified Newton's Method

# Arrays to store the tolerance and iteration count for plotting
modified_newton_tolerance=[]
iterations2=[]

def ModifiedNewtonf1():
    i=0 # i counts the number of iterations
    x_prev=0 # Starting point

    # First iteration
    x=x_prev-((f1(x_prev)*df1(x_prev))/(df1(x_prev)**2-d2f1(x_prev)*f1(x_prev)))
    i+=1

    # Calculating Relative Error Tolerance and storing it in the array
    tol=abs(x-x_prev)/abs(x)
    modified_newton_tolerance.append(tol)
    iterations2.append(i)

    # Iterating until tolerance is reached
    while(tol>0.000001):

        # Checking for the case where exact root is found
        if(f1(x)==0):
            print("Found exact solution")
            print("Function 1 Modified Newton's Method - Root is", x, ", No. of iterations are" , i)
            return(x)
        
        x_prev=x # Storing the value of previous iteration (to calculate tolerance)

        # Next iteration
        x=x_prev-((f1(x_prev)*df1(x_prev))/(df1(x_prev)**2-d2f1(x_prev)*f1(x_prev)))
        i+=1

        # Calculating Relative Error Tolerance and storing it in the array
        tol=abs(x-x_prev)/abs(x)
        modified_newton_tolerance.append(tol)
        iterations2.append(i)

    # Printing and returning final root and number of iterations after exiting the loop    
    print("Function 1 Modified Newton's Method - Root is", x, ", No. of iterations are" , i)
    return(x,modified_newton_tolerance,iterations2)

# Plotting Relative tolerance vs Iteration count for both the methods
ans,newton_tolerance,iterations=Newtonf1()
ans1,modified_newton_tolerance,iterations2=ModifiedNewtonf1()
plt.plot(iterations,newton_tolerance,'o--',label="Newton's Method")
plt.plot(iterations2,modified_newton_tolerance,'o--',label="Modified Newton's Method")
plt.legend()
plt.xlabel("No. of Iterations")
plt.ylabel("Relative Error")
plt.savefig("./func1.png")


# Second Function

# Defining the given function
def f2(x):
    return x-2*math.log(1+math.exp(-x))
# Defining the derivative of the given function
def df2(x):
    return (1+((2*math.exp(-x))/(1+math.exp(-x))))
# Defining the second derivative of the given function
def d2f2(x):
    return (-2*math.exp(x))/((1+math.exp(x))**2)

# Newton's Method

# Arrays to store the tolerance and iteration count for plotting
newton_tolerance=[]
iterations=[]

def Newtonf2():
    i=0 # i counts the number of iterations
    x_prev=0 # Starting point

    # First iteration
    x=x_prev-(f2(x_prev)/df2(x_prev))
    i+=1

    # Calculating Relative Error Tolerance and storing it in the array
    tol=abs(x-x_prev)/abs(x)
    newton_tolerance.append(tol)
    iterations.append(i)

    # Iterating until tolerance is reached
    while(tol>0.000001):

        # Checking for the case where exact root is found
        if(f2(x)==0):
            print("Found exact solution")
            print("Function 2 Newton's Method - Root is", x, ", No. of iterations are" , i)
            return(x)
        
        x_prev=x # Storing the value of previous iteration (to calculate tolerance)

        # Next iteration
        x=x_prev-(f2(x_prev)/df2(x_prev))
        i+=1

        # Calculating Relative Error Tolerance and storing it in the array
        tol=abs(x-x_prev)/abs(x)
        newton_tolerance.append(tol)
        iterations.append(i)

    # Printing and returning final root and number of iterations after exiting the loop    
    print("Function 2 Newton's Method - Root is", x, ", No. of iterations are" , i)
    return(x,newton_tolerance,iterations)

# Modified Newton's Method

# Arrays to store the tolerance and iteration count for plotting
modified_newton_tolerance=[]
iterations2=[]

def ModifiedNewtonf2():
    i=0 # i counts the number of iterations
    x_prev=0 # Starting point

    # First iteration
    x=x_prev-((f2(x_prev)*df2(x_prev))/(df2(x_prev)**2-d2f2(x_prev)*f2(x_prev)))
    i+=1

    # Calculating Relative Error Tolerance and storing it in the array
    tol=abs(x-x_prev)/abs(x)
    modified_newton_tolerance.append(tol)
    iterations2.append(i)

    # Iterating until tolerance is reached
    while(tol>0.000001):

        # Checking for the case where exact root is found
        if(f2(x)==0):
            print("Found exact solution")
            print("Function 2 Modified Newton's Method - Root is", x, ", No. of iterations are" , i)
            return(x)
        
        x_prev=x # Storing the value of previous iteration (to calculate tolerance)

        # Next iteration
        x=x_prev-((f2(x_prev)*df2(x_prev))/(df2(x_prev)**2-d2f2(x_prev)*f2(x_prev)))
        i+=1

        # Calculating Relative Error Tolerance and storing it in the array
        tol=abs(x-x_prev)/abs(x)
        modified_newton_tolerance.append(tol)
        iterations2.append(i)

    # Printing and returning final root and number of iterations after exiting the loop    
    print("Function 2 Modified Newton's Method - Root is", x, ", No. of iterations are" , i)
    return(x,modified_newton_tolerance,iterations2)

# Plotting Relative tolerance vs Iteration count for both the methods
plt.figure()
ans,newton_tolerance,iterations=Newtonf2()
ans1,modified_newton_tolerance,iterations2=ModifiedNewtonf2()
plt.plot(iterations,newton_tolerance,'o--',label="Newton's Method")
plt.plot(iterations2,modified_newton_tolerance,'o--',label="Modified Newton's Method")
plt.legend()
plt.xlabel("No. of Iterations")
plt.ylabel("Relative Error")
plt.savefig("./func2.png")



