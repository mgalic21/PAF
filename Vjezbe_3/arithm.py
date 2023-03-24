import numpy as np
import matplotlib.pyplot as plt

x = [3, 4, 5, 5, 4, 3, 4, 5, 4, 4]
y = [3, 2, 1, 1, 2, 3, 2, 1 ,2, 2]

def aritmeticka_sredina(x, y):
    
    suma_x = sum(x)
    suma_y = sum(y)
    
    #aritmetička sredina x i i y komponenti točaka
    as_x = suma_x / len(x)
    as_y = suma_y / len(y)

    print(as_x, as_y)
    

def devijacija(x, y):

    suma_x = sum(x)
    suma_y = sum(y)
    
    as_x = suma_x / len(x)
    as_y = suma_y / len(y)
    
    #izračunavanje sume u formuli devijacije
    dev_x = 0
    dev_y = 0
    for i in range(len(x)):
        dev_x += (float(x[i] - as_x)**2)
        dev_y += (float(y[i] - as_y)**2)
        
    sigma_x = np.sqrt(dev_x / (len(x) *(len(x) - 1)))
    sigma_y = np.sqrt(dev_y / (len(y) *(len(y) - 1)))    

    print(sigma_x, sigma_y)
    
aritmeticka_sredina(x, y)
devijacija(x, y)