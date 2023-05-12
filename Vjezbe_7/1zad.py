import matplotlib.pyplot as plt
import numpy as np
import projectile as pr

dt = [0.01, 0.02, 0.05]
for i in dt:
    p1 = pr.Projectile(1, 10, 0, 0, 45, 0.5, 0.5, 0.5, i)
    a, b = p1.Euler()
    plt.plot(a, b,  label = "Euler{}".format(i))
plt.xlabel("x[]")
plt.ylabel("y[m]")
plt.legend()
plt.show()