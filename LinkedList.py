#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:07:06 2017

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

class SinLinkedlist:
    def __init__(self):
        self.head = None

    """           #bymyself
    def add(self, item):
        temp = Node(item)
        prev = self.head
        while prev.getNext() != None:
            cur = prev.getNext()
            if cur.getNext() == None:
                cur.setNext(temp)
            prev = prev.getNext()
    """        
    def add(self, item):
        if self.empty():
            self.head = Node(item)
        else:
            temp = Node(item)
            cur = self.head
            while cur.getNext() != None:
                cur=cur.getNext()
            cur.setNext(temp)
            
    def addNode(self, node):
        if self.empty():
            self.head = node
        else:
            cur = self.head
            while cur.getNext() != None:
                cur=cur.getNext()
            cur.setNext(node)
  
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

x = [2,4,5,2,5,6]
if __name__ == '__main__':
    s= SinLinkedlist()
    for i in x:
        s.add(i)
    #s.output()
    """
    #2.1.hashtable
    hashtable=set([])
    prev = s.head
    hashtable.add(prev.getData())
    cur = prev.getNext()
    while cur != None:
        if cur.getData() in hashtable:
            prev.setNext(cur.getNext())
            cur = cur.getNext()
        else:
            hashtable.add(cur.getData())
            cur=cur.getNext()
            prev = prev.getNext()
    s.output()        
    """  
    """
    #2.1.without temporary buffer
    prev = s.head
    cur=prev.getNext()
    while cur != None:
        test =s.head
        while test != cur:
            if test.getData() == cur.getData():
                prev.setNext(cur.getNext())
                cur =cur.getNext()
                break
            test = test.getNext()
        if test == cur:
            cur= cur.getNext()
            prev= prev.getNext()
       # else:
        #    cur =cur.getNext()
         #   prev =prev
    s.output()
    """
    """
    #2.2. nth to the last element
    n = 3
    prev =s.head
    cur = s.head
    for i in range(n):
        prev=prev.getNext()
    while prev != None:
        prev=prev.getNext()
        cur= cur.getNext()
    print(cur.getData())
    """
    #2.3.carryadder
    a =999
    b =999
    x=SinLinkedlist()
    y=SinLinkedlist()
    result=SinLinkedlist()
    for i in range(len(str(a))):
        x.add(a%10)
        a=int(a/10)
    for i in range(len(str(b))):
        y.add(b%10)
        b=int(b/10)
    x_cur= x.head
    y_cur= y.head   
    carry = 0
    while x_cur != None or y_cur != None:        
        if x_cur == None:
            result.add((y_cur.getData()+carry)%10)
            if y_cur.getData()+carry >9:
                carry=1
            else:
                carry=0
            y_cur=y_cur.getNext()
        elif y_cur == None:
            result.add((x_cur.getData()+carry)%10)
            if x_cur.getData()+carry >9:
                carry=1
            else:
                carry=0
            x_cur=x_cur.getNext()
        else:            
            result.add((x_cur.getData()+y_cur.getData()+carry)%10)
            if x_cur.getData()+y_cur.getData()+carry >9:
                carry =1
            else:
                carry =0
            x_cur =x_cur.getNext()
            y_cur =y_cur.getNext()
    if carry ==1:
        result.add(carry)
    result.output()
 #2.5.create circular linked list   
    t=SinLinkedlist()
    A=Node('A')
    t.addNode(A)
    B=Node('B')
    t.addNode(B)
    C=Node('C')
    t.addNode(C)
    D=Node('D')
    t.addNode(D)
    E=Node('E')
    t.addNode(E)
    E.setNext(C)
# function1
    ht =set([])
    cur = t.head
    while cur.getData() not in ht:
        ht.add(cur.getData())
        cur = cur.getNext()
    if cur.getData() in ht:
        print(cur.getData())
#function2    
    turtle = t.head.getNext()
    rabbit = t.head.getNext().getNext()
    while turtle.getData() != rabbit.getData():
        turtle = turtle.getNext()
        rabbit = rabbit.getNext().getNext()
    pig = t.head
    while pig.getData() != turtle.getData():
        pig = pig.getNext()
        turtle= turtle.getNext()
    print(pig.getData())
        
    