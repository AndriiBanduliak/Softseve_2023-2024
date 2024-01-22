def string_int(str1):
    try:
        # Преобразовать строку в число
        number = int(str1)
        # Проверить, что число положительное
        if number > 0:
            return number
        else:
            return "Not a number"
    except ValueError:
        # Вернуть строку, если преобразование не удалось
        return "Not a number"