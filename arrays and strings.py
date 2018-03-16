#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:58:53 2017

@author: supperxxxs
"""

import numpy as np
import math 
x= 'asgrsd'
y= 'rsd'
n=4

def isunique(x):
    status=[0 for i in range(2**8)]
    for i in range(len(x)):
        if status[ord(x[i])] == 0:
            status[ord(x[i])] = 1
        else:
            return False
    return True
        
def unique(x):
    for i in range(len(x)):
        for j in range(i):
            if x[j] == x[i]:
                return False 
    return True
   
def reverse(x): #c style string
    rev = []
    for i in range(len(x)):
        rev.append(x[len(x)-i-2])
    x_rev= "".join(rev)
    return x_rev

def remove_duplicate(x):
    x_list= list(x)
    s =[]
    for i in range(len(x_list)):
        flag=0
        for j in range(i):
            if x_list[j] == x_list[i]:
                flag=1
                break
        if flag==0:
            s.append(x[i])           
    x_remove="".join(s)
    return x_remove

def remove(x):
    x_list = list(x)
    tail =1
    for i in range(1,len(x_list)):
        j=0
        while j<tail:
            if x_list[j] == x_list[i]:
                break
            j+=1
        if j == tail:
            x_list[tail]= x_list[i]
            tail += 1
    x_list= x_list[0:tail]
    return "".join(x_list)

def anagram(x,y):
   # return sorted(x) == sorted(y)
   status = [0 for i in range(2**8)]
   if len(x) != len(y):
       return False
   for i in range(len(x)):
       status[ord(x[i])] += 1
   for i in range(len(y)):
       if status[ord(y[i])] == 0:
           return False
       else:
           status[ord(y[i])] -= 1
   return True

def replace(x):
    x_replace = list(x)
    count = 0
    for i in range(len(x_replace)):
        if x_replace[i] == ' ':
            count +=1
    for i in range(len(x_replace)+count*2):
        if x_replace[i] ==' ':
             x_replace[i] ='%'
             x_replace.insert(i+1,'2')
             x_replace.insert(i+2,'0')
    return "".join(x_replace)

def rotate(n):
    s= np.array([[chr(i+n*j+97) for i in range(n)]for j in range(n)])
    matrix= np.array([['' for i in range(n)]for j in range(n)])
    for i in range(n):
        matrix[:,n-1-i]=s[i,:]
    return matrix

def rotated(n):
    s= [[chr(i+n*j+97)for i in range(n)] for j in range(n)]
    for layer in range(math.ceil(n/2)):
        for i in range(layer,n-1-layer):
            temp = s[i][n-1-layer]
            s[i][n-1-layer] = s[layer][i]
            s[layer][i] = s[n-1-i][layer]
            s[n-1-i][layer] =s[n-1-layer][n-1-i]
            s[n-1-layer][n-1-i] =temp
    return s

s = np.array([[1,3,4],[3,0,5],[2,6,0]])
def ToBeZero(s):
    row=[]
    column=[]
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                row.append(i)
                column.append(j)
    for i in row:
        s[i,:] = 0
    for i in column:
        s[:,i] = 0
    return s

def isSubstring(x,y):
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i+j]!= y[j]:
                break
            else:
                if j == len(y)-1:
                    return True
    return False

def substring(x,y):
    for i in range(len(x)):
        if x[i:i+len(y)]==y:
            return True
    return False

def isRotated(x,y):
    if len(x) != len(y):
        return False
    x_double= x+x
    return substring(x_double,y)
        