import pymongo
# опис зробила для себе

# Список з назв мов (щоб легше було визначити)
lang = ["Delphi", "C#", "Oracle", "MongoDB", "MySQL", "ACCESS"]


def file_processing(line: str) -> dict:
    """
    Функція для обробки рядка з файлу
    Args:
        line (str): рядок з данними
    Returns:
        dict: сформованний словник
    """
    # тут розділяю рядок на частинки використовуючи пробіли
    parts = line.strip().split()

    #це тип проекту, беремо по індексу слово та видаляємо з ього зайві пробіли
    project_type = parts[0].strip()

    #це кількість поінтів, беремо останнє слово та видаляємо пробіли, видаляємо (якщо є) знак "+", видаляємо пробіли щоб ТОЧНО не було пробілів
    points_str = parts[-1].strip().rstrip('+').strip()
    # беремо всі частини рядків окрім першого та останнього(вже їх визначили)
    middle_parts = parts[1:-1]

    # знаходимо позицію останнього вхождення мови
    lang_i = []  # буде берегати індекси назв мов
    for i in range(len(middle_parts)):  # проходимо циклом по довжині списка
        for el in lang:  # умовно за допомогою цикла передаємо у el всі елементи списка lang
            if el in middle_parts[i]:   # якщо співпадіння буде знайдено, то тоді зберігаємо індекс цього ел у список, та прериваємо цей цикл
                lang_i.append(i)
                break
    if lang_i:  #
        index = lang_i[-1]  # змінній index присвоюється останній ел у списку
        project_name = ' '.join(middle_parts[:index]).strip()  # рядок з елементів(), з 1 елемента до останнього який знаходиться перед index
        project_language = ' '.join(middle_parts[index:]).strip()  # рядок з елементів(), починаючи з index до останнього ел списка
    else:
        print(f"Пропущено через невизначену назву мови: {line.strip()}")  # перевірка щоб додалося(для себе зробила)
        return None
    # тут все просто, підставляємо
    try:
        points = int(points_str)
        return {
            "Тип проекту": project_type,
            "Назва проекту": project_name,
            "Назва мови якою створено": project_language,
            "Кількість поінтів": points,
        }
    except ValueError:
        print(f"Пропущено {line.strip()}")
        return None


def insert_data(file_path: str, collection_name: str) -> None:
    """
    функція для вставки даних з файлу в колекцію MongoDB
    Args:
        filename (str): шлях до файла
        collection_name (str): ім'я колекції, для ставки даних
    Return:
        None
    """
    cl = pymongo.MongoClient("mongodb://localhost:27017/")
    db = cl["Mydatabase"]
    collection = db[collection_name]

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            project_data = file_processing(line)
            if project_data:
                collection.insert_one(project_data)


insert_data("Task_25.txt", "projects")
