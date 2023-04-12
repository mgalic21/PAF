import matplotlib.pyplot as plt
import numpy as np

class Particle:
    
    def __init__(self, v0, kut, x0, y0, dt = 0.001):
        self.v0 = v0
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        self.dt = dt
        self.lista_x = []
        self.lista_y = []
    
    
    def info(self):
        print("V0: {} m/s .".format(self.v0))
        print("kut: {} °".format(self.kut))
        print("X0: {} m.".format(self.x0))
        print("Y0: {} m.".format(self.y0))
        
        
    def reset(self):
        self.v0 = 0
        self.kut = 0
        self.x0 = 0
        self.v0 = 0
        self.lista_y = []
        self.lista_x = []
    
        
    def __move(self, F, m, t):# rijesi sutra
        t0, g = 0, 9.81
        dt = 0.001
        
        kut_r = (self.kut / 180) * np.pi
        vx0 = self.v0 * np.cos(kut_r)
        vy0 = self.v0 * np.sin(kut_r)
        
        while t0 < t:
            self.x0 = self.x0 + vx0 * dt
            self.lista_x.append(self.x0)
            vy = vy0 - g * dt
            vy0 = vy
            
            self.y0 = self.y0 + vy * dt 
            self.lista_y.append(self.y0)
            t0 += dt
        
            
    def range(self):
        
        g, t = 9.81, 0
        
        kut_r = (self.kut / 180) * np.pi
        
        vx0 = self.v0 * np.cos(kut_r)
        vy = self.v0 * np.sin(kut_r)
        
        
        while self.y0 >= 0:
            
            self.x0 = self.x0 + vx0 * self.dt
            self.lista_x.append(self.x0)
            
            self.y0 = self.y0 + vy * self.dt 
            self.lista_y.append(self.y0)
            
            vy = vy - g * self.dt
            
            t += self.dt
            
        return self.lista_x[-1]
        self.y0 = 0
    
    
    def plot_trajcetory(self):
        
        plt.xlabel("x / m")
        plt.ylabel("y / m")
        plt.plot(self.lista_x, self.lista_y)
        plt.show()
   
        
    def analiticki_domet(self):
        
        domet = ((self.v0)**2 * np.sin(2 * ((self.kut / 180)*np.pi))) / 9.81
        return domet
        
