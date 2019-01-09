import re

def abbreviate(words):
    if '-' not in words:
        words_list = words.split(' ')
    elif ' - ' in words:
        words_list = words.replace(" - "," ").split(' ')
    elif '-' in words:
        words_list = re.split('-| ', words)
    return ''.join([word[0].upper() for word in words_list])
