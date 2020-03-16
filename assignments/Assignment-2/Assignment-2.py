import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

class structure_data:
    
    def __init__(self): 
        self.reviews = []
    
    ###  Extracting Data from file  ###
    def extractData(self):
        dataFrame = pd.read_csv("Movies_TV.txt", delimiter='\t')
        for review in dataFrame.Review:
            self.reviews.append(review)
        

    ###  Binary representation   ###

    def binaryStruct(self):
        vec = CountVectorizer(ngram_range=(1, 3), max_df=100, min_df=10, max_features=1000, binary=True)
        x = vec.fit_transform(self.reviews)
        return pd.DataFrame(x.toarray(), columns=sorted(vec.vocabulary_.keys()))
    

    ###  Frequency representation   ###

    def frequencyStruct(self):
        vec = CountVectorizer(ngram_range=(1, 3), max_df=100, min_df=10, max_features=1000, binary=False)
        x = vec.fit_transform(self.reviews)
        return pd.DataFrame(x.toarray(), columns=sorted(vec.vocabulary_.keys()))


    ###  Binary representation using Tfid   ###

    def binary_tfid(self):
        vec = TfidfVectorizer(ngram_range=(1, 3), max_df=100, min_df=10, max_features=1000, binary=True)
        x = vec.fit_transform(self.reviews)
        return pd.DataFrame(x.toarray(), columns=sorted(vec.vocabulary_.keys()))
     

    ###  Frequency  representation using Tfid   ###

    def frequency_tfid(self):
        vec = TfidfVectorizer(ngram_range=(1, 3), max_df=100, min_df=10, max_features=1000, binary=False)
        x = vec.fit_transform(self.reviews)
        return pd.DataFrame(x.toarray(), columns=sorted(vec.vocabulary_.keys()))
            


