import matplotlib.pyplot as plt
import numpy as np

m = float(input("Unesi masu(kg): "))
F = float(input("Unesi silu(N) : "))
a = F / m # F = m*a

# liste gdje se spremaju podaci
vremena = []
putevi = []
brzine = []
akceleracije = []

# pocetni podaci 
t = 0 
v = 0
s = 0
t0 = 0.01 

while t <= 10:
    s = s + v * t0
    v = v + a*t0
    vremena.append(t)
    putevi.append(s)
    brzine.append(v)
    akceleracije.append(a)
    t = t + t0
    
#crtanje grafa
plt.subplot(1, 3, 1)
plt.title("x - t graf")
plt.xlabel("t / s")
plt.ylabel("x / m")
plt.plot(vremena, putevi)

plt.subplot(1, 3, 2)
plt.title("v - t graf")
plt.xlabel("t / s")
plt.ylabel("v / (m/s)")
plt.plot(vremena, brzine)

plt.subplot(1, 3, 3)
plt.title("a - t graf")
plt.xlabel("t / s")
plt.ylabel("a / (m/s^2)")
plt.plot(vremena, akceleracije)

plt.show()