import math
def f(x):
    return (2/(1+19*math.exp((-10)*x)))-1

def secant(x0,x1):
    xn=0
    while 1>0:
        xn=x1-f(x1)*((x1-x0)/(f(x1)-f(x0)))
        if(abs(xn-x1)/abs(xn)<10**(-4)):
            return xn
        x0=x1
        x1=xn
print(secant(0.1155,0.99))
