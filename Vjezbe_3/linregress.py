import matplotlib.pyplot as plt
import numpy as np

# M = D * fi ---> D = M/FI
M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #Nm
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #rad

#aritmeticka sredina
suma_M = sum(M)     # y podaci
suma_fi = sum(fi)   # x podaci

as_M = suma_M / len(M)
as_fi = suma_fi / len(fi)
    
D = (as_M * as_fi) / (as_fi * as_fi) # a = xy-- / x**2--

y = 0
x = min(fi)
dx = 0.01
lista_x = []
lista_y = []

while x <= max(fi):
    y = D * x
    lista_x.append(x)
    lista_y.append(y)
    x += dx

lista_tocaka = []
for i in range(len(M)):
    a = "({} , {})".format(fi[i], M[i])
    lista_tocaka.append(a)
    
sigma_D = np.sqrt((1/len(M)) * ( ((as_M * as_M) / (as_fi * as_fi)) - D**2 ))

print(lista_tocaka)

plt.scatter(fi, M, color = "black")
plt.xlabel("\u03C6"" / [rad]")
plt.ylabel("M / [Nm]")
plt.plot(lista_x, lista_y, color = "yellow")
plt.title("D = {} ± {}".format(round(D, 9), round(sigma_D, 9)))
plt.show()

# y = ax + b ; b = 0
# a = xy-- / x**2--
# sigma_a = korijen(1/n * ((y**2--  /  x**2--) - a**2 )) --- ovo prodi na vjezbama