#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:47:40 2017

@author: supperxxxs
"""
import copy

class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

class SinLinkedlist:
    def __init__(self):
        self.head = None
   
    def add(self, item):
        if self.empty():
            self.head = Node(item)
        else:
            temp = Node(item)
            cur = self.head
            while cur.getNext() != None:
                cur=cur.getNext()
            cur.setNext(temp)
  
    def remove(self,item):
        prev =self.head
        while prev.getNext() != None:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()

    def search(self, item):
        cur = self.head.getNext()
        while cur != None:
            if cur.getData() == item:
                return True
            cur = cur.getNext()

        return False

    def empty(self):
        return self.head == None
    
    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != None:
            count += 1
            cur = cur.getNext()

        return count
    def output(self):
        cur=self.head
        while cur!= None:
            print(cur.getData())
            cur=cur.getNext()
            
class TreeNode:
    def __init__(self,initdata):
        self.__data = initdata
        self.__left = None
        self.__right = None
        self.__parent = None
    
    def getData(self):
        return self.__data
    
    def setData(self,newdata):
        self.__data = newdata
        
    def getLeft(self):
        return self.__left
    
    def setLeft(self,newleft):
        self.__left = newleft
        newleft.__parent = self
        
    def getRight(self):
        return self.__right
    
    def setRight(self,newright):
        self.__right = newright
        newright.__parent = self
        
    def hasLeft(self):
        return self.__left != None
    
    def hasRight(self):
        return self.__right != None
    
    def getParent(self):
        return self.__parent
    
    def isLeft(self):
        if self.__parent==None:
            return False
        else:
            return self.__parent.__left==self
    
    def isRight(self):
        if self.__parent==None:
            return False
        else:
            return self.__parent.__right==self
        
def BinarySearchTree(List):
    if len(List)== 0:
        return None
    else:
        mid = int(len(List)/2)
        root =TreeNode(List[mid])
        root.setLeft(BinarySearchTree(List[:mid]))
        root.setRight(BinarySearchTree(List[mid+1:]))
        return root  

def StoreEachLevel(root):
    total=SinLinkedlist()
    level=SinLinkedlist()
    level.add(root)
    total.add(level)
    while not level.empty():
        pre=level
        level = SinLinkedlist()
        cur = pre.head
        while cur != None:
            if cur.getData().hasLeft():
                level.add(cur.getData().getLeft())
            if cur.getData().hasRight():
                level.add(cur.getData().getRight())
            cur= cur.getNext()
        total.add(level)
    return total
            
        
    
def inorder(node):
    if node.hasLeft():
        inorder(node.getLeft())
    print(node.getData())
    if node.hasRight():
        inorder(node.getRight())
        
def preorder(node):
    print(node.getData())
    if node.hasLeft():
        preorder(node.getLeft())
    if node.hasRight():
        preorder(node.getRight())        

def postorder(node):
    if node.hasLeft():
        postorder(node.getLeft())
    if node.hasRight():
        postorder(node.getRight())  
    print(node.getData())       

def MaxDepth(node):
    if node == None:
        return 0 
    else:
        return 1+max(MaxDepth(node.getLeft()),MaxDepth(node.getRight()))

def MinDepth(node):
    if node == None:
        return 0
    else:
        return 1+min(MinDepth(node.getLeft()),MinDepth(node.getRight()))
    
    
def ifBalanced(node):
    return MaxDepth(node)-MinDepth(node)<= 1 

def FindNextNode(treenode):
    if treenode.hasRight():
        tmp = treenode.getRight()
        while tmp.hasLeft():
            tmp = tmp.getLeft()  
        return tmp.getData()
    elif treenode.isLeft():
        return treenode.getParent().getData()
    elif treenode.isRight():
        tmp = treenode
        while tmp.isRight():
            tmp = tmp.getParent()
        if tmp.getParent():
            return tmp.getParent().getData()
        else:
            return None
    
"""    
def FindNextNode(treenode):
    if treenode.hasRight():
        tmp = treenode.getRight()
        while tmp.hasLeft():
            tmp = tmp.getLeft()  
        return tmp.getData()
    else:
        tmp=treenode.getParent()
        while tmp.isRight():
            tmp = tmp.getParent()
        if tmp.getParent():
            return tmp.getParent().getData()
        else:
            return None
           
"""
def inAtree(a,root):
    if root==None:
        return False
    if a!= root:
        return inAtree(a,root.getLeft()) or inAtree(a,root.getRight())
    else:
        return True

def CommonAncestor(a,b,root):    
    if inAtree(a,root.getLeft()) == inAtree(b,root.getRight()):
        return root.getData()
    else:
        if inAtree(a,root.getLeft()):
            return CommonAncestor(a,b,root.getLeft())
        else:
            return CommonAncestor(a,b,root.getRight())
            
def containsTrees(a,b):
    if b == None:
        return True
    else :
        return subTree(a,b)

def subTree(a,b):
    if a == None:
        return False
    if a.getData() == b.getData():
       if matchTree(a,b):
           return True
    return subTree(a.getLeft(),b) or subTree(a.getRight(),b)

def matchTree(a,b):
    if a == None and b == None:
        return True
    if a == None or b== None:
        return False
    if a.getData() != b.getData():
        return False
    return matchTree(a.getLeft(),b.getLeft()) and matchTree(a.getRight(),b.getRight())

def findSum(root, summation,List,level):
    if root == None:
        return None
    tmp = summation
    List.append(root.getData())
    for i in range(level+1):
        tmp -= List[level-i]
        if tmp == 0:
            print(List[level -i:level+1])
    c1 = copy.deepcopy(List)
    c2 = copy.deepcopy(List)
    findSum(root.getLeft(),summation,c1,level+1)
    findSum(root.getRight(),summation,c2,level+1)
        
      
if __name__ == '__main__':
    a=TreeNode(1)
    b=TreeNode(2)
    c=TreeNode(3)
    d=TreeNode(4)
    e=TreeNode(5)
    f=TreeNode(6)
    g=TreeNode(7)
    h=TreeNode(8)
    a.setLeft(b)
    a.setRight(c)
    b.setLeft(d)
    b.setRight(e)
    c.setLeft(f)
    c.setRight(g)
    e.setRight(h)
    
    i = TreeNode(2)
    j = TreeNode(4)
    k = TreeNode(5)
    i.setLeft(j)
    i.setRight(k)
   # inorder(a)
   # print('\n')
   # preorder(a)
   # print('\n')
   # postorder(a)
    s= [1,2,3,4,5,6,7,8]
    """ 
    level=StoreEachLevel(BinarySearchTree(s)).head.getNext().getData()
    cur=level.head
    while cur!=None:
        print(cur.getData().getData())
        cur=cur.getNext()
    """