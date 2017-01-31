#!/usr/bin/env python
"""Semantic similarity net"""
import nltk
from nltk.corpus import wordnet


def contextsimilar(sentence):
    """return all contextually similar words"""
    for i in sentence.split(" "):
        text.similar(i)

        
def semanticallysimilar(sentence):
    """return synonyms and antonyms of word"""
    for word in sentence:
        synonyms, antonyms = [], []
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(str(l.name()))
                if l.antonyms():
                    antonyms.append(str(l.antonyms()[0].name()))
        print "Synonyms:", synonyms
        print "Antonyms:", antonyms

semanticallysimilar(["good", "boy"])
