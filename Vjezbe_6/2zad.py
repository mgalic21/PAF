import matplotlib.pyplot as plt
import numpy as np
import harmonic_oscillator as HO

h1 = HO.HarmonicOscillator(1, 5, 1, 1, 0.05)
h2 = HO.HarmonicOscillator(1, 5, 1, 1, 0.02)
h3 = HO.HarmonicOscillator(1, 5, 1, 1, 0.01)

t1, x1, v1, a1 = h1.move(5)
t2, x2, v2, a2 = h2.move(5)
t, x = h3.analytical_graph(5)

plt.title("x-t graph")
plt.scatter(t1, x1, s = 2, c = "y")
plt.scatter(t2, x2, s = 2, c = "r")
plt.plot(t, x)
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.show()