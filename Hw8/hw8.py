
def date_search_text(FilePath):
    """
    This function reads a text file, finds the shortest and most used words
    and replaces all occurrences of this word in the text with
    its uppercase version. The updated text is then written back to the file
    Args:
        FilePath: The path to the text file.
    Returns:
        str: return the shortest word that used most often in the text.
    """

    with open(FilePath, 'r+', encoding='utf-8') as file:
        text = file.read().split()

        lower_text = [word.lower() for word in text]
        word_count = {word: lower_text.count(word) for word in lower_text}

        max_word_count = max(word_count.values())
        most_popular_word = [word for word, count in word_count.items() if count == max_word_count]

        min_popular_word = min(most_popular_word, key=len)
        Upper_min_popular_word = min_popular_word.upper()

        file.seek(0)
        updated_content = [i if i.lower() != min_popular_word else Upper_min_popular_word for i in text]
        file.truncate(0)
        file.write(' '.join(updated_content))

        return (f'"{min_popular_word}" - This is the shortest word that used most often in the text.')


print(date_search_text('Hw8/Input_1.txt'))
