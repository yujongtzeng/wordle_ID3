#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:26:55 2022

@author: yujong
"""

def entropy(word, expected, computed, output = False):
    
    if output:
        print('The entropy of %s is %.2f, we computed %.2f' % 
              (word, expected, computed))
    return abs(expected - computed) < 10**(-6)    
        
def patternLen(pat, expected, p_list):
    computed = len(p_list[pat])    
    print(pat, expected, 'computed:', computed)        