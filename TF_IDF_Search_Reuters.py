from __future__ import division
import time
import re
import Tokenizer
from math import log


i = input('Enter within quotes, m for movie reviews corpus,'
          'r for reuters corpus( default is reuters) : ')

corpus=''

if i=='m' or i=='M':
    corpus='mr'
else:
    corpus='reuters'
    
ListFileids =  Tokenizer.get_list_fileids(corpus)   
NumDocs = len(ListFileids)    
start_time = time.time()
#val = my_dict.get(key, mydefaultval)
##1)Create a dictionary with word as key and a dictionary with documents where it occurs as keys and term frequency(tf) values as values

WordDocDict={}


##2)Loop through the reuters dataset, to get the entire text from  each file

for (fileIndex,fileName) in enumerate(ListFileids):
    
##3) Parse the string to get individual words    

    listWords = Tokenizer.get_list_tokens_nltk(corpus,fileName)
    #!!!!!!!!------Possible Improvement: Stemming--------------#

    
##4) Update the dictionary - 2 possible ways
    ##A) loop over the set of words and update dictionary with count value
        ##Complexity- n(set)*n(count operation) = O(n^2)
    ##B) loop over list and update count for each occurence
        ##Complexity- n(list) = O(n)
        ##B is better and takes one second lesser time to prepare the index
    for w in listWords:
        if WordDocDict.get(w,0)==0:
            WordDocDict[w]={}
            WordDocDict[w][fileIndex]=1
        else:
            WordDocDict[w][fileIndex]=WordDocDict[w].get(fileIndex,0)
            WordDocDict[w][fileIndex]+=1
    #for w in set(listWords):
     #   WordDocDict[w][fileIndex]=1+log(WordDocDict[w][fileIndex])
###Storing tf scores in dictionary
        
print "Inverted Index has been prepared and it took"
print time.time() - start_time, "seconds"



##5) Getting the query from the user
Query = input("Enter your query string : ")

ResultFileDict={}

start_time = time.time()

##6) Tokenizing query string to get individual words
QueryList = Tokenizer.get_list_tokens_string(Query)


##7) Calculating tf-idf scores 
for q in QueryList:
    d = WordDocDict.get(q,0) 
    if d!=0:
        length=len(d)
        for fileIndex in d.keys():
            ResultFileDict[fileIndex] = ResultFileDict.get(fileIndex,0)
            ResultFileDict[fileIndex]+=((1+log(d[fileIndex]))*(log(NumDocs/length)/log(10)))
                                        #1st term is tf # 2nd term is idf

##8) Sorting the dictionary based on its values            
ResultFileIndices = sorted(ResultFileDict.items(), key=lambda x:x[1],reverse = True)

print "Time taken to search"
print (time.time() - start_time), "seconds"

if(len(ResultFileIndices)==0):
    print "Sorry No matches found"
else:
    print "Number of search results : " , len(ResultFileIndices)
    if len(ResultFileIndices) > 10:
        print "Returning 1st 10 results"
    for (index,tup) in enumerate(ResultFileIndices):
        if index==10:
            break
        #print tup[0],ListFileids[tup[0]], tup[1]
        print Tokenizer.get_raw_text(corpus,ListFileids[tup[0]])[:40]
        print "\n"

###--------------------DEBUG STATEMENTS----------------------
        #string = Tokenizer.get_raw_text(corpus,ListFileids[tup[0]])
        #listWords = Tokenizer.get_list_tokens_string(string)
        #print listWords.count(QueryList[0]) , listWords.count(QueryList[1])  
        #print listWords.count(QueryList[2]) , listWords.count(QueryList[3]) ,
        #print listWords.count(QueryList[4]) , listWords.count(QueryList[5]) ,
        #print listWords.count(QueryList[6]) , listWords.count(QueryList[7])
###--------------------DEBUG STATEMENTS----------------------

            

###Floating point inaccuracies make exact reproduction of tf-idf scores impossible
