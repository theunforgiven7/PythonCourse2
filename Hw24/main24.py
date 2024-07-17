import pymongo


def file_processing(line: str) -> dict:
    """
    Функція для обробки рядка з файлу
    Args:
        line (str): рядок з даними
    Returns:
        dict: сформованний словник
    """
    parts = line.strip().split('\t')
    project_type = parts[0]
    project_name = parts[1]
    project_language = parts[2]
    points_str = parts[3].rstrip('+')

    points = int(points_str)
    return {
            "Тип проекту": project_type,
            "Назва проекту": project_name,
            "Назва мови якою створено": project_language,
            "Кількість поінтів": points,
        }


def insert_data(file_path: str, collection_name: str) -> None:
    """
    функція для вставки даних з файлу в колекцію MongoDB
    Args:
        filename (str): шлях до файла
        collection_name (str): назва колекції, для ставки даних
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
# with open('task_25.txt', 'r', encoding='utf-8') as f:
#     a = f.read()
#     # print(a)
