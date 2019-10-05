#!/usr/bin/env  python3

# Basic Graph Structure
# Every Vertex contains unique id and set of it's neighbors
# If the weight between two vertices is not given then it will 
# Initialize with None
# Exemple Graph looks like this 
#
# [A] --- [B] --- [C] --- [D]
#          |       |
#           \     / 
#            \   /
#             [E] --- [F]
#
##############################################

class Graph(object):

  class Vertex(object):
    def __init__(self, key):
      self.id = key
      self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
      self.neighbors[neighbor] = weight
    
    def __repr__(self, ):
      return 'ID({}) : Neighbors({})'.format(self.id, self.neighbors)


  def __init__(self, ):
    self.vertices = {}
    self.edges = []

  def __len__(self, ):
    return len(self.vertices)

  def __contains__(self, vertex):
    return vertex in self.vertices

  def __iter__(self, ):
    return iter(self.vertices.values())

  def add_vertex(self, key):
    self.vertices[key] = self.Vertex(key)

  # if vertex is not exist then create vertex first
  def add_edge(self, _from, _to, weight=None):
    if _from not in self.vertices:
      self.add_vertex(_from)
    if _to not in self.vertices:
      self.add_vertex(_to)
    self.vertices[_from].add_neighbor(_to, weight)
    self.vertices[_to].add_neighbor(_from, weight)
    if (_to, _from, weight) not in self.edges:
      self.edges.append((_from, _to, weight))
  
  def get_edges(self, ):
    return self.edges
      
      
if __name__ == '__main__':
  g = Graph()
  g.add_edge('A','B')
  g.add_edge('B','C')
  g.add_edge('B','E')
  g.add_edge('C','D')
  g.add_edge('C','E')
  g.add_edge('E','F')

  for v in g:
    print(v)
