import re

def word_count(phrase):
    words_dict = {}
    words_list = re.findall("[0-9a-zA-Z']+", phrase)
    words_list = [word.lower() for word in words_list]
    for word in words_list:
        if word[0] == "'" and word[-1] == "'":
            word = word [1:-1]
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict
