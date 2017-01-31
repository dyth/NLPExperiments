# NLP Experiments


*  **posscraper.py and pos.pl:** An attempt to parse a sentence using a grammar of object-relation-object and a simple parser. possscraper works by tokenising a sentence and scraping wiktionary for the parts of speech of the word. This is then fed into pos, which recursively applies definitions to the pos.

Example usage:

> python posscraper.py | swipl | egrep -v "false.|^$

* *semanticnet.py:* returns synonyms of all words within an input