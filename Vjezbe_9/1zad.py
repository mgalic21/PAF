import matplotlib.pyplot as plt
import numpy as np
import system as sys

t = 365.242
ms = 1.989 * 10**30
mz = 5.9742 * 10**24
rz = (1.486*10**11, 0)
vz = (0, 29783)
rs = (0,0)
vs = (0,0)
S1 = sys.System(mz, ms, rz, rs, vz, vs, 1)

z, s = S1.interaction(t)
plt.plot(z[:, 0], z[:, 1], label = "zemlja", c = "b")
plt.plot(s[:, 0], s[:, 1],"o", label = "sunce", c = "y")
plt.legend()
plt.show()