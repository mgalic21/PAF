import matplotlib.pyplot as plt
import numpy as np
import EM

E = (0, 0, 0)
B = (0, 0, 1)
v = (0.1, 0.1, 0.1)
s = (0, 0, 0)

p1 = EM.Particle(0.5, 1, E, B, v, s)
p2 = EM.Particle(0.5, -1, E, B, v, s)

p = p1.path(10)
e = p2.path(10)

graph = plt.axes(projection = "3d")
graph.view_init(23, 37)
graph.plot(p[:, 0], p[:, 1], p[:, 2], label = 'p+')
graph.plot(e[:, 0], e[:, 1], e[:, 2], label = 'e-')
graph.legend()
plt.show()