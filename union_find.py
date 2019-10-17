#!/usr/bin/env  python3
'''
Disjoint-set data structure (also called a union–find data structure or
merge–find set) is a data structure that tracks a set of elements partitioned
into a number of disjoint (non-overlapping) subsets.
'''

class UnionFind(object):
  '''Implemented by tree'''
  def __init__(self, ):
    self.parent,self.rank = {},{}


  def __repr__(self, ):
    '''To make easy to show how set's are connected'''
    sets = {}
    for key in self.parent:
      parent = self[key]
      if parent not in sets: sets[parent] = [key]
      else: sets[parent].append(key)
    return 'Disjoint-set: ' + str(sets)


  def get_parent(self, ):
    return self.parent
    

  def __getitem__(self, x):
    return self.find(x)


  def find(self, x):
    '''
    Path compression flattens the structure of the tree by making every node
    point to the root whenever Find is used on it.  This is valid, since each
    element visited on the way to a root is part of the same set.
    The resulting flatter tree speeds up future operations not only on these
    elements, But also on those referencing them. 
    '''
    try:
      if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])
    except KeyError:
      self.parent[x],self.rank[x] = x,0
    finally:
      return self.parent[x]
  

  def union(self, x, y):
    '''
    Union(x,y) uses Find to determine the roots of the trees x and y belong to. 
    If the roots are distinct, the trees are combined by attaching the root of 
    one to the root of the other.  If this is done naively, such as by always 
    making x a child of y, the height of the trees can grow as O(n).  
    To prevent this union by rank is used.
    '''
    x,y = self[x],self[y]
    if x != y:
      if self.rank[x] < self.rank[y]:  self.parent[x] = y
      else:  self.parent[y] = x
      if self.rank[x] == self.rank[y]:  self.rank[y] += 1

    
if __name__ == '__main__':
  u = UnionFind()
  u.union(u['0'],u['1'])
  print(u)
  u.union(u['3'],u['4'])
  print(u)
  u.union(u['5'],u['6'])
  print(u)
  u.union(u['1'],u['2'])
  print(u)
  u.union(u['3'],u['6'])
  print(u)
  u.union(u['0'],u['6'])
  print(u)






