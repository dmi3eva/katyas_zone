from random import choice, randint
import pandas as pd

letters = ['i', 'h']
size = 40
rows = []
for i in range(size):
    first_size = randint(4, 14)
    second_size = randint(3, 10)
    first = ''.join([choice(letters) for _ in range(first_size)])
    second = ''.join([choice(letters) for _ in range(second_size)])
    label = 1 if abs(first_size - second_size) <= 3 else 0
    row = {
        'id': i,
        'message': f"{first} {second}",
        'label': label
    }
    rows.append(row)
df = pd.DataFrame(data=rows)
df.to_csv("communication_test.data", sep=',', index=False)