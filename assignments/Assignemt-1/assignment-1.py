from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
from string import punctuation as punc
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction import stop_words
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
wl = WordNetLemmatizer()
ps = PorterStemmer()
stop_word = list(stop_words.ENGLISH_STOP_WORDS)


corpus = open('Movies_TV.txt').read()

corpus = re.sub(r'Domain.*\n', '', corpus)
rows = corpus.split('\n')
rows.remove(rows[-1])
inputData, y = [], []
for row in rows:
    _, label, _, review = row.split('\t')
    inputData.append(review)
    y.append(label)




#print(inputData[1])
print("----------------------")

def normlizing_case(inp):
    inp2 = []
    for row in inp:
        row = row.lower()
        inp2.append(row)
    return inp2

def unwantd_spaces(inp):
    inp2 = []
    for row in inp:
        row = re.sub(' +', ' ', row)
        inp2.append(row)
    return inp2


def r_punc(inp):
    inp2 = []
    for row in inp:
        row = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', ' ', row).lower()
        inp2.append(row)
    return unwantd_spaces(inp2)


#### Stop Words #####
def r_stop_words(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        words = [word for word in words if not word in stop_word]
        row = ' '.join(words)
        inp2.append(row)
    return inp2



def stemming(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        words = [ps.stem(word) for word in words if not word in stop_word]
        row = ' '.join(words)
        inp2.append(row)
    return inp2

def lemmitization(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        words = [wl.lemmatize(word) for word in words if not word in stop_word]
        row = ' '.join(words)
        inp2.append(row)
    return inp2

def r_num(inp):
    inp2 = []
    for row in inp:
        row = [i for i in row if not re.search(r'\d', i)]
        inp2.append(row)
    return inp2

inputData = unwantd_spaces(inputData)
inputData = normlizing_case(inputData)
inputData = r_punc(inputData)
inputData = r_stop_words(inputData)
inputData = stemming(inputData)
inputData = lemmitization(inputData)
#inputData[0]from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
from string import punctuation as punc
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction import stop_words
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
wl = WordNetLemmatizer()
ps = PorterStemmer()
stop_word = list(stop_words.ENGLISH_STOP_WORDS)


corpus = open('Movies_TV.txt').read()

corpus = re.sub(r'Domain.*\n', '', corpus)
rows = corpus.split('\n')
rows.remove(rows[-1])
inputData, y = [], []
for row in rows:
    _, label, _, review = row.split('\t')
    inputData.append(review)
    y.append(label)




#print(inputData[1])
print("----------------------")

def normlizing_case(inp):
    inp2 = []
    for row in inp:
        row = row.lower()
        inp2.append(row)
    return inp2

def unwantd_spaces(inp):
    inp2 = []
    for row in inp:
        row = re.sub(' +', ' ', row)
        inp2.append(row)
    return inp2


def r_punc(inp):
    inp2 = []
    for row in inp:
        row = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', ' ', row).lower()
        inp2.append(row)
    return unwantd_spaces(inp2)


#### Stop Words #####
def r_stop_words(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        words = [word for word in words if not word in stop_word]
        row = ' '.join(words)
        inp2.append(row)
    return inp2



def stemming(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        words = [ps.stem(word) for word in words if not word in stop_word]
        row = ' '.join(words)
        inp2.append(row)
    return inp2

def lemmitization(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        words = [wl.lemmatize(word) for word in words if not word in stop_word]
        row = ' '.join(words)
        inp2.append(row)
    return inp2

def r_num(inp):
    inp2 = []
    for row in inp:
        row = [i for i in row if not re.search(r'\d', i)]
        inp2.append(row)
    return inp2

inputData = unwantd_spaces(inputData)
inputData = normlizing_case(inputData)
inputData = r_punc(inputData)
inputData = r_stop_words(inputData)
inputData = stemming(inputData)
inputData = lemmitization(inputData)
#inputData[0]
