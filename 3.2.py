#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:39:00 2017

@author: supperxxxs
"""

class Node:
    def __init__(self, initdata,minimum):
        self.__data = initdata
        self.__next = None
        self.__mini = minimum
    
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext
    
    def getMini(self):
        return self.__mini

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
            self.head= Node(item,item)
        else:
            prev = self.head
            if item < prev.getMini():
                cur = Node(item,item)
            else:
                cur = Node(item,prev.getMini())
            cur.setNext(prev)
            self.head = cur
    
    def empty(self):
        return self.head == None
    
    def output(self):
        cur=self.head
        while cur!= None:
            print(cur.getData())
            cur=cur.getNext()
    
    def Min(self):
        return self.head.getMini()    

x = [5,4,3,2,1]
if __name__ == '__main__':
    s= Stack()
    for i in x:
        s.push(i)
    print(s.Min())