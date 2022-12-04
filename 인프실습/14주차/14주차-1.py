import numpy as np
a = np.arange(1, 4, 0.5)
print(f'a = {a}')
b = np.ones((6, 6))
print(f'b = {b}')
c = np.zeros((1, 6))
print(f'c = {c[0]}')
for i in range(6):
    c[0][i] = c[0][i] + 2 * (i + 1)
print(f'c = {c[0]}')
a = a * b
print(a)
for i in range(6):
    a[i] *= c[0][i]
print(a)
for i in range(6):
    print(f'a 배열의 {i+1}열 합 : {a.sum(axis = 0)[i]}')


