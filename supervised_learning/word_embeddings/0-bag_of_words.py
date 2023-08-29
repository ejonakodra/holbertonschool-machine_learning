#!/usr/bin/env python3
"""
Defines function that creates a bag of words embedding matrix
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words(sentences, vocab=None):
    """Creates a bag of words embedding matrix

    parameters:
        sentences [list]:
            list of sentences to analyze

        vocab [list]:
            list of vocabulary words to use for analysis
            if None, all words within sentences should be used

    returns:
        embeddings,features:
            embeddings [numpy.ndarray of shape (s, f)]:
                contains the embeddings
                s: number of sentences in sentences
                f: number of features analyzed
            features [list]:
                list of features used for embeddings"""
    if vocab is None:
        vocab = set(word for sentence in sentences for word in sentence.split())
    
    vectorizer = CountVectorizer(vocabulary=vocab)
    embeddings = vectorizer.transform(sentences).toarray()
    features = vectorizer.get_feature_names()
    
    return embeddings, features