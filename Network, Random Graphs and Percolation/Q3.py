import sys
import matplotlib.pyplot as plt
import random
import math


class UndirectedGraph:

    #initialiing graph with adj list as a dictionary where key (node) will refer to list (the neighbouring nodes)
    def __init__(self , NoOfVertices = None):
        self.adj_list = {}
        if NoOfVertices is not None:
            self.maxnodes = NoOfVertices                        #maxnode attribut will be the max nodes a graph can have (if initialized with mentioning num of nodes)
            self.NumNodes = NoOfVertices                        #NumNodes attr will be number of nodes which are currently present in graph at that point 
            self.freeGraph = False                              #boolean attr to tell if graph is free graph or not
            for i in range(NoOfVertices):                       #creating adj list if numnodes mentioned which initializing just node and empty lists
                self.adj_list[i+1] = []
        else:
            self.maxnodes = sys.maxsize                         #setting to max size as we can add add any number of nodes in free graph
            self.NumNodes = 0                                   
            self.freeGraph = True
        self.NumEdges = 0                                       #NumEdges attr to tell the number of nodes present in graph at that point
        




    def addNode(self , NodeToAdd ):
        if  isinstance(NodeToAdd , int)  and NodeToAdd > 0:                      #if the graph is not free then checking if the num nodes to add are less than max size  and if the arguement given is valid or not (int)
            if NodeToAdd <= self.maxnodes :                
                if NodeToAdd not in self.adj_list.keys():                                                   #if node is not present then adding node in dictionary (adj list)
                    self.adj_list[NodeToAdd] = []
                    # print(f"added node {NodeToAdd}")
                    self.NumNodes += 1
                return
            else:
                raise Exception("Node index cannot exceed number of nodes")    
        else:
            raise Exception("Input Node to add is Not Valid")        



    #addEdge funtion to add Edge in graph i.e. adding two nodes to graph and adding the other node in adj list of each other
    def addEdge(self , x , y):    
        if isinstance(x , int ) and isinstance(y , int):                                    
            if self.freeGraph:     
                                                
                if x in self.adj_list.keys():                        #if the graph is free (can add any node) 
                    self.adj_list[x].append(y)                      #addint to list assigned to node if node already present
                else:
                    self.adj_list[x] = [y]                          #crating new list and assigning to node in dict

                if y in self.adj_list.keys():
                    self.adj_list[y].append(x)
                else:
                    self.adj_list[y] = [x]
            else:                                                                   
                if x  in self.adj_list.keys() and y in self.adj_list.keys():                                #if graph is not free then we cant add new nodes other than nodes which are present...
                    self.adj_list[x].append(y)                                                               # adding neighbours in the list assigned to node in dict
                    self.adj_list[y].append(x)  
                    self.NumEdges += 1              
                else:
                    raise Exception("Node index not present")      
        else:
            raise Exception("Input Edge is Not Valid")  


         

    def plotDegDist(self):                                          #fun to plot degree distribution 

        FractionOfNodes = [0] * (self.NumNodes )                    #list to store fraction of nodes with degree  (number of nodes with degree i(position))
        X_axis = [i for i in range(self.NumNodes)]                  #list to store values for x axis(just for ploting part if needed)
        
        for i in self.adj_list:                                      #This loop increment Fraction of Node nodes degree (e.g. if some node has 3 edges then incrementing whatever value in FractionOfNodes in 3rd position by 1)
            FractionOfNodes[len(self.adj_list[i])] += 1                
        Total_sum = sum(FractionOfNodes)                              #storing sum of all frations which will be 2 times num of nodes present in graph (as this is undirected graph)
        for i in range(len(FractionOfNodes)):
            FractionOfNodes[i] = FractionOfNodes[i]/Total_sum          #storing fractions 

        #For taking average
        k = 1                                                          #As there will be some nodes without edges so 0 times fraction will lead to incorrect average so staring with 1 and then subtracting 1 from avg we got 
        AvgNodeDegree = 0                                              
        for i in FractionOfNodes:
            AvgNodeDegree += i * k 
            k+=1

        AvgNodeDegree -= 1

    
        #plotting part 

        plt.plot(FractionOfNodes , 'bo' , label = "Actual degree distribution")
        plt.axvline(AvgNodeDegree , color = 'r' , label = "Avg node degree")
        plt.grid()
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")
        plt.title("Node Degree Distribution")
        plt.legend()
        plt.show()


    #siple BFS function

    def bfs(self , start_node):
        n = self.NumNodes
        Q = [start_node]                            #list to store queue
        visited = []                                #list to store visited nodes 

        while Q:                                    # while the queue is not empty this loop will run 
            curr = Q.pop(0)                         #poping / removing the first element from queue list and storing it in curr 
            if curr not in visited:                 #ignoring if already visited
                visited.append(curr)
                for i in self.adj_list[curr]:       #adding all the neighbours in queue
                        Q.append(i)
        return visited

    def isConnected(self):                                                  #isConnect function to check connectness of graph (if every node is connected to by a sigle cluster)
        temp = self.bfs(random.choice(list(self.adj_list.keys())))           #taking random node to start bfs

                                                                            #So Basic idea is to start bfs from any random node and check if we can visit every node in that graph 
        temp.sort()                                                         #Sorting so that its easy to compare lists
        temp2 = [i for i in self.adj_list]                                  #list of all nodes present in graph
        temp2.sort()

        if temp == temp2:                                                    
            return True                                                     #if every node is visited means graph is connected
        else:
            return False                                                    #if any of the node is not visited at the end of BFS then graph is not connected


     
    #fun to return the desired output when print object is called 
    def __str__(self):
        text = f"Graph with {self.NumNodes} nodes and {self.NumEdges} edges. Neighbours of the nodes are belows:\n"
        for i in self.adj_list:
            text += f"Node {i}: " + str(self.adj_list[i]) + '\n'
        return text.replace('[' , '{').replace(']' , '}')
    

    #fun so that we can add two objects of type UndirectedGraph

    def __add__(self , n):
        if isinstance(n , int):                         #when only node to add
            self.addNode(n)                                #calling addNode addEdge to make sure of valid input

        elif isinstance(n , tuple):                      #when edge to be add
            self.addNode(n[0])
            self.addNode(n[1])
            self.addEdge(n[0] , n[1]) 
        return self  





