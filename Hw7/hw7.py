# vowels = 'aeiou'
# consonants = 'bcdfghjklmnpqrstvwxyz'

def process_datesearch_text(your_file):
    vowels = 'aaeiouyаеёиоуыэюя'
    consonants = 'bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ'

    with open(f'{your_file}', 'r', encoding='utf-8') as file:
        text = file.read().lower()

    vowel_counts = {vowel: text.count(vowel) for vowel in vowels}
    consonant_counts = {consonant: text.count(consonant) for consonant in consonants}

    sum_vowels = sum(vowel_counts.values())
    sum_consonants = sum(consonant_counts.values())
    print(f'Сумарна кількість голосних літер - {sum_vowels} ')
    print(f'Сумарна кількість приголосних літер - {sum_consonants}')

    if sum_vowels > sum_consonants:
        most_popular_vowels = []
        for i in range(3):
            max_vowel = max(vowel_counts, key=vowel_counts.get)
            most_popular_vowels.append((max_vowel, vowel_counts[max_vowel]))
            del vowel_counts[max_vowel]
        result = 'Найпопулярніші голосні літери - ' + ', '.join([f'{char}: {count}' for char, count in most_popular_vowels])
    else:
        most_popular_consonant = None
        max_count = 0
        for b, count in consonant_counts.items():
            if count > max_count:
                most_popular_consonant = (b, count)
                max_count = count
        result = 'Найпопулярніша приголосна літера - ' + f'{most_popular_consonant[0]}: {most_popular_consonant[1]}'

    with open('Hw7/output.txt', 'w', encoding='utf-8') as file:
        file.write(result)
        
    return  result


print(process_datesearch_text('Hw7/input_8.txt'))
