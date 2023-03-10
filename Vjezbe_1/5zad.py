import matplotlib.pyplot as plt
import numpy as np

def pravac(a, b, c, d):
    
    k = (d - b) / (c - a)
    l = ( (d - b) / (c - a) ) * ( -a ) + b
    
    print("Dvije odabrane tocke su: ({},{}) i ({},{})".format(a, b, c, d))
    print("Jednadzba pravca iznosi: y = {} x + {}".format(k, l))
    
    aps = [a, c]
    ordi = [b, d]
    ime_grafa = input("Unesi ime grafa: ")
    print(aps)
    print(ordi)
    
    plt.ylabel("y os")
    plt.xlabel("x os")
    plt.title(ime_grafa)
    
    prikaz_podatka = input("Unesi s za saveat, a p za prikaz: ")
    
    if prikaz_podatka == "s":
        ime_= input("Unesi ime datoteke slike: ")
        ime_ += ".pdf"
        plt.plot(aps, ordi)
        plt.savefig(ime_)
    
    elif prikaz_podatka == "p":
        plt.plot(aps, ordi)
        plt.show()
    
    else:
        print("Greška pri unosu prikaza podatka.")
        
pravac(10, 2, 6, 4)