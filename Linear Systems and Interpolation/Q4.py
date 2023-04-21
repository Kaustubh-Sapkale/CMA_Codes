
import numpy as np
import matplotlib.pyplot as plt
import math


class Polynomial:

  def __init__(self , given_list = []):
      self.coefficient_list = given_list                    #coefficient attribute so that we can get list of coefficient at that point of time 
      self.Len = len(self.coefficient_list)                 #Len attribut so that we can get lenth of coefficient list (degree of polynomial +1)
      self.title = "None"                                   #title attribute so that we can get which method is used to solve system of linear equations 
  
  # method to return the matrix as a string for printing
  def __str__(self):
    text = "Coefficients of the polynomial are:\n"
    for i in self.coefficient_list:
      text += str(i) + ' '
    return text

  def __getitem__(self , x):
    ans = 0
    for i in range(len(self.coefficient_list)):
        ans += self.coefficient_list[i] * pow(x , i)
    return ans

  def __add__(self , toadd):
    if self.Len < toadd.Len:
      needed = self.coefficient_list
      for i in range(toadd.Len - self.Len):
        needed.append(0)
      self = Polynomial(needed)
    elif self.Len > toadd.Len:
      needed = toadd.coefficient_list
      for i in range(self.Len - toadd.Len):
        needed.append(0)
      toadd = Polynomial(needed)

    # print(f"adding {self.coefficient_list} and {toadd.coefficient_list}")
    temp = [0] * self.Len
    for i in range(len(temp)):
      temp[i] = self.coefficient_list[i] + toadd.coefficient_list[i]
    #   print(f"adding {self.coefficient_list[i]}  {toadd.coefficient_list[i]} numbers and the result is {temp[i]}")
    # print(f"returning added polynomial which is {temp}")
    return Polynomial(temp)

  def __sub__(self , tosub):
    temp = [0] * self.Len
    for i in range(tosub.Len):
      temp[i] = self.coefficient_list[i] - tosub.coefficient_list[i]
    return Polynomial(temp)




    
  def __mul__(self , tomul):
    if isinstance(self , Polynomial) and isinstance(tomul , Polynomial):
        if self.Len < tomul.Len :
            for i in range(tomul.Len - self.Len):
                self.coefficient_list.append(0)

        if self.Len > tomul.Len :
            for i in range( self.Len - tomul.Len ):
                tomul.coefficient_list.append(0)

        temp = [0] * (self.Len + tomul.Len )
        for i in range(self.Len):
            for j in range(tomul.Len):
                temp[i+j] += tomul.coefficient_list[j] * self.coefficient_list[i]
        
        while(temp[-1] == 0):
            temp.pop()   
        return Polynomial(temp)


    temp = [0] * self.Len
    
    for i in range(self.Len):
      temp[i] = self.coefficient_list[i] * tomul
    return Polynomial(temp)

  def __rmul__(self , scalar):
    return self.__mul__(scalar)

  def __radd__(self , scalar):
    return self.__add__(scalar)



  def show(self , x , y):
    y_axis = []
    x_axis = list(np.linspace(x,y , num=50))
    for i in x_axis:
        y_axis.append(self[i])



    #plotting 
    plt.plot(x_axis , y_axis , color = 'b')


    if self.title == 'None':
        text = f"Plot of the polynomial ({self.coefficient_list[0]}) "
        for i in range(1 ,len(self.coefficient_list)):
            text +='+(' + str( self.coefficient_list[i]) + ') x^' + str(i) 

        plt.title(text)
    elif self.title == 'fitMat':
        plt.title("Polynomial interpolation using matrix method")
    elif self.title == 'fitLag':
        plt.title("Interpolation using Lagrange polynomial")

        
    plt.ylabel("p(x)")
    plt.xlabel("x")
    plt.grid()
    plt.show()

  def fitViaMatrixMethod(self , given_list):
    #by solving system of equaitons using matrix methods. first finding inveted matrix of A. then premultiplying with matrix b. the result of multiplication will be the solution of system of equations
    NumOfPoints = len(given_list)

    Mat_A = []
    Mat_B = []
    min_x = math.inf
    max_x = -1 * math.inf
    x_points = []
    y_points = []
    for (i , j) in  given_list:
        temp_list = []
        if i < min_x:
            min_x = i
        if i > max_x:
            max_x = i
        for k in range(NumOfPoints):
            temp_list.append(pow(i , k))    
        Mat_A.append(temp_list)
        Mat_B.append([j])
        x_points.append(i)
        y_points.append(j)
    
    # print(Mat_A)
    # print(Mat_B)

    Inv_Mat_A = np.linalg.inv(Mat_A)
    # print(Inv_Mat_A)
    Res = np.dot(Inv_Mat_A , Mat_A)
    Res2 = np.dot(Inv_Mat_A , Mat_B)

    for i in range(NumOfPoints):
        for j in range(NumOfPoints):
            Res[i][j] = round(Res[i][j] , 3)
            
    # print(Res)
    # print(Res2)
    Final_Polynomial = []
    for i in Res2:
        Final_Polynomial.append(round(i[0] , 3))
    new_p = Polynomial(Final_Polynomial)
    new_p.title = 'fitMat'
    plt.scatter(x_points , y_points , color = 'r')
    new_p.show(min_x , max_x)
  



  def fitViaLagrangePoly(self , givenlist):
    #finding langrange polynomials first and then by using formula solving for the required equation
    NumOfPoints = len(givenlist)
    Lang_Poly = []

    min_x = math.inf
    max_x = -1 * math.inf
    x_points = []
    y_points = []
    for (i , j) in  givenlist:
        if i < min_x:
            min_x = i
        if i > max_x:
            max_x = i
        x_points.append(i)
        y_points.append(j)


    for i in range(NumOfPoints):
      f = 0
      temp = Polynomial([])
      for j in range(NumOfPoints):
        if i != j:
          if temp.Len == 0:
            temp = temp + Polynomial([-1 * givenlist[j][0] / (givenlist[i][0] - givenlist[j][0]), 1 / (givenlist[i][0] - givenlist[j][0])])
          else:
            temp *=  Polynomial([-1 * givenlist[j][0] / (givenlist[i][0] - givenlist[j][0]), 1 / (givenlist[i][0] - givenlist[j][0])])

      Lang_Poly.append(temp)

    
    Final_Poly = givenlist[0][1]*Lang_Poly[0]
    for i in range(1,len(givenlist)):
      Final_Poly += givenlist[i][1] * Lang_Poly[i]
    
    Final_Poly.title = "fitLag"
    plt.scatter(x_points , y_points , color = 'r')
    Final_Poly.show(-1 , 3)
      



