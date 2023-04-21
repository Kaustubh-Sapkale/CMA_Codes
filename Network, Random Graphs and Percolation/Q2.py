import sys
import matplotlib.pyplot as plt
import random

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
            raise Exception("Input Node is Not Valid")  


         
     

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

        plt.scatter(X_axis , FractionOfNodes , label = "Actual degree distribution" , s = 8)
        plt.axvline(AvgNodeDegree , color = 'r' , label = "Avg node degree")
        plt.grid()
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")
        plt.title("Node Degree Distribution")
        plt.legend()
        plt.show()




    
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


# g = ERRandomGraph(100)
# g.sample(0.7)
# g.plotDegDist()

g = ERRandomGraph(1000)
g.sample(0.4)
g.plotDegDist()
