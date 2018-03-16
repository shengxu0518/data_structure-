#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:25:18 2017

@author: supperxxxs
"""

def repalceBit(N,M,i,j):
    mask = 2**(j-i+1)-1
    mask = mask<<i
    mask = (2**32-1)-mask
    N= mask & N
    M=M << i
    N= N | M
    return N

def convert(M,N):
    diff = M ^ N
    count = 0
    while diff>0:
       count+=diff%2
       diff = int(diff/2)
    return count

def swap(M):
    a = 0xAAAAAAAA
    b = 0x55555555
    return ((M & a)>>1) +((M & b)<<1)
