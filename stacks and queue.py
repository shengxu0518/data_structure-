#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 01:19:10 2017

@author: supperxxxs
"""

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

class Stack:
    def __init__(self):
        self.head = None
    
    def pop(self):
        top = self.head
        if top != None:
            temp =top.getData()
            self.head = top.getNext()
            return temp
        return None
    
    def push(self,item):
        if self.empty():
            self.head = Node(item)
        else:
            top = self.head
            temp = Node(item)
            temp.setNext(top)
            self.head = temp
        
    def empty(self):
        return self.head == None
    
    def peek(self):
        return self.head.getData()
    
    
    def output(self):
        cur=self.head
        while cur!= None:
            print(cur.getData())
            cur=cur.getNext()
        
#3.5:two stacks to form a queue
class myQueue:
    def __init__(self):
        self.a= Stack()
        self.b= Stack()
    
    def enqueue(self,item):
        self.a.push(item)
    
    def dequeue(self):
        if self.b.empty():
            temp =self.a.pop()
            while temp != None:
                self.b.push(temp)
                temp= self.a.pop()
        return self.b.pop()
        #while not self.a.empty()
        #   b.push(a.pop())   
#3.6 sort the stack
s = [2,5,8,2,6,1,1,3,4,7]
def xLessThan(st,i):
    if st.empty():
        return True
    else:
        return st.peek()<= i
def yGreatThan(st,i):
    if st.empty():
        return True
    else:
        return st.peek()>= i
def sortStack(s):
    x = Stack()
    y = Stack()
    for i in s:
        while True:
            if xLessThan(x,i) and yGreatThan(y,i):
                   x.push(i)
                   break
            elif not xLessThan(x,i):
                y.push(x.pop())
            elif not yGreatThan(y,i):
                x.push(y.pop())
            
    while not y.empty():
        x.push(y.pop())
    return x 
#3.4. HonaiTower 
def HonaiTower(n,source,destination,media):
    if n==1:
        destination.push(source.pop())
    else:
        HonaiTower(n-1, source,media,destination)
        destination.push(source.pop())
        HonaiTower(n-1,media,destination,source)  
if __name__ == '__main__':
    a= sortStack(s)
    a.output()
    
    A = Stack()
    B = Stack()
    C = Stack()
    n = 6
    s = [n-i for i in range(n)]
    for i in s:
        A.push(i)
    HonaiTower(n,A,C,B)
