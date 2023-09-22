import math
def f(x):
    ans= (2/(1+19*math.exp(-10*x)))-1
    return ans


def secant():
    x_prev=1/12
    x0=0.99
    i=1
    x1 = x0 - f (x0)*(x0-x_prev)/(f(x0)-f(x_prev))
    if(f(x1)==0):
        print(x1,i)     
        return x1,i
    x2 = x1 - f (x1)*(x1-x0)/(f(x1)-f(x0))
    i+=1
    if(f(x2)==0):
        print(x2,i)     
        return x2,i
    xn_prev=x1
    xn=x2
    
    while(abs(xn-xn_prev)/abs(xn)>0.0001):
        xn_next = xn - f(xn)*(xn-xn_prev)/(f(xn)-f(xn_prev))
        i+=1
        if(f(xn_next)==0):
            print(xn_next,i)     
            return xn_next,i
        xn_prev=xn
        xn=xn_next
    print(xn,i)    
    return(xn,i)   

ans,i=secant()