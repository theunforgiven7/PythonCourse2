#### 1

as1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(*[i for i in as1 if i < 5]) # * розпаковує list

#### 2

as2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([i for i in as2 if i in ba])

#### 3

arr = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]

bar = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

print(list(set(arr) ^ set(bar)))