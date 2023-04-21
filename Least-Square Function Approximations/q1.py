import numpy as np
import matplotlib.pyplot as plt
from poly import Polynomial

def bestfit(n , given_points):
    if not isinstance(n , int):
        raise Exception("invalid input n should be number")
    if not isinstance(given_points , list):
        raise Exception(f"invalid input {given_points} is not list")
    if len(given_points) != 0:
        
        for i in given_points:
            if not type(i) is tuple:
                raise Exception(f"Elements in the list are not tuple of points")
            if len(i) != 2:
                raise Exception(f"Elements in the list are not tuple of two points")
            if not isinstance(i[0] , (int , float)) or not isinstance(i[1] , (int , float)):
                raise Exception(f"Invalid input {i} in the {given_points}")
    

    x_points = [x for x,y in given_points]
    y_points = [y for x,y in given_points]

    #as per the equation given in the ppt computing matrix and vector
    #Ax = B
    A = []
    for j in range(0, n + 1):
        row = []
        for k in range(0, n + 1):
            row_sum = 0
            for i in range(len(given_points)):
                row_sum += x_points[i] ** (j + k)
            row.append(row_sum)
        A.append(row)
    
    B = []
    for j in range(0, n + 1):
        row_sum = 0
        for i in range(len(given_points)):
            row_sum += y_points[i] * (x_points[i] ** j)
        B.append(row_sum)

    #solving matrix wrt the vector 
    ans = Polynomial(list(np.linalg.solve(A, B)))

    ans.show(min(x_points) , max(x_points))
   
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_points , y_points , "ro" ,  label = "Input Points" )
    plt.show()
    return ans

    
    

if __name__ == "__main__":
    newpol = bestfit(5 , [(1,2) , (2,3) , (5,6) , (4,4) , (6,7)])
    print(newpol)

