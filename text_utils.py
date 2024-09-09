def count_chars(text):
    if not text:
        return 0
    
    # if the text doesnt have anything, it returns 0
    
    total = 0
    for chars in text:
        total += 1
    return total

    # it counts all of the characters that are in the text and adds it to the total

def count_words(text):
    if not text:
        return 0
    
    # if the text doesnt have anything, it returns 0

    total = 0
    for words in text.split(" "):
        total += 1
    return total

    # it counts all of the words (every word is split by a space " ") that are in the text and adds it to the total


def count_sentences(text):
    total = 0
    for sentences in text:
        if sentences == "." or sentences == "?" or sentences == "!":
            total += 1
    return total

    # it counts all of the punctuation in the text and adds them up together
