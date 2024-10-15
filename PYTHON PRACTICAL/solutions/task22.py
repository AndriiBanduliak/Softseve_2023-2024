def order(a):
    is_ascending = True
    is_descending = True

    # Проверка на возрастание и убывание
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            is_descending = False
        elif a[i] < a[i - 1]:
            is_ascending = False

    if is_ascending:
        return "ascending"
    elif is_descending:
        return "descending"
    else:
        return "not sorted"
