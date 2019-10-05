#!/usr/bin/env  python3

class UnionFind(object):
  def __init__(self, ):
    self.parent,self.rank = {},{}

  def __repr__(self, ):
    return str(self.parent)
    
  def __getitem__(self, x):
    return self.find(x)

  def find(self, x):
    try:
      if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])
    except KeyError:
      self.parent[x],self.rank[x] = x,0
    finally:
      return self.parent[x]
  
  def union(self, x, y):
    x,y = self.find(x),self.find(y)
    if x == y:  return 
    if self.rank[x] > self.rank[y]:  self.parent[y] = x
    else:  self.parent[x] = y
    if self.rank[x] == self.rank[y]:  self.rank[y] += 1

  def get_parent(self, ):
    return self.parent
    

if __name__ == '__main__':
  u = UnionFind()
  u.union(u['A'],u['B'])
  u.union(u['B'],u['C'])
  u.union(u['D'],u['A'])
  u.union(u['F'],u['V'])
  u.union(u['E'],u['A'])
  u.union(u['G'],u['H'])
  u.union(u['Z'],u['N'])
  u.union(u['J'],u['N'])
  u.union(u['E'],u['M'])
  print(u)






