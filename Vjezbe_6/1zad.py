import matplotlib.pyplot as plt
import numpy as np
import harmonic_oscillator as HO

h1 = HO.HarmonicOscillator(1, 5, 1, 1, 0.01)
t, x, v, a = h1.move(5)

plt.subplot(1, 3, 1)
plt.title("x-t graph")
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.plot(t, x)

plt.subplot(1, 3, 2)
plt.title("v-t graph")
plt.xlabel("t[s]")
plt.ylabel("v[m/s]")
plt.plot(t, v)

plt.subplot(1, 3, 3)
plt.title("a-t graph")
plt.xlabel("t[s]")
plt.ylabel("a[m/s**2]")
plt.plot(t, a)

plt.show()


