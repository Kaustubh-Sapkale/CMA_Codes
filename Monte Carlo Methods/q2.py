import sys
import matplotlib.pyplot as plt
import random
import numpy as np


###    Exception    ###
class LessSideException(Exception):
    #exception when the number of sides is less than 4
    pass
class NotIntException(Exception):
    #exception when the input is not integer
    pass
class SumNotValid(Exception):
    #exception when the sum of probability distribution is not 1
    pass

###                ###

###     Declaring Class
class Dice:


    def __init__(self, numSides = 6):

        self.numSides  = numSides
        
        try:
            if not isinstance(numSides , int):
                raise NotIntException  
        except NotIntException:
            print("<class 'Exception'>\nCannot construct the dice")
            sys.exit()

        try:
            if numSides < 4:
                raise LessSideException  
        except LessSideException:
            print("<class 'Exception'>\nCannot construct the dice")
            sys.exit()


        self.Prob_Dist = [1.0/float(self.numSides)] * numSides                  #default Probability Distribution when its not mention

        

    def __str__(self ):
        return f'Dice with {self.numSides} faces and probability distribution {tuple(self.Prob_Dist)}'.replace('(' , '{').replace(')' , '}')
    
    
    def setProb(self , new_Prob_Dist ):

        try:
            if sum(new_Prob_Dist) != 1 or len(new_Prob_Dist) != self.numSides:
                raise SumNotValid
        except SumNotValid:
            print("<class 'Exception'>\nInvalid probability distribution")
            sys.exit()


        self.Prob_Dist = list(new_Prob_Dist)
    
    def roll(self , num_throws):

        expected = [0] * self.numSides
        freq = [0] * self.numSides
        x_axis = []


        for i in range(self.numSides):
            x_axis.append(i+1)
            self.Prob_Dist[i] = 10 * self.Prob_Dist[i]


        #Expected results   << probability * num of throws >>
        for i in range(self.numSides):
            expected[i] = num_throws * self.Prob_Dist[i] / 10
        

        #Simulated results      << taking random sample >> 
        for i in range(num_throws):
            temp = random.choices(range(0 ,  self.numSides , 1) , weights=self.Prob_Dist , k=1)
            freq[temp[0]] = freq[temp[0]]+1
            

        #plotting        
        X_axis = np.arange(len(x_axis))
        
        plt.bar(X_axis - 0.1, freq ,color = 'b' , width = 0.2, label = 'Actual'  )
        plt.bar(X_axis + 0.1, expected, color = 'r' , width= 0.2, label = 'Expected')
        
        plt.xticks(X_axis, x_axis)
        plt.xlabel("Sides")
        plt.ylabel("Occurrences")
        plt.title(f'Outcome of {num_throws} throws of a {self.numSides}-faced dice')
        plt.legend()
        plt.show()






#MAIN CODE 


d = Dice("4")
d.setProb((0.1, 0.2, 0.3, 0.3, 0.1 ))
d.roll(10000)
print(d)