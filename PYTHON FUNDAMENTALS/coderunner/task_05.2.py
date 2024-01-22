def count_vowels(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
