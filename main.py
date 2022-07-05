import numpy as np

# matr = np.array([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6])
# print(matr)

a = 6
b = 6
matr = [[x for x in range(a)] for d in range(b)]
c = np.array(matr)

print(c)
