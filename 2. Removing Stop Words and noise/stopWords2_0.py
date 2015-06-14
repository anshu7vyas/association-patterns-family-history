'''
Created on Mar 1, 2015

@author: Anshul
'''
import sys
from nltk.corpus import stopwords

def main():
    
    if len(sys.argv) is not 3:
        print 'incorrect arguments Input two files in this order: inputfilelist.txt outputfile.txt'
        sys.exit(2)
    else:
        familySentences = sys.argv[1]
        transformedFamilySentences = sys.argv[2]
        
    def remove_stopWords(familySentences):
        transformedFamilySentencesList = []
        
        #defining the stop words set for the file
        stopset = set(stopwords.words("english"))
        
        #checking for stop words and then appending tokens to transformedFamilySentencesList
        with open(familySentences, 'r') as text_file:
            for line in text_file:
                line = line.lower()
                line = line.replace(":","")
                line = line.replace(";","")
                line = line.replace("'","")
                line = line.replace('"',"")
                line = line.replace(",","")
                line = line.replace(".","")
                line = line.replace("-"," ")
                row = line.split()
                tokens = ' '.join([word for word in row if word not in stopset])
                #print tokens
                transformedFamilySentencesList.append(tokens)
        
        #Write output to transformedFamilySentences file
        transformedSentences = open(transformedFamilySentences, 'w')
        for sent1 in transformedFamilySentencesList:
            transformedSentences.write(sent1 + '\n')
        
        transformedSentences.close()
    
    remove_stopWords(familySentences)
                
if __name__ == "__main__":
    main()