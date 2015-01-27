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

#val = my_dict.get(key, mydefaultval)
##1)Create a dictionary with word as key and list of documents where it occurs in sorted order as value

word_doc_dict={}

##2)Loop through the dataset, to get the entire text from  each file

for (file_index,file_name) in enumerate(list_fileids):
    list_words = Tokenizer.get_list_tokens_nltk(corpus,file_name)

##3) Parse the string to get individual words

    #!!!!!!!!------Possible Improvement: Stemming--------------#


##4) Update the dictionary
    for w in set(list_words):
        if word_doc_dict.get(w,0)==0:
           word_doc_dict[w]=[]
           
        word_doc_dict[w].append(file_index)

print "Inverted Index has been prepared and it took"
print time.time() - start_time, "seconds"



##5) Getting the query from the user
query = input("Enter your query string : ")
op = input("Enter the operator, (AND/OR) Default is AND: ")

start_time = time.time()
query_list=Tokenizer.get_list_tokens_string(query)
result_file_indices=[]




if op=='OR':
    for q in query_list:
        if word_doc_dict.get(q.lower(), 0)!=0:
            result_file_indices.extend(word_doc_dict[q.lower()])
else:
    file_indices=range(len(list_fileids))
    for q in query_list:
        if word_doc_dict.get(q.lower(), 0)==0:
            file_indices=[]        
            break
        else:
            temp_list=[]
            query_file_indices=word_doc_dict[q.lower()]
            index_f=0
            index_q=0
            while index_f < len(file_indices) and index_q < len(query_file_indices):
                if file_indices[index_f]==query_file_indices[index_q]:
                    temp_list.append(query_file_indices[index_q])
                    index_f+=1
                    index_q+=1
                elif file_indices[index_f] < query_file_indices[index_q]:
                    index_f+=1
                else:
                    index_q+=1
            file_indices=[]
            file_indices.extend(temp_list)
    result_file_indices.extend(file_indices)

print "Time taken to search"
print time.time() - start_time, "seconds"

if(len(result_file_indices)==0):
    print "Sorry No matches found"
else:
    print "Number of search results : " , len(result_file_indices)
    for index in result_file_indices:
        print Tokenizer.get_raw_text(corpus,list_fileids[index])[:40]
        print "\n"
      
            
