import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
    
    def __init__(self, mass, k, v0, x0, dt = 0.001):
        self.mass = mass
        self.k = k
        self.v0 = v0
        self.x0 = x0
        self.dt = dt
        self.lista_x = []
        self.lista_v = []
        self.lista_a = []
        self.lista_t = []
        
        
    def reset(self):
        self.mass = self.mass
        self.k = self.k
        self.v0 = 0
        self.x0 = 0
        self.dt = self.dt
        self.lista_x = []
        self.lista_v = []
        self.lista_a = []
        self.lista_t = []
        
        
    def printinfo(self):
        print("m = ", self.mass)
        print("k = ", self.k)
        print("v = ", self.v0)
        print("x = ", self.x0)
        
        
    def move(self, t):
        t0 = 0.0
        while t0 <= t:
            a = (-self.k / self.mass) * self.x0
            self.lista_a.append(a)
            self.v0 += a * self.dt
            self.lista_v.append(self.v0)
            self.x0 += self.v0 * self.dt
            self.lista_x.append(self.x0)
            self.lista_t.append(t0)
            t0 += self.dt
        return self.lista_t, self.lista_x, self.lista_v, self.lista_a
    
    
    def analytical_graph(self, t):
        t0 = 0.0
        time = np.arange(t0, t, self.dt)
        omega = np.sqrt(self.k / self.mass)
        A = np.sqrt(self.x0**2 + (self.v0 / omega)**2)
        if self.x0 == 0:
            if self.v0 > 0:
                phi = 0.5 * np.pi
            else:
                phi = -0.5 * np.pi
        else:
            phi = np.arctan(-self.v0 / (omega * self.x0))
        x = A * np.cos(omega * time + phi)
        return time, x
    
    