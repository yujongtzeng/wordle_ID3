#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 06:47:19 2022

@author: yujong
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:13:34 2022

@author: yujong

Compare the results of entropy matrix computed in '../src/entropy.py' against 
the entropy matrix by 3b1b. 


"""

import sys
sys.path.insert(1, '../src/')
       
import read_data
import entropy, compare
import from_3b1b


class test_3b1b:
    
    def __init__(self):
        
        #script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        #rel_path = "../data.txt"
        #abs_file_path = os.path.join(script_dir, rel_path)
        self.filters = read_data.readtxt('../data/Allowed_words.txt')
        self.answers = read_data.readtxt('../data/Possible_answers.txt')
        self.filters.extend(self.answers)          
    
    
    # This function will print out word if the entropy doesn't match.
    # Otherwise it shows how many cases have passed (same entropy).
    def testEntropy(self, filters, answers):               
        my = entropy.entropy(filters, answers)
        
        pat_matrix  = from_3b1b.generate_pattern_matrix(filters, answers)
        etp_matrix= from_3b1b.generate_entropy_matrix(pat_matrix)    
        count = 0
        for i, word in enumerate(filters):
            difference = []
            #print(etp_matrix[i], my.getEntropy(word))
            res = compare.entropy(word, etp_matrix[i], my.getEntropy(word))
            if res:
                count += 1
            else:
                difference.append(word)
                compare.entropy(word, etp_matrix[i], my.getEntropy(word), True)
        print(count, ' cases passed.')    
            

        
        
#data1 = ['aahed', 'lucky', 'crane']   
#data2 = ['cigar', 'rebut', 'sissy', 'humph', 'awake',
#         'blush', 'focal', 'evade', 'naval', 'serve', 
#         'heath', 'dwarf', 'model', 'karma', 'stink', 'grade']
#data3 = ['cigar', 'rebut', 'sissy', 'sissy']
#data4 = ['weary', 'slate', 'helio', 'bulla', 'khaki']


test = test_3b1b()
#result = test.testEntropy(test.filters, test.filters)       
result = test.testEntropy(test.filters, test.answers) 


    