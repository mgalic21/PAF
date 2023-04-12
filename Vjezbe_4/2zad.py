import matplotlib.pyplot as plt
import numpy as np
import particle as pp

t = 0.0001
lista_t = []
numericka_rjesenja = []
while t < 0.1:
    p1 = pp.Particle(100, 45, 2, 5, t)
    numericka_rjesenja.append(np.abs(p1.range()-p1.analiticki_domet())/p1.analiticki_domet()*100)
    t += 0.0001
    lista_t.append(t)


plt.plot(lista_t,numericka_rjesenja)
plt.show()
