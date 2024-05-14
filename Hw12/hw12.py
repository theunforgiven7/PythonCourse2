"""Вирішення задач за допомогою lambda виразів"""


#1.lambda-вираз, який перевіряє, чи є рядок паліндромом

check_palindrome = (
    lambda word: word.replace(' ', '').lower() == word.replace(' ', '').lower()[::-1]
)


word = "шалаш"
print(check_palindrome(word))

#2.lambda-вираз,
# який повертає список тільки з непарних елементів даного списку.

list1 = [1, 345, 322, 13, 66, 8345453, 0]
re_list = list(filter(lambda a: a % 2 != 0, list1))
print(re_list)

#3.lambda-вираз, який приймає список слів і повертає список слів,
# довжина яких менше або дорівнює середній довжині всіх слів в списку.

short_words = (
    lambda word_lst: [w for w in word_lst if len(w) <= sum(map(len, word_lst)) / len(word_lst)]
)
