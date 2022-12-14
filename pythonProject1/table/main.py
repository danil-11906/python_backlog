import numpy as np
from numpy import linalg

a = """1;0;1000000000;500000000;500000;250000000;150000000;0;0;0;0;50000000;250000000
2;200000000;0;100000000;1000000;150000000;100000000;0;0;0;0;200000000;10000000000
3;0;0;0;0;0;0;0;0;0;0;0;300000
4;0;0;700000;0;0;0;0;0;0;0;0;1890000
5;0;0;0;0;0;0;0;0;0;40000000;0;22600000
6;0;0;0;0;0;0;0;0;0;0;0;670000000
7;0;0;0;0;4200000;10000000;0;0;200000000;0;3000000;1600000000
8;0;0;0;0;0;10000000000;0;1000000;0;0;0;100000
9;0;0;0;0;3000000;100000000;0;0;0;0;200000;200000000
10;0;0;0;0;0;0;0;0;0;0;0;600000000
11;0;0;0;0;0;0;0;0;0;0;0;315000000""".strip().split('\n')

y = [[250000000], [10000000000], [300000], [1890000 * 2], [22600000 * 3], [67000000], [10000000], [100000],
         [3000000], [600000000], [315000000 * 2]]

table = []
for i in a:
    arr = list(map(int, i.split(';')[1:]))
    row = []
    print(sum(arr))

    for j in arr:
        j = int(j)
        row.append(round(j / sum(arr), 2))
    table.append(row)

print(table)

new_table = []
for idx, i in enumerate(table):
    new_table.append(table[idx][:-1])

one = np.eye(len(new_table[0]))

new_table = np.matrix(new_table)
res = one - new_table
invert = linalg.inv(res)
y = np.matrix(y)

final = invert * y
print('\n')
print(final)
