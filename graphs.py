class Graph: 
      
    # init function to declare class variables 
    def __init__(self,nodes): 
        self.nodes = nodes  
        self.adj = [[] for i in range(nodes)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.nodes): 
            visited.append(False) 
        for v in range(self.nodes): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 
  
# Driver Code 
if __name__=="__main__": 
  

  file = open('n1000.txt','r')
  nodes = int(file.readline())
  print(nodes)
  g=Graph(nodes)
  for i in file:
    a,b = int(i.split(' ')[0]), int(i.split(' ')[1])
    g.addEdge(a,b)
  cc = g.connectedComponents() 
  print("Following are connected components") 
  print(cc) 
  count = 0
  for i in cc:
    count+=1
  print(count)