def is_pangram(sentence):
    alphabet =('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    sentence_unique_letters = []
    for letter in sentence:
        if letter.lower() in alphabet and letter.lower() not in sentence_unique_letters:
            sentence_unique_letters.append(letter.lower())
    return len(sentence_unique_letters) == 26
