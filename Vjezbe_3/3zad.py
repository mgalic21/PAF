import numpy as np

lista_x = [1, 1.005, 1.01, 1.016, 1.022, 1.029, 1.033, 1.036, 1.043, 1.045]
lista_y = [2, 2.103, 2.204, 2.21, 2.47, 2.491, 2.5432, 2.574, 2.619, 2.677]


print(np.mean(lista_x))
print(np.mean(lista_y))
print(np.std(lista_x)/ np.sqrt(len(lista_x)-1))
print(np.std(lista_y)/ np.sqrt(len(lista_y)-1))
