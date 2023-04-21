import matplotlib.pyplot as plt
import math

def LogOfFactorial(n):
    list1 = [0]
    for i in range (2 , n):
        list1.append(list1[-1] + math.log10(i))                 #  log(n!) = log((n-1)!) + log(n) 
    return list1


def stirling(n):                                                
    return (n/math.e)**n * math.sqrt(2*math.pi*n)

def LogOfStirling(n):
    return 0.5 *( math.log10(2 * math.pi * n) ) + n *(math.log10(n/math.e))

#main code 

x = range(1 , 1000000)


y1 = [LogOfStirling(i) for i in x]
Y1 = LogOfFactorial(1000000)

plt.plot(x, Y1 , label="Log of Factorial" , color = 'r')
plt.plot(x, y1, label="Log of Stirling approximation" , color = 'b' , linestyle='dashed')
plt.title("Visualisation of Stirling's approximation" , loc='center')
plt.xlabel("n")
plt.ylabel("Log10(n!)")
plt.legend()
plt.show()
