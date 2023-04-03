# -*- coding: utf-8 -*-
"""
Initial Code Created on Thu Oct 15 12:32:31 2020

"Array" implementation of heap using built-in lists

@author: jerem
"""

class BinHeap:
    def __init__(self, n):
        self.heapList = [0]
        self.currentSize = 0
        self.num_branch = n

    def percUp(self,i):
        while i // self.num_branch > 0:
          parent_ind = (i+(self.num_branch-2)) // self.num_branch  # Find the index of the parent of the node whose index is i
          if self.heapList[i] < self.heapList[parent_ind]:  # Swap the values of node i and its parent, if the value of its parent is larger
             tmp = self.heapList[parent_ind]
             self.heapList[parent_ind] = self.heapList[i]
             self.heapList[i] = tmp
          i = parent_ind  # Parent node becomes the new compared node

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)
      # print(self.heapList)

    def percDown(self,i):
      while (i*self.num_branch-(self.num_branch-2)) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      """ Find the minimum value among all child nodes of the node whose index is i that is specified in the parameter."""
      # (i*self.num_branch+1) is the index of rightmost child node of the node i for n-ary heap whatever n is
      if i*self.num_branch+1 <= self.currentSize:      # If i*self.num_branch+1 <= self.currentSize, it means node i has all n child nodes.
         # Calculate how many children the node i has
         numChild = self.num_branch                    # Thus, the number of child nodes is exactly the number of branch.
         # Find the minimum index among the children
         minIndex = (i*self.num_branch+1)-(self.num_branch-1)
         # Find the maximum index among all children
         maxIndex = i*self.num_branch+1
      else:                                            # If i*self.num_branch+1 > self.currentSize, it means node i has less than n child nodes.
         # Calculate how many children the node i has
         numChild = self.num_branch-((i*self.num_branch+1)-self.currentSize)  # ((i*self.num_branch+1)-self.currentSize) represents the difference between the number of existing child nodes and all nodes
         # Find the minimum index among the children
         minIndex = self.currentSize-(numChild-1)  
         # Find the maximum index among all children
         maxIndex = self.currentSize  

      minVal = self.heapList[minIndex]  # Record the minimum value among all children
      minVal_ind = minIndex  # Record the index of the minimum value among all children
      for ind in range(minIndex+1, maxIndex+1):
         if self.heapList[ind]<minVal:
            minVal=self.heapList[ind]
            minVal_ind=ind
      return minVal_ind
            
    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = (len(alist)+(self.num_branch-2)) // self.num_branch  # Find the index of the last node's parent
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
      #print(self.heapList)

    def __str__(self):
      return self.toString(1)
         
    def toString(self, i):
      sss = '[' + str(self.heapList[i])
      for childIndex in range(i*self.num_branch-(self.num_branch-2), i*self.num_branch+2):
        if childIndex <= self.currentSize:
          sss += self.toString(childIndex)
      sss += ']'
      return sss

       


bh = BinHeap(4)
bh.buildHeap([9,5,6,2,3,1,4,4,2])    # [0, 1, 2, 6, 2, 3, 5, 4, 4, 9]
bh.insert(1)   # [0, 1, 2, 1, 2, 3, 5, 4, 4, 9, 6]
print(bh)      # [1[2[5][4][4][9]][1[6]][2][3]]


print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())



"""
For a n-ary heap, with k nodes the maximum height of the given heap will be logn(k). 

- percUp() run for maximum of logn(k) times (as at every iteration the node is shifted one level up is case of percUp() 
  or one level down in case of percDown).
- percDown() calls itself recursively for n children. So time complexity of this functions is O(n logn(k)).
- insert() call percUp() once. So complexity is O(logn(k)).

Time complexity of build heap is O(n)

"""