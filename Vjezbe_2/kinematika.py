import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(F, m, tuk):
    t = 0 
    v = 0
    s = 0
    dt = 0.01 
    
    a = F / m # F = m*a

    # liste gdje se spremaju podaci
    vremena = []
    putevi = []
    brzine = []
    akceleracije = []
    
    while t <= tuk:
        s = s + v * dt
        v = v + a*dt
        vremena.append(t)
        putevi.append(s)
        brzine.append(v)
        akceleracije.append(a)
        t = t + dt
    
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
  
    
    
def kosi_hitac(v0, alfa_s, tuk):

    # alfa_r - pocetni kut u radijanima
    alfa_r = (alfa_s / 180) * np.pi
    
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
    while t <= tuk:
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
    