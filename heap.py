#!/usr/bin/env  python3
from random import randint
from time import time, sleep
import heapq

# Implementation of min heap
# Didn't care about performance much

class MinHeap(object):
  def __init__(self, random_list=None):
    if random_list is None or not random_list:
      self.heap = [0]
    else:
      self.heap = [0] + random_list
      self.build_heap(1)

  def __repr__(self, ):
    return repr(self.heap[1:])
    
  def insert(self, val):
    # Heap is always already heapified
    self.heap.append(val)
    idx = len(self.heap)-1
    while idx is not 1:
      root_idx = idx // 2
      if self.heap[root_idx] > self.heap[idx]:
        self.heap[root_idx],self.heap[idx] = self.heap[idx],self.heap[root_idx]
        idx = root_idx
      else:
        return


  def remove(self, ):
    if len(self.heap)-1 == 0:
      print('Heap is Empty! You should insert first!')
      return

    self.heap[1],self.heap[-1] = self.heap[-1], self.heap[1]
    min_val = self.heap.pop()

    root = 1
    while root is not None:
      root = self.heapify(root)
    
    return min_val


        
  def heapify(self, root):
    left_child,right_child = root*2,root*2+1
    heaplen = len(self.heap) - 1

    if heaplen > left_child:
      if self.heap[left_child] < self.heap[root]:
        if self.heap[left_child] < self.heap[right_child]:
          self.heap[left_child],self.heap[root] = self.heap[root],self.heap[left_child] 
          return left_child
        else:
          self.heap[right_child],self.heap[root] = self.heap[root],self.heap[right_child] 
          return right_child
      elif self.heap[right_child] < self.heap[root]:
        self.heap[right_child],self.heap[root] = self.heap[root],self.heap[right_child] 
        return right_child
    elif heaplen  == left_child:
      if self.heap[left_child] < self.heap[root]:
        self.heap[left_child],self.heap[root] = self.heap[root],self.heap[left_child] 
        return left_child
    

  def build_heap(self, root):
    # Postorder traversal 
    left_child,right_child = 2*root,2*root+1
    heaplen = len(self.heap) - 1

    if heaplen >= left_child:
      self.build_heap(left_child)
    else:
      self.heapify(root) 
      return
    if heaplen >= right_child:  
      self.build_heap(right_child)

    while root is not None:
      root = self.heapify(root) 

  
  def heap_sort(self, ):
    # Heap sorted by descending order
    heapcp = self.heap
    heaplen = len(self.heap) - 1
    if heaplen == 0:
      print('Heap Is Empty')
      return
    
    sorted_heap = [self.remove() for _ in range(heaplen)]
    self.heap = heapcp
    return sorted_heap 
      


if __name__== '__main__':
  # return value will be different depends on input parameter
  # parameter can be stay empty or unsorted list
  h = MinHeap()

  val = [7,30,100] 

  print("=============================")
  print("Heap Insert Test\n\n\n\n")
  for _ in range(val[1]):
    h.insert(randint(0,100))
    print(h)

  print("=============================")
  print("Heap Remove Test\n\n\n\n")
  for _ in range(val[1]):
    h.remove()
    print(h)

  print("==============================")
  print("Build Heap Test\n\n\n\n")
  print("Building Heap Test Between My Function and heapq Library!")
  randlist = [randint(0,20) for _ in range(val[2])]
  print("Sample List : {}".format(randlist))

  
  h = MinHeap(randlist)
  print("\n\n\n My Function Output : ", end='')
  print(h)


  heapq.heapify(randlist)
  print("\n\n\n heapq Library Function Output : {}\n".format(randlist))

  print('Is The Output Same? : {}\n\n'.format(str(h) == str(randlist)))

  print("=============================")
  print("Heap Sort Test\n\n\n\n")
  randlist = [randint(0,100) for _ in range(val[2])]
  print("Random List : {}\n\n".format(randlist))
  h = MinHeap(randlist)
  print("Sorted Heap : {}\n\n".format(h.heap_sort()))

    
