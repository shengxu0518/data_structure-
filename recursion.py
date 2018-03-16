#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:46:24 2018

@author: supperxxxs
"""
import copy

def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)
   
def GetSubset(a):
    allsubsets = []   
    allsubsets.append([])
    for i in a:
        s= copy.deepcopy(allsubsets)
        for j in s:
            j.append(i)
        allsubsets.extend(s)
    return allsubsets

#recursion
def GetSubset1(a,index):
    allsubsets =[]
    if len(a) == index:
        allsubsets.append([])
    else:
        allsubsets=GetSubset1(a,index+1)
        item =a[index]
        s= []
        for i in allsubsets:
            b =[]
            b.extend(i)
            b.append(item)
            s.append(b)
        allsubsets.extend(s)
    return allsubsets

chess = [0 for i in range(8)]            
def CheckQueens(row):
    for i in range(row):
        diff= chess[row]-chess[i]
        if diff == 0 or diff == i-row or diff == row-i:
            return False
    return True

def EightQueens(row):
    if row == 8:
        print(chess)
        return
    for i in range(8):
        chess[row] = i
        if CheckQueens(row):
            EightQueens(row+1)

typeofcoin = [25,10,5,1]    
def Changes(n,i):
    if i==3:
        return 1
    ways=0
    while n>0:
        ways+=Changes(n,i+1)
        n-=typeofcoin[i]
    return ways
        
    
    