#file to find all connected components in a graph
import sys
sys.setrecursionlimit(100000)
class Graph: 
    # init function 
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
    def connectedComponents(self): 
        visited = [] 
        connected = [] 
        for i in range(self.nodes): 
            visited.append(False) 
        for v in range(self.nodes): 
            if visited[v] == False: 
                temp = [] 
                connected.append(self.DFSUtil(temp, v, visited)) 
        return connected 
  
def run(filename):
    file = open(filename,'r')
    nodes = int(file.readline())
    graph = Graph(nodes)
    for i in file:
        numbers = i.split(' ')
        a,b = int(numbers[0]),int(numbers[1])
        graph.addEdge(a,b)

    #print connected components
    connected_components = graph.connectedComponents()
    print("The Following are Connected Components:")
    print(connected_components)
    
    #print number of connected components
    count = 0 
    for i in connected_components:
        count+=1
    print('\n')
    print(f"There are {count} connected components")
    #close file
    file.close()



# Driver Code 
if __name__=="__main__": 
    run('n1000.txt')