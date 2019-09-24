#!/usr/bin/env  python3
from graph import Graph
from heapq import heappush, heappop

# MST는 greedy 알고리즘이다.

# 조건: 가중치를 가지는 무방향 그래프여야한다.
#  모든노드들이 연결된다.
#  가중치합이 최소가 된다.
# n 개의 vertex에 n-1개의 edge를 가진다.
# 간선의 개수가 작은경우 크루스칼알고리즘 많은경우 프림알고리즘
# Kruskal알고리즘과 Prim알고리즘이 있다.

# Sample Graph


#  Disjoint-set which is called Union-Find
# 서로 중복되지 않는 부분 집합들 로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
# tree로 구현하는게 가장 효율적
class UnionFind(object):
	def __init__(self, i):
		self.parent = [x for x in range(

			
	def union(self, ):
	

	def find(self, ):
	
	

class MST(object):
  
  def __init__(self, graph):
    self.graph = graph

  def prim(self, start):
    total_cost,mst = 0,[] 
    discovered,explored = [(0,start,start)],set()
    while discovered:
      cost,_from,_to = heappop(discovered)
      if _to not in explored:
        explored.add(_to)
        total_cost += cost
        mst.append((_from,_to))
        for v in set(self.graph.vertices[_to].neighbors) - explored:
          heappush(discovered, (self.graph.vertices[_to].neighbors[v],_to,v) )

    return total_cost, mst[1:] 
      
		
    def kruskal(self, ):

    

     
    
    





if __name__ == '__main__':
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
    
  mst = MST(g) 
  print('total count : {} , edges : {}'.format(*mst.prim('A')))

