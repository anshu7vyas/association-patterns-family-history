'''
Created on Mar 8, 2015

@author: NANSH
'''

import re
import sys
#import os
#os.getcwd()

## Entering the files as arguments : [1. WordAssociations.txt] [2. OriginalSentences.txt] [3. OuputFile.txt] 
associations = sys.argv[1]
familySentences = sys.argv[2]
output_File = sys.argv[3]

def kSpan(k):       # k is the parameter where k = 3, 5, 10
    
    ## Opening the Word Associations File and Original Sentences file. 
    with open(associations,'r') as in_file:
        wordSets = in_file.readlines()      #Putting each sentence in wordSets
        
    with open(familySentences,'r') as sentFile:
        sentences = sentFile.readlines()    #Putting each sentences in sentences data structure
        #sentences = str(sentences).lower()   
    sentFile.close()
        
    countUnion = 0      #Total number of associations
    
    fout = open(output_File, 'w')
    
    for union in wordSets:
        countUnion += 1
        
        union = union.replace('(','')
        union = union.replace(')','')
        union = union.strip()       #Trimming the spaces (leading and trailing) 
        sack = union.split()        #Store each word in union
        supp = sack[-1]             #defining support as the format ['sentences', '(support)']
        del sack[-1] 
        unionSet = set(sack)        #Putting associations within a set
        
        count_Span = 0      #Counting associations within span
        counter = 0         # Counter for the association set found in sentence
        #check = False
        
        for sent in sentences:
            sent = sent.strip()
            regex = re.compile('[\W_]+', re.U)      # Only alphanumeric
            sent = re.sub(regex, " ", sent, count=0, flags=0)
                
            wordList = sent.split() #split into list
            wordOrigin = set(wordList) #Putting words in a set
                
            if unionSet.issubset(wordOrigin): ## CHECK IF THE ASSOCIATION SET IS WITHIN ORIGINAL WORDS SET
                #check
                counter +=1 
                span = max(wordList.index(a) for a in sack) - min(wordList.index(a) for a in sack) + 1 ## DEFINING SPAN
                if span > 1 and span <= k:
                    count_Span +=1 
            """else:
                check = False
                break"""
            
        if count_Span > 0.4 * counter: ## CHECK IF THE ASSOCIATIONS ARE MORE FREQUENT THAN 40% 
            #print unionSet
            fout.write(' '.join(unionSet) + '(' + str(supp) + ')' + "\n")       #write in the output file
                
    fout.close()
    in_file.close()            
                
kSpan(3)        ##CHECK FOR VALUES K = 3, 5, 10