def X_O(word):
    word = word.lower()  # Convert the string to lowercase
    return word.count('x') == word.count('o')