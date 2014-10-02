Search-Engine-TF-IDF
=============

TO BE ADDED: TF IDF SEARCH WITH ALL THE DIFFERENT FORMULA WHICH WILL BE LISTED

Searching a Corpus, using Python.

The corpus used is the Reuters corpus available with "Natural Language Toolkit"(nltk)

http://nltk.org/


A) TF_IDF_Search_Reuters

The 'TF_IDF_Search_Reuters.py' performs ranked search, producing the top 10 search results. 

http://en.wikipedia.org/wiki/Tf%E2%80%93idf

http://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html

http://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html



Overview of Algorithm:
An inverted index is prepared which is a python dictionary with word as key and a dictionary as value
This nested dictionary has a document where the word occurs as key and log term frequency(tf) value as value

The result-set is a python dictionary with the document index as key and the product of the stored log term-frequency
and the calculated-on-the-fly-inverted-document-frequency as the value.This product is TF-IDF.

Then the result-set is reverse-sorted based on it values and the top 10 documents are displayed.

The time required to prepare the inverted index and the time required to return the search results are also reported.

B) Binary_Inverted_Index_Reuters

The 'Binary_Inverted_Index_Reuters.py' performs unranked search, producing all documents which satisfy the query.
The query can have one or more words. 

If the search mode is AND, then only the documents where ALL the search terms are present are displayed.

If the search mode is OR, then only the documents where ANY of  the search terms are present are displayed.



Default Search Mode: AND

Overview of Algorithm:
An inverted index is prepared which is a dictionary with word as key and list of document-indices where it occurs in sorted order as value.

http://en.wikipedia.org/wiki/Inverted_index

For an 'OR' query, all the documents for every query term is appended to the list of results.

For an 'AND' query, we walk through the sorted lists and only the documents present in all the lists are appended to the result-list.

The time required to prepare the inverted index and the time required to return the search results are also reported.


