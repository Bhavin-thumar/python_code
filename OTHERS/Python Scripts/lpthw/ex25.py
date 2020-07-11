def break_words(stuff):
    """this function break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in full sentence and return sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints first and last word of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """prints first and last word of sorted sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
