import matplotlib.pyplot as plt
import numpy as np
import calculus as cal

def f1(x):
    return 2*(x**2) + 3

high_values, low_values, steps, avg_values = [] , [] , [] , []

for i in range(100, 1100, 50):
    low_value, high_value, avg_val = cal.trapez(f1, 0, 1, i)
    steps.append(i)
    low_values.append(low_value)
    high_values.append(high_value)
    avg_values.append(avg_val)
    
plt.scatter(steps, high_values, s = 20, c = "blue" )
plt.scatter(steps, low_values, s = 20, c = "blue"  )
plt.scatter(steps, avg_values, s = 20, c = "orange")
plt.plot(steps, avg_values , c = "black")
plt.show()
