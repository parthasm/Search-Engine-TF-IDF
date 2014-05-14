from __future__ import division
import time
from nltk.corpus import reuters
from nltk.corpus import stopwords
import re
#from os import listdir
from os.path import isfile, join
from math import log
start_time = time.time()
sw = stopwords.words('english')

    


#val = my_dict.get(key, mydefaultval)
##1)Create a dictionary with word as key and list of documents where it occurs in sorted order as value

WordDocDict={}

##2)Loop through the reuters dataset, to get the entire text from  each file

for (fileIndex,fileName) in enumerate(reuters.fileids()):
    string = reuters.raw(fileids=fileName)

##3) Parse the string to get individual words


    listWords = re.split(r'\W+',string)
    listWords = [w.lower() for w in listWords if w.isalnum() and len(w)>1 and w not in sw]
    #!!!!!!!!------Possible Improvement: Stemming--------------#


##4) Update the dictionary
    for w in set(listWords):
        if WordDocDict.get(w,0)==0:
           WordDocDict[w]=[]
           
        WordDocDict[w].append(fileIndex)

print "Inverted Index has been prepared and it took"
print time.time() - start_time, "seconds"



##5) Getting the query from the user
n = int(input("Enter number of query words : "))
op = input("Enter the operator, (AND/OR) Default is AND: ")


QueryList=[]
ResultFileIndices=[]

for i in range(n):
    QueryList.append(input("Enter query word: "))

start_time = time.time()
if op=='OR':
    for query in QueryList:
        if WordDocDict.get(query.lower(), 0)!=0:
            ResultFileIndices.extend(WordDocDict[query.lower()])
else:
    FileIndices=range(len(reuters.fileids()))
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
    #for index in ResultFileIndices:
     #   print reuters.fileids()[index]
      #  print reuters.words(fileids=reuters.fileids()[index])[:20]
            
