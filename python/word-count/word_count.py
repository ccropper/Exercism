import collections
import re

def word_count(phrase):
    words_list = re.findall("[0-9a-zA-Z']+", phrase)
    words_list = (word.lower().strip("'") for word in words_list)
    return collections.Counter(words_list)
