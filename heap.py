#!/usr/bin/env  python3
# Implementation of min heap and heap sort

def insert(heap, val):
  heap.append(val)
  idx = len(heap)-1
  while idx:
    root_idx = (idx-1)//2  
    if heap[root_idx] > heap[idx]:
      heap[root_idx],heap[idx] = heap[idx],heap[root_idx]
      idx = root_idx
    else: return
  

def remove(heap):
  heap[0],heap[-1] = heap[-1],heap[0]
  min_val = heap.pop()
  heapify(heap, 0, len(heap))
  return min_val


def heapify(unsorted, idx, heaplen):
  largest = idx
  left_child, right_child = 2*idx+1, 2*idx+2
  if left_child < heaplen and unsorted[left_child] < unsorted[largest]:
    largest = left_child
  if right_child < heaplen and unsorted[right_child] < unsorted[largest]:
    largest = right_child
  if largest != idx:
    unsorted[largest], unsorted[idx] = unsorted[idx], unsorted[largest]
    heapify(unsorted, largest, heaplen)
  

def build_heap(unsorted):
  n = len(unsorted)
  for i in range(n//2-1, -1, -1):
    heapify(unsorted, i, n)
  return unsorted

def heap_sort(unsorted):
  build_heap(unsorted)
  for i in range(len(unsorted)-1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)
  return unsorted[::-1]
  
   
  


if __name__ == '__main__':
  unsorted = list(map(int, input().split(',')))
  print(heap_sort(unsorted))

  #  heap = []
  #  for x in unsorted:
  #    insert(heap,x)
  #  print(heap)
  #  while heap:
  #    print("POP {} value".format(remove(heap)))
    
