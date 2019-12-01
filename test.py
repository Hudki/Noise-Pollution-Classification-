import csv


with open('people.csv', 'r') as f:
    y = ' '.join(reversed(list(csv.reader(f))[-1]))
    print(y)
