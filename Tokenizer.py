from nltk.corpus import stopwords
import re

stopwords_english = set(stopwords.words('english'))

def get_list_tokens_nltk(corpus, file_name):
    string = get_raw_text(corpus,file_name)
    return get_list_tokens_string(string)

#!!!!!!!!------Possible Improvement: Stemming--------------#
  

def get_list_tokens_string(string):
    list_words = re.split(r'\W+',string)
    return [w.lower() for w in list_words if w.isalpha() and len(w)>1 and w.lower() not in stopwords_english]    


def get_raw_text(corpus,file_name):
    string=''
    if corpus=='mr':
        from nltk.corpus import movie_reviews
        string = movie_reviews.raw(fileids=file_name)
    else:
        from nltk.corpus import reuters
        string = reuters.raw(fileids=file_name)
    return string

def get_list_fileids(corpus):
    li=[]
    if corpus=='mr':
        from nltk.corpus import movie_reviews
        li = movie_reviews.fileids()
    else:
        from nltk.corpus import reuters
        li = reuters.fileids()
    return li

