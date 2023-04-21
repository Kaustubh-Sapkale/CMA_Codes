#class RowVectorFloat 
class RowVectorFloat:
  def __init__(self ,  GivenList = None): 
    if not isinstance(GivenList , list):
      raise Exception("Invalid Input List") 
                    
    self.CurrList = GivenList                                   #CurrList attribute to store vector


  #fun to return desired text as output 
  def __str__(self):
    text = ""
    for i in self.CurrList:
      text += str(i) + ' '
    return text 


  #def fun so that object can tell len when len() is called 
  def __len__(self):
    return len(self.CurrList)


  #fun to make the object iterable so that it can tell value at required index 
  def __getitem__(self , i):
    if not isinstance(i , int):
      raise Exception("Invalid index")
    if i > len(self):
      raise Exception("Out of Index")
    return self.CurrList[i]


  #fun to set value at required index 
  def __setitem__(self , i , value):
    if i > len(self):
      raise Exception("Out of Index")

    self.CurrList[i] = value

  #defining function so that two objects can perform multiply operation
  def __mul__(self , r1):
    temp = []
    #basically we are multiplying values at same index if there are two vectors, if one of them is scalar then multiplying that scalar with each value of vector
  
    if isinstance(self , int) or isinstance(r1 , int):
      if  isinstance(self , int) and isinstance(r1 , int):
        return self * r1
      elif isinstance(self , int):
        for i in r1:
          temp.append(self * i)
        return RowVectorFloat(temp)
      elif isinstance(r1 , int):
        for i in self:
          temp.append(r1 * i)
        return RowVectorFloat(temp)
    else:
      for i in range(len(r1)):
        temp.append(self[i] * r1[i])
      return RowVectorFloat(temp)
  
  #defing fun to multiply objects with scalar 
  def __rmul__(self , scalar):

    return self.__mul__(scalar)

  #defing fun to add object with scalar 
  def __radd__(self , scalar):
    return self.__add__(scalar)

  #defining fun to add onjects
  def __add__(self , r1):
    temp = []
    #basically we are adding values which are at same index

    if isinstance(self , int) or isinstance(r1 , int):
      if  isinstance(self , int) and isinstance(r1 , int):
        return self + r1
      elif isinstance(self , int):
        for i in r1:
          temp.append(self + i)
        return RowVectorFloat(temp)
      elif isinstance(r1 , int):
        for i in self:
          temp.append(r1 + i)
        return RowVectorFloat(temp)
    else:
      for i in range(len(r1)):
        temp.append(self[i] + r1[i])
      return RowVectorFloat(temp)

  #fun so that we can subtract scalar from object
  def __rsub__(self , scalar):
    return self.__sub__(scalar)

  #fun so that we can subtract objects
  def __sub__(self , r1):
    temp = []

    if isinstance(self , int) or isinstance(r1 , int):
      if  isinstance(self , int) and isinstance(r1 , int):
        return self - r1
      elif isinstance(self , int):
        for i in r1:
          temp.append(self - i)
        return RowVectorFloat(temp)
      elif isinstance(r1 , int):
        for i in self:
          temp.append(r1 - i)
        return RowVectorFloat(temp)
    else:
      for i in range(len(r1)):
        temp.append(self[i] - r1[i])
      return RowVectorFloat(temp)


if __name__ == "__main__":

  r1 = RowVectorFloat([1, 2 , 4])
  r2 = RowVectorFloat([1, 1 , 1])
  r3 = 2*r1 + (-3)*r2
  print(r3)

  