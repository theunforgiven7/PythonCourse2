#№1


word = input('Введи слово:')
word = word.lower()
word = word.replace(' ', '')
reversed_w = word[::-1]
if word == reversed_w:
    print(f'{word} - Це паліндром')

else:
    print(f"{word} - це не паліндром")

