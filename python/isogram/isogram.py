import re
def is_isogram(string):
    letters = re.sub('[^A-Za-z0-9]+', '', string).lower()
    used_letters = ()
    for letter in letters:
        if letter not in used_letters:
            used_letters = used_letters + (letter,)
        elif letter in used_letters:
            return False
    return True