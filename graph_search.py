#!/usr/bin/env  python3
from graph import Graph

# GraphSearch class contains Depth-First Search, Breadth-First Search, Dijkstra Algorithm
class GraphSearch(object):
  def __init__(self, graph):
    self.graph = graph

  # Depth-First Search with stack
  # In python you can use set object to make code shorter
  def dfs_stack(self, start):
    stack, visited = [start], set()
    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        visited.add(vertex)
        for neighbor in set(self.graph.vertices[vertex].neighbors) - visited:
          stack.append(neighbor)
    return visited
  
  # Depth-First Search with implement with recursion
  def dfs_recursive(self, start, visited=None):
    if visited == None:
      visited = set()
    visited.add(start)

    for neighbor in set(self.graph.vertices[start].neighbors) - visited:
      self.dfs_recursive(neighbor, visited)
    return visited

  # Generate path from start to end with Depth-First Search
  def dfs_path_generator(self, start, end):
    stack = [(start, [start])]       
    while stack:
      vertex, path = stack.pop()
      for neighbor in set(self.graph.vertices[vertex].neighbors) - set(path):
        if neighbor == end:
          yield path + [neighbor]
        else:
          stack.append((neighbor, path + [neighbor]))
        
  # Get every path from start to end with DFS recursion
  def dfs_path_recursive(self, start, end, path=None, visited=None):
    if visited == None and path== None:
      visited, path = [], []
    visited.append(start)
    if start == end:
      # Appended list should be a copy of visitied list
      path.append(visited[:])
      return 
    for neighbor in self.graph.vertices[start].neighbors:
      if neighbor not in visited:
        self.dfs_path_recursive(neighbor,end,path,visited)
        visited.pop()
    return path
    
  # Breadth-First Search with queue
  def bfs_queue(self, start):
    queue, visited = [start], set()
    while queue:
      vertex = queue.pop(0) 
      if vertex not in visited:
        visited.add(vertex)
        queue.extend(set(self.graph.vertices[vertex].neighbors) - visited)
    return visited

  # Generate path from start to end with Breadth-First Search
  def bfs_path_generator(self, start, end): 
    queue = [(start, [start])]
    while queue:
      vertex, path = queue.pop(0)
      for neighbor in set(self.graph.vertices[vertex].neighbors) - set(path):
        if neighbor == end:
          yield path + [neighbor]
        else:
          queue.append((neighbor, path + [neighbor]))





if __name__ == '__main__':
  print('''########## Graph Depth-First Search and Breadth-Frist Search Test ###########
              Exemple Graph looks like this\n
                           [A] --- [B] --- [C] --- [D]
                                    |       |
                                     \     /
                                      \   /
                                       [E] --- [F]
      ''')

  g = Graph()
  g.add_edge('A','B')
  g.add_edge('B','C')
  g.add_edge('B','E')
  g.add_edge('C','D')
  g.add_edge('C','E')
  g.add_edge('E','F')

  for v in g:
    print(v)

  gs = GraphSearch(g)

  print('\n Finding path with DFS')
  for i,path in enumerate(gs.dfs_path_generator('A','D')):
    print("Path number: {},  Path : {}".format(i+1, path))

  print('\n Finding path with BFS')
  for i,path in enumerate(gs.bfs_path_generator('A','D')):
    print("Path number: {},  Path : {}".format(i+1, path))




