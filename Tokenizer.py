from nltk.corpus import stopwords
import re

sw = set(stopwords.words('english'))

def get_list_tokens_nltk(corpus, fileName):
    string = get_raw_text(corpus,fileName)
    return get_list_tokens_string(string)

#!!!!!!!!------Possible Improvement: Stemming--------------#
  

def get_list_tokens_string(string):
    listWords = re.split(r'\W+',string)
    return [w.lower() for w in listWords if w.isalpha() and len(w)>1 and w.lower() not in sw]    


def get_raw_text(corpus,fileName):
    string=''
    if corpus=='mr':
        from nltk.corpus import movie_reviews
        string = movie_reviews.raw(fileids=fileName)
    else:
        from nltk.corpus import reuters
        string = reuters.raw(fileids=fileName)
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

