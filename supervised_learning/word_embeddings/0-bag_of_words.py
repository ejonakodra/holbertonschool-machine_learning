#!/usr/bin/env python3
"""Bag of words"""

from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words(sentences, vocab=None):
    """
    bag of words function
    Args:
        sentences: list of sentences to analize
        vocab: list of the vocabulary words to use for the analysis
    Returns: embeddings, features
    """
    if vocab is None:
        vectorizer = CountVectorizer()
    else:
        vectorizer = CountVectorizer(vocabulary=vocab)

    embeddings = vectorizer.fit_transform(sentences).toarray()
    features = vectorizer.get_feature_names_out()

    return embeddings, features