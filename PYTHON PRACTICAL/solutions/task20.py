def findPermutation(p, q):
    # Инициализируем массив для результата
    r = []

    # Для каждого элемента в q находим его индекс в p
    for element in q:
        # Индекс элемента в p
        index_in_p = p.index(element)
        # Добавляем индекс в r (не забываем, что индексы начинаются с 1)
        r.append(index_in_p + 1)

    return r
