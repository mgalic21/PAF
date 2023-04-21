import matplotlib.pyplot as plt
import numpy as np

def value(func, x, dx = 0.001 , step = 3):
    
    if step == 2:
        return ((func(x + dx) - func(x)) / (dx))
    else:
        return (( func(x + dx) - func(x - dx) ) / (2 * dx) )


def rate_of_change(func, lowest, highest, dx = 0.001, step = 3):
    
    list_of_points, list_of_rof, list_of_rof2 = [] , [] , []

    while lowest <= highest:    
        list_of_points.append(lowest)
        list_of_rof.append((( func(lowest + dx) - func(lowest - dx) ) / (2 * dx)))
        list_of_rof2.append(((func(lowest + dx) - func(lowest)) / (dx)))
        lowest = lowest + dx
        
    if step == 2:
        i = 0
        while i < len(list_of_points):
            print(list_of_points[i] , list_of_rof2[i])
            i += 1
        return list_of_points, list_of_rof2
    
    else:
        j = 0
        while j < len(list_of_points):
            print(list_of_points[i], list_of_rof[i])
            j += 1
        return list_of_points, list_of_rof


def integral(func,low, high, dx = 0.001):
    list_of_points, low_values = [] , []
    list_of_points2, high_values = [] , []
    lowest_value, highest_value = 0, 0
    
    while low <= high:
        
        list_of_points.append(low)
        lowest_value += func(low) * dx
        low_values.append(lowest_value)
        
        low += dx
        
        list_of_points2.append(low)
        highest_value += func(low) * dx
        high_values.append(highest_value)
        
    return list_of_points , low_values, list_of_points2, high_values


def trapez(func, a, b, N):
    
    dx = (b-a) / N
    
    i, donja, gornja, avg = 0, 0, 0, 0
    
    while i < N:
        
        donja += func(a) * dx
        gornja += func(a + dx) *dx
        a += dx
        avg += (dx / 2) * (func(a-dx) + func(a))
        i += 1
        
    return donja, gornja, avg