#!/usr/bin/env  python3
from random import sample

# Basic implementation of Binary Search Tree 
# all method's are made up with recursive function call for quick implementation

# Binary Search Tree has few conditions 
# First : BST is a binary tree so it has at most 2 child per each node
# Second : Every value in node must be unique
# Third : Every left child's value will be lower the it's parent and right will be higher
# Fourth: Left and Right subtree should be a BST

# Represent Binary Search Tree
class BST(object):
  def __init__(self, ):
    self.root = None    

  # Add node to BST
  def add_node(self, node, current_top=None):
    # if add node method would not called by itself, start node is the root node
    if current_top is None:
      current_top = self.root
    
    # if there is nothing
    if self.root is None:
      self.root = node
    else: 
      # go right
      if node.data > current_top.data:
        # if there is no child then add node
        if current_top.right is None:
          node.parent = current_top
          current_top.right = node
          return current_top
        # if there is child exist then recursively repeat from right child node
        else:
          self.add_node(node, current_top.right)
      # go left
      else:
        # if there is no child then add node
        if current_top.left is None:
          node.parent = current_top
          current_top.left = node
          return current_top
        # if there is child exist then recursively repeat from left child node
        else:
          self.add_node(node, current_top.left)
        
  # Find the data in the BST
  def search_data(self, data, current_node=None):
    # if search data method would called by itself, it'll search from the root node
    if current_node is None:
      current_node = self.root
      # if BST hasn't got any node
      if self.root is None:
        return False

    # Searching down through tree 
    # if value is smaller then the current node value, go left child
    # if value is larger then the current node value, go right child
    if current_node.data > data:
      if current_node.left is not None:
        return self.search_data(data, current_node.left)
    elif current_node.data < data:
      if current_node.right is not None:
        return self.search_data(data, current_node.right)
    else:
      return current_node

    return False    

  
  # Remove node from the BST
  def remove_node(self, data):
    # Find the node to delete in the BST    
    node = self.search_data(data)  
    # Node should be exist
    if not node:
      return False

    # When selected node hasn't got any child
    if node.left is None and node.right is None:
      # if selected node is root node
      if node is self.root:
        self.root = None
      # Current node is attached to which side of it's parent node? 
      elif node.parent.data > node.data:
        node.parent.left = None
      else:
        node.parent.right = None

    # When selected node has two childs
    elif node.left is not None and node.right is not None:
      # Current Node will be deleted so it need's replacement for the empty place
      # The replacement could be biggest value from the left side of subtree
      # Or smallest value from the right side of subtree
      # In this implementation i'll pick the later one
      right_min_node = self._find_min_from_rightpart(node.right)

      # if node is root
      if node is self.root:
        self.root = right_min_node
      else:
      # if node is not root
        if node.parent.data > node.data:
          node.parent.left = right_min_node
        else:
          node.parent.right = right_min_node

      # Putting the replacement node to the empty place
      right_min_node.parent = node.parent
      if node.left is not None:
        node.left.parent = right_min_node
      if node.right is not None:
        node.right.parent = right_min_node
        
      right_min_node.left, right_min_node.right = node.left, node.right

    # When selected node has one child
    else:
      # The child is attached to which side of current node?
      if node.left is not None: child = node.left
      else: child = node.right
      
      # if current node is root 
      if node is self.root:
        self.root = child
      # of current node is not root
      elif node.parent.data > node.data:
        node.parent.left = child
      else:
        node.parent.right = child
      child.parent = node.parent
    return node
        

  # Find the minimum value from the right subtree of the current node
  def _find_min_from_rightpart(self, node):
    # Finding down through the BST until there is no left node
    # And remove that node and return it
    if node.left is not None:
      return self._find_min_from_rightpart(node.left)
    return self.remove_node(node.data)
    

  # Print BST
  # Printing order is followed by inorder traversal which is traverse by 
  # (Left child --> Current Node --> Right child) order
  def print_node(self, node=None):
    if node is None:
      node = self.root

    if node.left is not None:
      self.print_node(node.left)
    print("Data: {}, Parent: {}".format(node.data, 
        node.parent.data if node.parent is not None else None))
    if node.right is not None:
      self.print_node(node.right)


# Represent each node
class Node(object):
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    self.parent = None


if __name__== '__main__':
  print("Build BST")
  bst = BST()
  for data in sample(range(10), 10):
    bst.add_node(Node(data))
  
  while bst.root is not None:
    bst.print_node()
    n = int(input("Enter data to delete in the BST: "))
    bst.remove_node(n)
   



