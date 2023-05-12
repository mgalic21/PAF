import matplotlib.pyplot as plt
import numpy as np
import projectile as pr



dt = [0.01, 0.02, 0.05]
for i in dt:
    p1 = pr.Projectile(1, 10, 0, 0, 45, 0.5, 0.5, 0.5, i)
    a, b = p1.Euler()
    plt.scatter(a, b, s = 1, label = "Euler{}".format(i))
p2 = pr.Projectile(1, 10, 0, 0, 45, 0.5, 0.5, 0.5, 0.01)
x,y = p2.Runge_Kutta()
plt.plot(x, y, c = "black", label = "Runge-Kutta{}".format(0.01))
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()