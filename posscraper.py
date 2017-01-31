#!/usr/bin/env python
"""Scrape wiktionary for parts of speech"""
# run by python posscraper.py | swipl | egrep -v "false.|^$"
import os
import urllib2
import itertools
from urllib2 import Request
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer


# start [pos] on prolog.
print "[pos]."
# all parts of speech
pos = ['Noun', 'Verb', 'Adverb', 'Adjective', 'Preposition', 'Conjunction', 'Article', 'Determiner']
# punctuation remover from sentence
tokenizer = RegexpTokenizer(r'\w+')


def returnallpos(word):
    """return all possible pos of word from wiktionary"""
    soup = BeautifulSoup(urllib2.urlopen(
        Request("https://en.wiktionary.org/wiki/" + word)), "html.parser")
    h3_dump = [str(element.get_text()).replace("\n", "").replace("[edit]", "")
           for element in soup.select('h3')]
    h4_dump = [str(element.get_text()).replace("\n", "").replace("[edit]", "")
           for element in soup.select('h4')]
    headings = h3_dump + h4_dump
    return sorted(set(headings) & set(pos), key = headings.index)


def posfromsentence(sentence):
    """return all possible pos of each word from sentence"""
    sentencelist = []
    for word in tokenizer.tokenize(sentence.lower()):
        sentencelist.append(returnallpos(word))
    return sentencelist


def structuresearch(sentence):
    sentencelist = posfromsentence(sentence)
    for x in itertools.product(*sentencelist):
        print("convert(sentence([" + ", ".join(x).lower() + "]), A).")
        
    
s = """The complex houses married and single soldiers and their families."""
sentence = "How can the net amount of entropy of the universe be massively decreased"

structuresearch("Time flies like an arrow.")
