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
                    self.adj_list[x] = [y]                          #creating new list and assigning to node in dict

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


   
    def OneTwoComponentSizes(self):                     #fun to return size of largest and second largest connected component in graph
        components = []                                 #list to store tuple of connected components (which is tuple of  nodes present in connected component)
        present = []                                    #sized will store size of connected component present in graph
        sizes = []

        
        for i in self.adj_list:                          #looping through all the nodes present in the graph 
            if i not in present:                          #if node is already present in previout components then skipping that node 
                temp = self.bfs(i)                       #if node is not in any of the present components then starting BFS from that node
                for Neighbours in temp:
                    present.append(Neighbours)
                components.append(tuple(temp))          #storing all the visited nodes from that node using BFS in tuple (which will be one connected component)
        for i in components:
          sizes.append(len(i))                          #storing sizes of components 
        sizes.sort()                                    #sorting to return last two as result 
        if len(sizes) != 1:                             #condition to check if only one component is present or many
          return [sizes[-1] , sizes[-2]]                #returning size of largest and 2nd largest component
        else:
          return [sizes[-1] , 0]                        #returning size of largest component and 0 as there is only one component










class ERRandomGraph(UndirectedGraph):
    def sample(self , p):
        for x in self.adj_list:                                                                 #looping through all the possible edges
            for y in self.adj_list:
                if y > x:                                                                       #making sure taking edge probability of edge between node 1 and node 2 only once
                    temp = random.choices([True , False] , weights = [p*100 , (1-p)*100])       # temp will have value TRUE with the probebility p
                    if temp[0]:
                        self.addEdge(x,y)

#Statement :- If p < 0.001, the Erd ̋os-R ́enyi random graph G(1000, p) will almost surely have only small connected components. On the other hand, if p > 0.001, almost surely, there will be a single giant component containing a positive fraction of the vertices.

def FunToVerifyStatement(NumOFTrials = 50):

    if not isinstance(NumOFTrials , int ) or not NumOFTrials > 0:
        raise Exception("Input Not Valid")
   
    Largest = []                                                            #list to store fraction of number of nodes present in largest component to total number of nodes present in graph
    second_largest = []                                                     #list to store fraction of number of nodes present in second largest component to total number of nodes present in graph
    X_axis = [float(i)/(float(10000)) for i in range(100+1)]                #list containing 100 points from 0.0001 to 0.01
    #simulating result for every p
    for p in X_axis:
        L = 0
        SL = 0
        for _ in range(NumOFTrials):
          g = ERRandomGraph(1000)
          g.sample(p)
          temp = g.OneTwoComponentSizes()
          L += temp[0]                                                      #L will have size of largest component
          SL += temp[1]                                                     #SL will have size of 2nd largest component
        print(int(p* 10000) , '/', "100")
        Largest.append(L/g.NumNodes * NumOFTrials )                          #storing fraction of number of nodes present in largest component to total number of nodes present in graph
        second_largest.append(SL / g.NumNodes * NumOFTrials)                 #storing fraction of number of nodes present in second largest component to total number of nodes present in graph

    # Threshold = ( math.log10(100) / math.log10(math.e)) * 0.01
    plt.plot(X_axis , Largest , color = 'g' , label ="Largest connected component" )
    plt.plot(X_axis , second_largest , color = 'b' , label = "2nd largest connected component")
    plt.axvline(1/g.NumNodes , label = " Largest CC size threshold" , color = 'r')
    plt.axvline(math.log(g.NumNodes)/g.NumNodes , label = "Connectedness threshold" , color = 'y')
    # plt.axvline(Threshold , color = 'r' , label = "Theoretical threshold")
    plt.title(f"Fraction of nodes in the largest and second-largest connected components (CC) of  G({g.NumNodes}, p) as function of p")
    plt.ylabel(f"Fraction of runs G({g.NumNodes},p) is connected")
    plt.xlabel("p")
    plt.legend()
    plt.show()





g = UndirectedGraph(6)
g = g + (1, 2)
g = g + (3, 4)
g = g + (6, 4)
print(g.OneTwoComponentSizes())

# FunToVerifyStatement(50)
