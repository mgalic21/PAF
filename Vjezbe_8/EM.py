import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, mass, q, E, B, v0, s0, dt = 0.01):
        self.mass = mass
        self.q = q
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)  #koordinate pocetne brzine
        self.s0 = np.array(s0)  #koordinate pocetne tocke
        self.s = []
        self.dt = dt
        
    def path(self, t):
        t0 = 0.0
        while t0 <= t:
            a = (self.q / self.mass)*(self.E + (np.cross(self.v0, self.B)))
            self.v0 = self.v0 + (a * self.dt)
            self.s0 = self.s0 + (self.v0 * self.dt)
            self.s.append(self.s0)
            t0 += self.dt
        return np.array(self.s)