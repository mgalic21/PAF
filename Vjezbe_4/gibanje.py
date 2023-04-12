import matplotlib.pyplot as plt
import particle as pp
import numpy as np


p1 = pp.Particle(100, 45, 2, 5)
p1.analiticki_domet()
p1.info()
p1.range()
p1.plot_trajcetory()


p2 = pp.Particle(10, 45, 0, 5)
p2.analiticki_domet()
p2.range()
p2.plot_trajcetory()
p1.info()
    