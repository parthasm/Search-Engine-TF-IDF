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
list_fileids =  Tokenizer.get_list_fileids(corpus)   
num_docs = len(list_fileids)    

#val = my_dict.get(key, mydefaultval)
##1)Create a dictionary with word as key and a dictionary with documents where it occurs as keys and term frequency(tf) values as values

word_doc_dict={}


##2)Loop through the dataset, to get the entire text from  each file

for (file_index,file_name) in enumerate(list_fileids):
    
##3) Parse the string to get individual words    

    list_words = Tokenizer.get_list_tokens_nltk(corpus,file_name)
    #!!!!!!!!------Possible Improvement: Stemming--------------#

    
##4) Update the dictionary - 2 possible ways
    ##A) loop over the set of words and update dictionary with count value
        ##Complexity- n(set)*n(count operation) = O(n^2)
    ##B) loop over list and update count for each occurence
        ##Complexity- n(list) = O(n)
        ##B is better and takes one second lesser time to prepare the index
    for w in list_words:
        if word_doc_dict.get(w,0)==0:
            word_doc_dict[w]={}
            word_doc_dict[w][file_index]=1
        else:
            word_doc_dict[w][file_index]=word_doc_dict[w].get(file_index,0)
            word_doc_dict[w][file_index]+=1
    #for w in set(list_words):
     #   word_doc_dict[w][file_index]=1+log(word_doc_dict[w][file_index])
###Storing tf scores in dictionary
        
print "Inverted Index has been prepared and it took"
print time.time() - start_time, "seconds"



##5) Getting the query from the user
query = input("Enter your query string : ")

result_file_dict={}

start_time = time.time()

##6) Tokenizing query string to get individual words
query_list = Tokenizer.get_list_tokens_string(query)


##7) Calculating tf-idf scores 
for q in query_list:
    d = word_doc_dict.get(q,0) 
    if d!=0:
        length=len(d)
        for file_index in d.keys():
            result_file_dict[file_index] = result_file_dict.get(file_index,0)
            result_file_dict[file_index]+=((1+log(d[file_index]))*(log(num_docs/length)/log(10)))
                                        #1st term is tf # 2nd term is idf

##8) Sorting the dictionary based on its values            
result_file_indices = sorted(result_file_dict.items(), key=lambda x:x[1],reverse = True)

print "Time taken to search"
print (time.time() - start_time), "seconds"

if(len(result_file_indices)==0):
    print "Sorry No matches found"
else:
    print "Number of search results : " , len(result_file_indices)
    if len(result_file_indices) > 10:
        print "Returning 1st 10 results"
    for (index,tup) in enumerate(result_file_indices):
        if index==10:
            break
        #print tup[0],list_fileids[tup[0]], tup[1]
        print Tokenizer.get_raw_text(corpus,list_fileids[tup[0]])[:40]
        print "\n"

###--------------------DEBUG STATEMENTS----------------------
        #string = Tokenizer.get_raw_text(corpus,list_fileids[tup[0]])
        #list_words = Tokenizer.get_list_tokens_string(string)
        #print list_words.count(query_list[0]) , list_words.count(query_list[1])  
        #print list_words.count(query_list[2]) , list_words.count(query_list[3]) ,
        #print list_words.count(query_list[4]) , list_words.count(query_list[5]) ,
        #print list_words.count(query_list[6]) , list_words.count(query_list[7])
###--------------------DEBUG STATEMENTS----------------------

            

###Floating point inaccuracies make exact reproduction of tf-idf scores impossible
