# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:52:54 2021

@author: SHARATH
"""

import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')


def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in tagged_sentence:
            if chunk[1] =='NN' or chunk[1]=='JJ':
                names.append(chunk[0])
    return names

# final_name = extract_names("yes, darshan , ruchira and siddhi")
