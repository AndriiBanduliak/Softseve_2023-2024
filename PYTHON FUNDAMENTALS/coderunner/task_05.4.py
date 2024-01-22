def is_isogram(word):
    normalized_word = word.lower()
    return len(normalized_word) == len(set(normalized_word))