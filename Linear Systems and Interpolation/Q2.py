
import random 
import numpy as np 
from Q1 import RowVectorFloat 

# define a custom class for a square matrix of float numbers
class SquareMatrixFloat(RowVectorFloat):
  
  # constructor to initialize the matrix with given dimensions
  def __init__(self , n):
    if not isinstance(n , int):                             #exception 
      raise Exception("Invalid Input")
    self.Mat = [[0] * n] * n  # create an empty matrix with all elements initialized to 0
    self.N = len(self.Mat)   # store the dimension of the matrix

  # method to return the matrix as a string for printing
  def __str__(self):
    text = "the matrix is:\n"
    for i in self.Mat:
      for j in i:
        text += str(j) + " "
      text += '\n'
    return text

  # method to generate a random symmetric matrix with positive diagonal elements
  def sampleSymmetric(self):
    n = self.N
    temp2 = []
   
    for i in range(n):
      temp_list  = []
      for j in range(n):
        temp_list.append(0)
      temp2.append(temp_list)
    for i in range(n):
      temp2[i][i] = round(random.uniform(0,n) , 3)  # generate a random number for the diagonal element
      for j in range( i + 1 ,n):
        temp =  round(random.uniform(0,1) , 3)  # generate a random number for the off-diagonal element
        temp2[i][j]  = temp
        temp2[j][i] = temp  # assign the same value to the symmetric element
    self.Mat = temp2  # store the generated matrix in the object

  # method to convert the matrix to its row echelon form
  def toRowEchelonForm(self):
    n = self.N
    for i in range(n):
      for j in range(i+1):
        first = self.Mat[i][j]  # get the first non-zero element in the current row
        for k in range(n):
          self.Mat[i][k] = round(self.Mat[i][k] / first , 2)  # divide the row by the first element to make it the leading 1
        if i > j:
          for k in range(n):
            self.Mat[i][k] = self.Mat[j][k] - self.Mat[i][k]  # subtract the current row from the previous row to make all the elements below the leading 1 zero
            if  self.Mat[j][k] - self.Mat[i][k] == 0.0:
              self.Mat[j][k] = 0.0  # set any element that becomes zero to exactly 0

  # method to check if the matrix is diagonally dominant
  def isDRDominant(self):
    n = self.N

    for i in range(n):
      diag = 0
      non_diag = 0
      for j in range(n):
        if i == j:
          diag = abs(self.Mat[i][j])  # adding the absolute value of the diagonal element
        else:
          non_diag += abs(self.Mat[i][j])  # adding the absolute value of the off-diagonal elements
      if diag < non_diag:  # check if the diagonal element is smaller than the sum of off-di
        return False
    return True

  def jSolve(self, givenlist , NumIterations):
    # Solve the linear system using Jacobi method
             
    if not self.isDRDominant():
      raise Exception("<class 'Exception'>\nNot solving because convergence is not guranteed.")

    temp_mat = self.Mat
    err = []
    print(self)
    prev_itr = [0] * self.N                     #to  store values of previous iterations
    for _ in range(NumIterations):

      itrs = prev_itr[:]
      prev_itr = [0] * self.N
      #as in the formula finding valie for x(k)
      for i in range(self.N):
        for j in range(self.N):
          if i != j:
            prev_itr[i] -= temp_mat[i][j] * itrs[j] / temp_mat[i][i]
          else:
            prev_itr[i] += givenlist[i] / temp_mat[i][i]
      err.append(np.linalg.norm(np.dot(temp_mat , prev_itr) - givenlist))
    return (err,prev_itr)







  def gsSolve(self , givenlist , NumIterations):
    # Solve the linear system using Gauss-Siedel method 


    if not self.isDRDominant():
      raise Exception("<class 'Exception'>\nNot solving because convergence is not guranteed.")


    itrs = []                                                                #to store value at current iteration 
    prev_itr = [0] * self.N                                                   # to store values of previous iterations
    temp_mat = self.Mat
    err = []
    print(self)
    for _ in range(NumIterations):
      itrs = [0] * self.N
      for i in range(self.N):
        for j in range(self.N):
          if i != j:
            if i > j:
              itrs[i] -= temp_mat[i][j] * itrs[j] / temp_mat[i][i]
            else:
              itrs[i] -= temp_mat[i][j] * prev_itr[j] / temp_mat[i][i]
          else:
            itrs[i] += givenlist[i] / temp_mat[i][i]
          
      prev_itr = itrs[:]      
      err.append(np.linalg.norm(np.dot(temp_mat ,prev_itr) - givenlist))
    return (err,prev_itr)

if __name__ == "__main__":
  # print("1...")
  # s = SquareMatrixFloat(3)
  # print(s)
  # print("\n2'''")
  # s = SquareMatrixFloat(4)
  # s.sampleSymmetric()
  # print(s)
  # s.toRowEchelonForm()
  # print(s)
  # print("\n3..")
  s = SquareMatrixFloat(4)
  s.sampleSymmetric()
  print(s.isDRDominant())
  (e, x) = s.jSolve([1, 2, 3, 4], 10)
  print(x)
  print(e)


