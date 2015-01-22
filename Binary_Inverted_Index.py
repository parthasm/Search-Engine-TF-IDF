from __future__ import division
import time
import Tokenizer
from math import log

i = input('Enter within quotes, m for movie reviews corpus,'
          'r for reuters corpus( default is reuters) : ')

corpus=''

if i=='m' or i=='M':
    corpus='mr'
else:
    corpus='reuters'

start_time = time.time()

ListFileids =  Tokenizer.get_list_fileids(corpus)

#val = my_dict.get(key, mydefaultval)
##1)Create a dictionary with word as key and list of documents where it occurs in sorted order as value

WordDocDict={}

##2)Loop through the dataset, to get the entire text from  each file

for (fileIndex,fileName) in enumerate(ListFileids):
    listWords = Tokenizer.get_list_tokens_nltk(corpus,fileName)

##3) Parse the string to get individual words

    #!!!!!!!!------Possible Improvement: Stemming--------------#


##4) Update the dictionary
    for w in set(listWords):
        if WordDocDict.get(w,0)==0:
           WordDocDict[w]=[]
           
        WordDocDict[w].append(fileIndex)

print "Inverted Index has been prepared and it took"
print time.time() - start_time, "seconds"



##5) Getting the query from the user
Query = input("Enter your query string : ")
op = input("Enter the operator, (AND/OR) Default is AND: ")

start_time = time.time()
QueryList=Tokenizer.get_list_tokens_string(Query)
ResultFileIndices=[]




if op=='OR':
    for query in QueryList:
        if WordDocDict.get(query.lower(), 0)!=0:
            ResultFileIndices.extend(WordDocDict[query.lower()])
else:
    FileIndices=range(len(ListFileids))
    for query in QueryList:
        if WordDocDict.get(query.lower(), 0)==0:
            FileIndices=[]        
            break
        else:
            TempList=[]
            QueryFileIndices=WordDocDict[query.lower()]
            indexF=0
            indexQ=0
            while indexF < len(FileIndices) and indexQ < len(QueryFileIndices):
                if FileIndices[indexF]==QueryFileIndices[indexQ]:
                    TempList.append(QueryFileIndices[indexQ])
                    indexF+=1
                    indexQ+=1
                elif FileIndices[indexF] < QueryFileIndices[indexQ]:
                    indexF+=1
                else:
                    indexQ+=1
            FileIndices=[]
            FileIndices.extend(TempList)
    ResultFileIndices.extend(FileIndices)

print "Time taken to search"
print time.time() - start_time, "seconds"

if(len(ResultFileIndices)==0):
    print "Sorry No matches found"
else:
    print "Number of search results : " , len(ResultFileIndices)
    for index in ResultFileIndices:
        print Tokenizer.get_raw_text(corpus,ListFileids[index])[:40]
        print "\n"
      
            
