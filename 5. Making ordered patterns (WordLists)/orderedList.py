'''
Created on Mar 9, 2015

@author: Anshul
'''
import sys
import re
from itertools import permutations

## Entering the files as arguments : [1. WordAssociations.txt] [2. OriginalSentences.txt] [3. OuputFile.txt] 
associationK = sys.argv[1]
origin = sys.argv[2]
#orderedList_out = sys.argv[3]

def orderedList():
    
    ## Opening the Word Associations File and Original Sentences file. 
    with open(associationK,'r') as in_file:
        wordSets = in_file.readlines()      #Putting each sentence in wordSets    
    
    with open(origin,'r') as sentFile:
        sentences = sentFile.readlines()    #Putting each sentences in sentences data structure
        #sentences = str(sentences).lower()   
    sentFile.close()
        
    countUnion = 0
    permuteFreq = 0
    
    #fout = open(orderedList_out, 'w')

    
    for union in wordSets:    
        countUnion += 1
        s = union.split()
        del s[-1]
        #print s
        perms = permutations(s, r=None)
    
        for perm in perms:
            #print perm
            permute = str(perm)
            permute = permute.split()
        
            for sent in sentences:
                sent = sent.strip()
                regex = re.compile('[\W_]+', re.U)      # Only alphanumeric
                sent = re.sub(regex, " ", sent, count=0, flags=0)
                sentList = sent.split()     #split into list
                #print sent
                
                if ((c == ch for c in sentList) for ch in permute):
                    permuteFreq +=1
                print permuteFreq
            
                #fout.write(' '.join(permOut) + " (" + str(permuteFreq) + ") " + '\n')
            
    #fout.close()
    in_file.close()
    
orderedList()      
"""            
        
            for sent in sentences:    
                sent = sent.strip()
                
                regex = re.compile('[\W_]+', re.U)      # Only alphanumeric
                sent = re.sub(regex, " ", sent, count=0, flags=0)
                wordList = sent.split()         #split into list
                print wordList
                if perm in wordList:
                    permuteFreq +=1
                    #print perm
                else:
                    break
                
    fout.write(' '.join(perm) + " (" + str(permuteFreq) + ") " + '\n')
    
   
    """
#orderedList()   