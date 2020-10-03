import numpy as np
from matplotlib import pyplot as plt 
#file to calculate the distribution of degrees for nodes in a graph
class Graph():
  def __init__(self,nodes):
    self.nodes = nodes
    #use set to handle duplicate cases
    self.storage = [set() for i in range(self.nodes)]
  
  #add edge to storage
  def add(self,x,y):
    self.storage[x].add(y)
    self.storage[y].add(x)

  def distribution(self):
    return [len(i) for i in self.storage]


def run(filename):
  #initialize new graph
  file = open(filename,'r')
  nodes = int(file.readline())
  graph = Graph(nodes)

  #add all edges
  for i in file:
    x,y = int(i.split(' ')[0]),int(i.split(' ')[1])
    graph.add(x,y)
  #close file
  file.close()

  #print out degree distribution list
  distribution = (graph.distribution())
  #histogram
  plt.style.use('fivethirtyeight')
  plt.hist(distribution, edgecolor='black')
  plt.title('Node Degrees Distribution')
  plt.xlabel('Degrees')
  plt.ylabel('Total Occurences')
  plt.tight_layout()
  plt.show()

if __name__ =='__main__':
  run('n10000.txt')