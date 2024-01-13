# Counts the number of occurrences of each word in a string.

#     Args:
#       string: The string to search.
#       words: A list of words to count.

#     Returns:
#       A dictionary mapping each word to its number of occurrences.


def count_words(string, words):

    word_counts = {}
    for word in words:
        word_counts[word] = 0

    for word in string.split():
        if word in word_counts:
            word_counts[word] += 1

    return word_counts


string = "Python is a better programming language. It is never too late to learn Python."

word_counts = count_words(string, ["better", "never", "is"])

print(word_counts)
