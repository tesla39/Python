import numpy as np
import nltk        #Natural Language Toolkit for natural language processing
from nltk.stem.porter import PorterStemmer  #portstemmer is an algorithm for reducing word to their base or root form

Stemmer =PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    # sentence_word=[stem(word) for word in tokenized_sentence]
    sentence_word = list(map(stem, tokenized_sentence))
    bag=np.zeros(len(words),dtype=np.float32) #numpy array bag is initialized with zero 
                                              #and length is equal unique word in the wordlist

    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx]=1

    return bag 