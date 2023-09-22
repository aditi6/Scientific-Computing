import matplotlib.pyplot as plt

def lagrange(x):
    xi=[1930,1940,1950,1960,1970,1980]
    fx=[28.5,32.4,37.6,45.1,55.8,69.7]
    
    def l(i):
        num=1 # numerator
        den=1 # denominator 
        for t in range(6):
            if(i!=t):
                num=num*(x-xi[t])
            if(i!=t):
                den=den*(xi[i]-xi[t])
        return num/den
    
    p=0
    for i in range(6):
        # Each term of the lagrange polynomial
        p=p+(l(i)*fx[i])

    return p    

x=[1930,1940,1950,1960,1970,1980,1990,2000,2010,2020,2030]
pop=[]

for t in x:
    pop.append(lagrange(t))
plt.plot(x,pop,linestyle='--',marker='o')
plt.xlabel("Year")  
plt.ylabel("Lagrange Polynomial")  
plt.savefig('.\plot1.jpg')


years=[1990,2000,2010,2020]
pop_val=[87.1,105.7,124.1,139.6]
error=0
for i in range(4):
    print(lagrange(years[i]))
    # Mean squared error of the estimates
    error=error+(pop_val[i]-lagrange(years[i]))**2
mean_error=error/4
print("Mean square error is", mean_error)