from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
from nltk import ngrams
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

# def r_num(inp):
#     inp2 = []
#     for row in inp:
#         row = [i for i in row if not re.search(r'\d', i)]
#         inp2.append(row)
#     return inp2

# Ngram Section

sentence = inputData[0]
words = sentence.split(' ')
def Ngrams(words)
    unigrams = list(ngrams(words, 1))
    bigrams = list(ngrams(words, 2))
    trigrams = list(ngrams(words, 3))
    print("unigrams", unigrams)
    print("---------")
    print("bigrams", bigrams)
    print("---------")
    print("trigrams", trigrams)

def NgramsProb(words):
    unigrams_prob = [words.count(x)/len(set(words)) for x in words]
    print("unigram Probs\n")
    print(unigrams_prob)
    print("\n")

    print("\nbi grams Probs\n")
    bigrams_freq = []
    for b in bigrams:
        temp = bigrams.count(b)
        temp2 = words.count(b[0])
        bigrams_freq.append(temp/temp2)
    print(bigrams_freq)
    
    print("\nbi grams Probs\n")
    trigrams_freq = [trigrams.count(x)/bigrams.count(x[:2]) for x in trigrams]
    print(trigrams_freq)
    return


# Average Section
def totel_tokens(inp):
    inp2 = []
    for row in inp:
        words = word_tokenize(row)
        inp2.append(words)
    return len(inp2)
t_tokens = totel_tokens(inputData)
print("total tokens: ", t_tokens)
print("Unique tokens: " set(t_tokens))

def avg_reivews(inp):
    avg_len = []
    for row in inp:
        rl = rl + len(row)
        avg_len.append(float(rl/len(inp)))
    return avg_len
print("Average length of reivews: ", avg_len(inputData))


def avg_token(inp):
    avg_tokens = []
    for row in inp:
        rl = len(row)
        words = word_tokenize(row)
        tl = float(len(words)/rl)
        avg_tokens.append(tl)
    return avg_tokens
print("average length of tokens with in a reivews: ", avg_token(inputData))



# def r_num(inp):
#     inp2 = []
#     for row in inp:
#         row = [i for i in row if not re.search(r'\d', i)]
#         inp2.append(row)
#     return inp2


def Display():
    print("Select below\n")
    print("------------\n")
    print("1: Text Normilization Process\n")
    print("2: Ngrams Sections\n")
    print("3 Average Sections\n")
    inp = input("Enter your value\n")
    inp = int(inp)
    
    if(inp == 1):
        print(" Removing unwanted whitespaces \n", inputData = unwantd_spaces(inputData))
        print(" Normalizing case\n ", inputData = normlizing_case(inputData))
        print("Removing Stop_words\n ", inputData = r_stop_words(inputData))
        print("Removing punctuations\n ", inputData = r_punc(inputData))
        print("Stemming words process\n ", inputData = stemming(inputData))
        print("Lemmatizing words\n ", inputData = lemmitization(inputData))
        print("Data after Processing\n\n")
        print(inputData)
        return 
    if(inp == 2):
        print("Ngrams:\n", Ngrams(words))
        print("Ngrams Probs\n ", NgramsProb(words))
        return
    if(inp == 3):
        totel_tokens(inputData)
        print("\n")
        avg_reivews(inputData)
        print("\n")
        avg_token(inputData)
        print("\n")
        return
    else:
        print("You entered wrong number\n")
        return Display()
        

diplay()