class ERRandomGraph(UndirectedGraph):
    def sample(self , p):
        for x in self.adj_list:                                                                 #looping through all the possible edges
            for y in self.adj_list:
                if y > x:                                                                       #making sure taking edge probability of edge between node 1 and node 2 only once
                    temp = random.choices([True , False] , weights = [p*100 , (1-p)*100])       # temp will have value TRUE with the probebility p
                    if temp[0]:
                        self.addEdge(x,y)

#The Statement is :- erdos-Renyi random graph G(100, p) is almost surely connected only if p > ln 100/100 

def FunToVerifyStatement(NumOFTrials = 1000):                                                  #NumOfTrials to set number of graphs to take result of connectness for each edge probability

    if not isinstance(NumOFTrials , int ) or not NumOFTrials > 0:
        raise Exception("Input Not Valid")

    Y_axis = []
    X_axis = [float(i)/(float(1000)) for i in range(100+1)]                             #list of 100 points from 0.001 to 0.1

    for i in X_axis:
        Ts = 0                                                                          #Ts Fs to see the fraction of simulated experiment
        Fs = 0
        for _ in range(NumOFTrials):

            g = ERRandomGraph(100)                                                       #creating new ERR for taking samples
            g.sample(i)                                                                 #to set probability for edge

            if g.isConnected():
                Ts += 1                                                                 #incrementing Ts if graph is connected
            else:            
                Fs += 1                                                                 #incrementing Fs if graph is not connected
        print(int(i* 1000) , '/', "100")                                                #print statement just to keep track while code is running

        Y_axis.append(Ts/(Ts+Fs))                                                       #appending fraction of positive responce by total responce 


    Threshold = ( math.log(100)* 0.01)                                                   #given theoritical expression  
                                                     
    plt.plot(X_axis , Y_axis , color = 'b')
    plt.axvline(Threshold , color = 'r' , label = "Theoretical threshold")
    plt.title(f"Connectedness of a G({g.NumNodes}, p) as function of p")
    plt.ylabel(f"Fraction of runs G({g.NumNodes},p) is connected")
    plt.xlabel("p")
    plt.legend()
    plt.grid()
    plt.show()


# g = UndirectedGraph(5)
# g = g + (1, 2)
# g = g + (2, 3)
# g = g + (3, 4)
# g = g + (3, 5)
# print(g.isConnected())

g = UndirectedGraph(5)
g = g + (1, 2)
g = g + (2, 3)
g = g + (3, 5)
print(g.isConnected())


# g = UndirectedGraph(6)
# g = g + (1, 2)
# g = g + (2, 3)
# g = g + (3, 4)
# g = g + (3, 5)
# print(g)
# a = g.bfs(1)
# print(a)

# print(g.isConnected())



FunToVerifyStatement(100)                                              #You can reduce this number for fast result but graph will be from less sample                                                      