#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:09:58 2022

@author: yujong

Issue: test doesn't match, expecially when guess has repeated characters
"""

def pattern(guess: str, answer: str):
    """
    compute the matching pattern of two strings guess and answer
    sample pattern: 'xggxy', 
    'b': black, not in answer, 
    'y': yellos, in answer but wrong positions
    'g': green, in answer and in right position
    """
    if len(guess) != len(answer):
        print('word lengths should be the same')
    pattern = ['b' for _ in range(len(guess))]
    wordbank = list(answer)
    
    # green pass
    for i in range(len(guess)):        
        if guess[i] == answer[i]:
            pattern[i] = 'g'
            wordbank.remove(guess[i])
    
    # yellow pass
    for i in range(len(guess)):
        if guess[i] in wordbank and pattern[i] != 'g':
            pattern[i] = 'y'
            wordbank.remove(guess[i])
    return "".join(pattern)       


