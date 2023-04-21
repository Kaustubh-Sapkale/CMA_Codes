from poly import Polynomial
import math

def legendre_poly( n=0):

    if not isinstance(n , int):
        raise Exception("Invalid Input n should be int")
    if n < 0:
        raise Exception("Invalid Input n should be nonnegative")
    
    #as per the formula given for langendre polynomial 

    num = Polynomial([-1, 0, 1]) ** n
   

    for i in range(n):
        num = num.derivative()

    ans = num / (2**n * math.factorial(n))

    return ans



if __name__ == "__main__":

    print(legendre_poly(0))

    print(legendre_poly(1))


    print(legendre_poly(2))



