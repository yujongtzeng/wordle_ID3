#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 06:49:05 2022

@author: yujong

Issue: printPattenList need to sort before printing
"""

import pattern
import math
import json


import collections
class entropy:
    """
    filters: List[strings], the list of possible guess
    answers: List[strings], the list of all possible answers
    
    """
    
    def __init__(self, filters, answers):
        self.filters = filters
        self.answers = answers
        self.entropy = {}
        self.sorted_entropy = {}
        self.pattern_list = {} 
        
        # compute self.pattern_list
        # For each filter word in self.filters, classify words in self.answers
        # by the matching patterns and store in self.pattern_list          
        for i, fword in enumerate(self.filters):
            self.pattern_list[fword] = collections.defaultdict(list)
            for ans in self.answers:
                pat = pattern.pattern(fword, ans)                
                self.pattern_list[fword][pat].append(ans)
                  
        # compute self.entropy (the entropy matrix)           
        for i, fword in enumerate(self.filters):
            ent = 0
            for pat in self.pattern_list[fword]:                            
                p = len(self.pattern_list[fword][pat]) / len(self.answers) 
                ent -= p * math.log2(p) if p > 0 else 0    
            self.entropy[fword] = ent             
    
    def getEntropy(self, word):
        return self.entropy[word]
    
    def getPatternList(self, fword):
        return self.pattern_list[fword]
    
    def printPatternList(self, outputfile):
        with open(outputfile) as file_o:
            json.dump(self.pattern_list, file_o)
    
    def printEntropy(self, outputfile):
        if not self.sorted_entropy:
            self.sorted_entropy = sorted(self.entropy.items(), 
                                         key= lambda x: x[1], reverse=True)
        with open(outputfile, 'w') as f:
            json.dump(self.sorted_entropy, f)      
            
    def findBest(self):                
        bestWord, maxE = "", 0
        for key  in self.entropy:
            if self.entropy[key] > maxE:
                bestWord, maxE = key, self.entropy[key]
        return bestWord, maxE  


        
    def getNBestWords(self, n = 5):
        if not self.sorted_entropy:
            self.sorted_entropy = sorted(self.entropy.items(), 
                                         key=lambda x: x[1], reverse=True)
        print(["%s: %.2f" % (key, v) for (key, v) in self.sorted_entropy[:n]])            
 

# For print out the best first guesses and their entropy               
import read_data            
filters = read_data.readtxt('../data/Allowed_words.txt')
answers = read_data.readtxt('../data/Possible_answers.txt')
filters.extend(answers)              

en_test = entropy(filters, answers)
en_test.printEntropy('../data/best_words.json')
