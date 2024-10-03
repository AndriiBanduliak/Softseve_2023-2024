def filterBible(scripture, book, chapter):
    # Комбинируем book и chapter в строку для сравнения
    target_prefix = book + chapter
    # Фильтруем стихи, которые начинаются с этой строки
    return [verse for verse in scripture if verse.startswith(target_prefix)]
