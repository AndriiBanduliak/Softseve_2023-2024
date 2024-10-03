def isPalindrome(s):
    # Словарь для подсчета количества символов
    char_count = {}

    # Подсчёт частоты каждого символа
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Подсчёт количества символов с нечётной частотой
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Строка может быть палиндромом, если нечётных символов <= 1
    return odd_count <= 1
