import matplotlib.pyplot as plt
import calculus as cal
import numpy as np

def f0():
    x = np.linspace(-2, 2, 1000)
    y = 3*x**2
    plt.plot(x, y)
    
def f1(x):
    return x**3

def f2(x):
    return np.cos(x)

vrijednost = cal.value(f1, 5)
print(vrijednost)

points, change = cal.rate_of_change(f1, -2, 2, 0.01, 2)
points_2, change_2 = cal.rate_of_change(f1, -2, 2, 0.1, 2)

plt.scatter(points, change, s = 2, c = "orange" )
plt.scatter(points_2, change_2 , s = 2, c = "blue" )
f0()
plt.show()