if __name__ == "__main__":
  # print("1..")
  # p1 = Polynomial([1, 2, 3])
  # print(p1)

  # print("\n2..")
  # p2 = Polynomial([3, 2, 1])
  # p3 = p1 + p2
  # print(p3)

  # print("\n3..")

  # p1 = Polynomial([1, 2, 3])
  # p2 = Polynomial([3, 2, 1])
  # p3 = p1 - p2
  # print(p3)

  # print("\n4..")
  # p1 = Polynomial([1, 2, 3])
  # p2 = (-0.5)*p1
  # print(p2)
    
  # print("\n5..")
  # p1 = Polynomial([-1, 1])
  # p2 = Polynomial([1, 1, 1])
  # p3 = p1 * p2
  # print(p3)

  # print("\n6..")
  # p = Polynomial([1, 2, 3])
  # print(p[2])

  # print("\n7..")

  # p = Polynomial([1, -1, 1, -1])
  # p.show(-1, 2)


  # p = Polynomial([])
  # p.fitViaMatrixMethod([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])
  # p.fitViaMatrixMethod([(0,1) , (1,4) , (-1,0) , (2,15)])

  p = Polynomial([])
  p.fitViaLagrangePoly([(1,-4), (0,1), (-1, 4), (2, 4), (3,1)])
  # p.fitViaLagrangePoly([(0,1) , (1,4) , (-1,0) , (2,15)])
