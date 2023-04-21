import matplotlib.pyplot as plt
import random
 
def estimatePi(n):
    PointsInCircle = 0
    PointsInSquare = 0
    fraction = []
    x = []
    valueOfPi = []
    for i in range(n):
        x.append(i)
        valueOfPi.append(3.14)
        x_point = random.uniform(-1 , 1 )
        y_point = random.uniform(-1 , 1)
        PointsInSquare = PointsInSquare + 1                                               #Everytime the point will lie in square
        if x_point * x_point + y_point * y_point <= 1 :                                    #cheking if point lie in circle or not 
            PointsInCircle = PointsInCircle + 1
        fraction.append(4 * float(PointsInCircle)/float(PointsInSquare))                   #Estimated value for pie


    #plotting

    plt.plot(x , fraction , color = 'b' , label = "Monte Carlo method") 
    plt.plot(x , valueOfPi , color = 'r' , label = "Value of math pi")
    plt.title("Estimating pi usign Monte Carlo Method")
    plt.xlabel("No. of points generated")
    plt.ylabel("4 x fraction of points within the circle")
    plt.ylim(3.10,3.20)
    plt.grid(linestyle = '--')
    plt.legend()
    plt.show()
    return fraction


estimatePi(200000)
        
        
