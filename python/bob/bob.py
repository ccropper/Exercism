def hey(phrase):
    is_question = False
    yelling = False
    # strip the spaces from input
    phrase = phrase.replace(" ", "").rstrip().lstrip()
    # if input is empty, return "Fine. Be that way!"
    if not phrase:
        return "Fine. Be that way!"
    # check if last character is a ?
    if phrase[-1] == '?':
        is_question = True
    # strip all non-letter characters from input
    alpha_phrase = ''.join(filter(str.isalpha, phrase))
    if alpha_phrase.lower() != alpha_phrase and alpha_phrase.upper() == alpha_phrase:
            yelling = True
    if yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    return "Whatever."
