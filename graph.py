#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:55:26 2017

@author: supperxxxs
"""
import numpy as np

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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, item):
        if self.empty():
            self.front = Node(item)
            self.rear = self.front
        else:
            temp = Node(item)
            self.rear.setNext(temp)
            self.rear = temp
            temp.setNext(None)
            
    def dequeue(self):
        top = self.front
        if top != self.rear:
            temp = top.getData()
            self.front = top.getNext()
            return temp
        else:
            temp= self.front.getData()
            self.front = None
            self.rear = None
            return temp
        return None

    def empty(self):
        return self.front == None
    
    def output(self):
        cur=self.front
        while cur!= None:
            print(cur.getData())
            cur=cur.getNext()
            
class Graph:
    def __init__(self,n):
        self.matrix = np.zeros((n,n))
        
    def addEdge(self,a,b):
        self.matrix[a][b] = 1
        
    def BFS(self,s):
        q = Queue()
        visited = [False]* (len(self.matrix))
        q.enqueue(s)
        visited[s] = True
        while not q.empty():
            tmp=q.dequeue()
            print(tmp)
            for i in range(len(self.matrix)):
                if self.matrix[tmp][i] == 1:
                    if visited[i] == False:
                        q.enqueue(i)
                        visited[i] = True
            
    def DFS(self,t):
        s = Stack()
        visited = [False]* (len(self.matrix))
        s.push(t)
        visited[t] = True
        while not s.empty():
            tmp = s.pop()
            print(tmp)
            for i in tmp.getNeighbour():
                if visited[i] == False:
                    s.push(i)
                    visited[i] = True

    def Route(self,start,end):
        q =Queue()
        visited = [False] * (len(self.matrix))
        q.enqueue(start)
        visited[start] = True
        while not q.empty():
            tmp = q.dequeue()
            if tmp == end:
                return True
            for i in range(len(self.matrix)):
                if self.matrix[tmp][i] == 1:
                    if visited[i]== False:
                        q.enqueue(i)
                        visited[i] = True
        return False
    
    def getNeighbour(self,vertex):
        neighbour =[]
        for i in range(len(self.matrix)):
            if self.matrix[vertex][i] ==1:
                neighbour.append(i)
        return neighbour
    
   
if __name__ == '__main__':
    a= Graph(4)
    a.addEdge(0,1)
    a.addEdge(0,2)
    a.addEdge(1,2)
    a.addEdge(2,0)
    a.addEdge(2,3)
    a.addEdge(3,3)

