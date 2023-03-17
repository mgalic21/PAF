import matplotlib.pyplot as plt
import numpy as np

i = 0
while i == 0:
    # alfa_s - pocetni kut u stupnjevima
    alfa_s = int(input("pocetni kut: "))
    if  0 <= alfa_s and alfa_s <= 90:
        i += 1
    else:
        print("Upisi kut izmedu 0 i 90!")

# alfa_r - pocetni kut u radijanima
alfa_r = (alfa_s / 180) * np.pi

v0 = float(input("v0 (m/s): "))
# vx0 - jednoliko gibanje
vx0 = v0 * np.cos(alfa_r)
# jednoliko ubrzano gibanje (prema dolje)
vy0 = v0 * np.sin(alfa_r)

# pocetne koordinate tijela                   
x0 = 0
y0 = 0
y = 0
g = 9.81
dt = 0.001

#liste podataka
vremena = []
putanje_x = []
putanje_y = []

t = 0
while t <= 10:
    x = x0 + vx0 * dt
    putanje_x.append(x)
    x0 = x
    vy = vy0 - g * dt
    y = y0 + vy * dt
    vy0 = vy
    y0 = y
    putanje_y.append(y)
    vremena.append(t)
    t = t + dt
    
#crtanje grafa
plt.subplot(1, 3, 1)
plt.title("x - t graf")
plt.xlabel(" t / s")
plt.ylabel(" x / m")
plt.plot(vremena, putanje_x)

plt.subplot(1, 3, 2)
plt.title("y - t graf")
plt.xlabel(" t / s")
plt.ylabel(" y / m")
plt.plot(vremena, putanje_y)

plt.subplot(1, 3, 3)
plt.title("x - y graf")
plt.xlabel(" x / m")
plt.ylabel(" y / m")
plt.plot(putanje_x, putanje_y)

plt.show()