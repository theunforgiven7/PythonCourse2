import json
import csv





factory = {
    'It department': 38,
    'Sales dep': 20,
    'Prodaction dep': 90,
    'Law dep': 5,
    'Construction dep': 69
}

# a)
factory['Law dep'] = 15

# b)
factory['New dep'] = 88

# c)
del factory['Law dep']

#w JSON
with open('Hw9/factory.json', 'w') as f:
    json.dump(factory, f)

# w CSV
with open('Hw9/factory.csv', 'w') as f:
    writer = csv.writer(f)
    for key, value in factory.items():
        writer.writerow([key, value])

# r JSON
with open('Hw9/factory.json', 'r') as f:
    data_json = json.load(f)

# r CSV
csv_d = {}
with open('Hw9/factory.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        csv_d[row[0]] = int(row[1])

# d)
total_worker = sum(data_json.values())
print(f'Загальна кількість співробітників у компанії: {total_worker}')
