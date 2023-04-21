import matplotlib.pyplot as plt
import networkx as nx
import random

class Lattice:
    def __init__(self, n):

        if n < 0 or not isinstance(n, int):
            raise Exception("Input not Valid. Cant make Lattice with given n")
        self.G = nx.empty_graph(n**2)                                                   #creating empty graph using networkx.free_graph attr G will have the graph comtaining nodes
        self.pos = {i:(i//n,i%n) for i in range(n**2)}                                  #pos attr will have position of each node present if Lattice 
        self.len = n                                                                    #len attr will return tha size of side of Lattice 
        self.percolated = False                                                         #percolated boolean attr which will tell if graph is percolated or not till that point 
        self.top_nodes = [n*(i+1)-1 for i in range(n)]                                  #top_nodes attr will have list of all the top nodes in the lattice
        self.bottom_nodes = [n*i for i in range(n)]                                     #bottom_nodes attr will have list of all the bottom nodes in the lattice
        self.edge = []                                                                  #edge attr will have list of all the edges in form of tuple 



    def nodes(self):                                                                    #fun to return nodes present in graph
        return self.G.nodes()


    def show(self):                                                                      #show fun to plot the lattice 
        colors = nx.get_edge_attributes(self.G,'color').values()                         #list which will store color for each edge 
        widths = nx.get_edge_attributes(self.G,'width').values()                         #list which will store width of each edge

        if self.percolated:                                                                                                     #if percolated then ploting only edges 
            nx.draw(self.G, self.pos, node_size=0 , node_color='b' , edge_color = colors , width = list(widths))
        else:                                                                                                                   #else plotting point lattice 
            nx.draw(self.G, self.pos, node_size=1 , node_color='b')
        plt.axis('off')
        plt.show()


    def AddEdge(self , x , y):                                                            #fun to add edge in lattice                                                        
        if max(x , y) > self.len*self.len or min(x , y) < 0:
            raise Exception("Node not found in Lattice")
        self.edge.append((x,y))                                                           #adding edge in attr list 
        self.edge.append((y,x))
        self.G.add_edge(x , y , color = 'r'  , width = 1)                                   # adding edge in graph 


    def percolate(self , p):
        if p > 1 or p < 0:
            raise Exception("Enter Valid value for p")

        if p != 0:
            self.percolated = True                                                      #changing value of boolean attr percolated     
        for x,y in self.allPossibleEdge() :                                             #looping through all possible edges 
            temp = random.choices([True , False] , weights = [p*100 , (1-p)*100])       #True with the probability p else false
            if temp[0]:
                self.AddEdge(x,y)


    def getLen(self):                                                                   #fun to get Len of side  Lattice 
        return self.len

   
    def allPossibleEdge(self):                                                           #fun to get all possible edges present in Lattice 
        pos = []
        for n in range(self.getLen()* self.getLen()):                                     #looping through all the nodes and then appending all possible edges in vertical direction in list
            if (n+1)%self.getLen() != 0:
                pos.append((n , n+1))
        for n in range(self.getLen()*(self.getLen()-1)):                                   # -------- horizontal direction ---------   
            pos.append((n , n+self.getLen()))
        return pos
    
    def existsTopDownPath(self):                                                             #fun to check if there exist path from top to bottom
        for node in self.top_nodes:
            for node2 in self.bottom_nodes:                                                 #looping through all the top and bottom edges 
                if nx.has_path(self.G, node, node2):                                        #usign has path function of networkx to check if there exist path between node 1 and node 2
                    return True                                                             #if there is path function will return True
        return False                                                                        #after looping through all nodes if there is no path then return false 
    
    def bfs(self , start_node):
        n = self.getLen()
        Q = [start_node]                                                                    #queue for BFS
        visited = []                                                                        #visited list to store nodes which are visited till that point 
        while Q:
            curr = Q.pop(0)                                                                 #storing first element for queue in curr and removing from queue
            
            if curr not in visited:                                                         #if its not in visited adding all its neighbours in queue for next search 
                visited.append(curr)                                                        
                if curr + 1 not in visited and (curr, curr+1) in self.edge:                       
                        Q.append(curr+1)
                if curr - 1 not in visited and (curr , curr -1) in self.edge:
                        
                        Q.append(curr-1)
                if curr + n not in visited and curr + n < n * n and (curr , curr + n) in self.edge:                       
                        Q.append(curr+n)
                if curr - n not in visited and curr -n > -1 and (curr , curr - n) in self.edge:
                        
                        Q.append(curr-n)
        return visited                                                                          #returning list of visited nodes if we start BFS from start node 
    
    
    def showPaths(self ):                                                                       #show path fun to mark longest shortest path or path from top to bottom 
        shortest_paths = {}                                                                     #dict to store longest shortest path or path from top to bottom from node X (node will refer to list of nodes which is path which start from node X )
        bottomNodes = self.bottom_nodes
        for node in self.top_nodes:                                                             #looping through top nodes and bottom nodes if there exist path, if yes then assigning path to node in the dictionary
            print(f"{(node + 1)/len(self.top_nodes)}/{len(self.top_nodes)}")
            for node2 in bottomNodes:
                if nx.has_path(self.G, node, node2):
                    temp_list = nx.shortest_path(self.G , node, node2)
                    if node not in shortest_paths.keys():                                       #checking for shortest path from all the top to bottom paths from Node X
                        shortest_paths[node] = temp_list
                    else:
                        if len(shortest_paths[node]) > len(temp_list):
                            shortest_paths[node] = temp_list
                else:
                    bottomNodes.remove(node2)                                                   #for optimizing loops... if there is no path to bottom node then there wont be shortest path to that bottom node from next top nodes 
  
        for node in self.top_nodes:                                                             #for longest shortest paths if there is not path from top to bottom from that certain node
            if node not in shortest_paths.keys():
                temp = self.bfs(node)                                                           #BFS will give the deepest depth(last node which is visited) which is longest path which exist 
                temp_list = nx.shortest_path(self.G , node, temp[-1])
                shortest_paths[node] = temp_list

                

        for i in shortest_paths:
            for j in range(len(shortest_paths[i])-1):
                self.G.add_edge(shortest_paths[i][j] , shortest_paths[i][j+1] , color = '#458B00' , width = 2 )                             #changing color of edges of paths which are in the dictionary

        self.show()
        
    def numeinB(self):
        numofedge = 0
        for i in self.bottom_nodes:
            for x,y in self.edge:
                if i==x :
                    numofedge += 1
        return numofedge


if __name__ == "__main__":
    # l = Lattice(25)
    # l.show()

    l = Lattice(5)
    l.percolate(0.4)
    l.show()
    print(l.numeinB())
    

    # l = Lattice(25)
    # l.percolate(0.4)
    # l.show()
    # print(l.existsTopDownPath())

    # l = Lattice(100)
    # l.percolate(0.4)
    # l.showPaths()

    # l = Lattice(100)
    # l.percolate(0.7)
    # l.showPaths()





