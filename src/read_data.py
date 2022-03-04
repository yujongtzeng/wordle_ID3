#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:30:53 2022

@author: yujong
"""

def readtxt(txtfile):
    with open(txtfile) as file:
        data = file.read()
        datalist = data.split(",")
        return [w[1:6] for w in datalist]
    
#filters = read('Allowed_words.txt')    
#print(filters[:10])