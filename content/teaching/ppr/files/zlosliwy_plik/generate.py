#!/usr/bin/env python
import random
import string

random.seed(6)
population = string.ascii_letters + string.digits + '\t\n "\','
sep = '|'
for i in range(50000):
    row = []
    for j in range(10):
        row.append(''.join(random.choices(population, k=random.randint(1, 8))))
    print(sep.join(row))
