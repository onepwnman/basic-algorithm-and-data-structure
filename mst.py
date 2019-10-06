#!/usr/bin/env  python3
'''
A minimum spanning tree (MST) or minimum weight spanning tree is a subset of 
the edges of a connected, edge-weighted undirected graph that connects all 
the vertices together, without any cycles and with the minimum possible total
edge weight. That is, it is a spanning tree whose sum of edge weights is as 
small as possible.

If there are n vertices in the graph, then each spanning tree has n − 1 edges.
MST is one of greedy algorithm which means it can be made of choosing best node
of current state. 
There is two algoritm's in MST which called Kruskal algorithm and Prim algoritm
If graph has a lots of edges, you can pick Prim algoritm otherwise Kruskal
algoritm is more efficient
'''

from graph import Graph
from heapq import heappush, heappop
from union_find import UnionFind

def mst_prim(graph, start):
  '''Using Heap data structure to select edges'''

  total_cost,mst = 0,[] 
  discovered,explored = [(0,start,start)],set()
  # Started from start position
  while discovered:
    # Looping over the while loop and if you find out not discovered vertices from 
    # current vertex then push it to the heap and pop next vertex until every vertices 
    # are discovered
    cost,_from,_to = heappop(discovered)
    if _to not in explored:
      explored.add(_to)
      total_cost += cost
      mst.append((_from,_to))
      for neighbor in set(graph.vertices[_to].neighbors) - explored:
        heappush(discovered, (graph.vertices[_to].neighbors[neighbor],_to,neighbor))

  return total_cost, mst[1:] 
    

def mst_kruskal(graph):
  '''Using Disjoint-set data structure to select edges'''

  total_cost, mst = 0, []
  u = UnionFind()

  # Sorted by weight
  edges = sorted(graph.get_edges(), key=lambda x: x[2])

  for start, end, weight in edges:
    # If start vertex and end vertex has different parent on union-find structure
    # then joining the two subset
    if u[start] != u[end]:
      u.union(u[start],u[end])
      total_cost += weight
      mst.append((start,end))

  return total_cost, mst
        


if __name__ == '__main__':
  print('''MST : Prim algorithm and kruskal algorithm Exemple graph looks like this\n
  [EX]
                  [A]
              3 /  |  \\ 10
               /   |7  \\ 
             [B]--[C]--[D]
             /  2 /|  6 |
           5/    /4|10  |
           /    [E]|    |
          /     2\\ |    /9 
        [G]-------[F]--/
              4

        ''')
  g = Graph()
  g.add_edge('A','B',3)
  g.add_edge('A','C',7)
  g.add_edge('A','D',10)
  g.add_edge('B','C',2)
  g.add_edge('B','G',5)
  g.add_edge('C','D',6)
  g.add_edge('C','E',4)
  g.add_edge('C','F',10)
  g.add_edge('D','F',9)
  g.add_edge('E','F',2)
  g.add_edge('G','F',4)

  for v in g:
    print(v)
    
  print('\nPrim ==> total count : {} , edges : {}'.format(*mst_prim(g,'A')))
  print('\nKruskal ==> total count : {} , edges : {}'.format(*mst_kruskal(g)))
