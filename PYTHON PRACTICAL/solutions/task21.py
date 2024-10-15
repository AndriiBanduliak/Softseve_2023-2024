def toPostFixExpression(expression):
    # Приоритеты операторов
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2
    }

    # Стек для операторов и скобок
    stack = []
    # Выходная строка для постфиксного выражения
    output = []

    for token in expression:
        if token.isdigit():  # Если это число, сразу добавляем его в результат
            output.append(token)
        elif token == '(':  # Открывающая скобка
            stack.append(token)
        elif token == ')':  # Закрывающая скобка
            # Выталкиваем операторы до ближайшей открывающей скобки
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Удаляем '('
        else:  # Если это оператор
            # Пока есть операторы в стеке и они имеют больший или равный приоритет
            while (stack and stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)  # Помещаем текущий оператор в стек

    # Выталкиваем оставшиеся операторы из стека
    while stack:
        output.append(stack.pop())

    return output
