# Class defining a Node (optional parameter to enable doubly linked list)
# Future implementations will use singly linked list
# Author: Anurag Sen
# Date Updated: 03SEP2019

class Node():
  # Constructor with node value and next node reference
  def __init__(self, val, next_node=None, previous_node=None):
      self.value = val
      self.next = next_node
      self.prev = previous_node

  # Accessor Methods for value and next node reference
  def get_value(self):
      return(self.value)

  def get_next(self):
      return(self.next)

  def get_prev(self):
      return(self.prev)

  # Setting Methods for value and next node reference
  def set_value(self, val):
      self.value = val

  def set_next(self, next_node):
      self.next = next_node

  def set_prev(self, previous_node):
      self.prev = previous_node
