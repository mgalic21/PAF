def pravac(a, b, c, d):
    
    k = (d - b) / (c - a)
    l = ( (d - b) / (c - a) ) * ( -a ) + b
    print("Dvije odabrane tocke su: ({},{}) i ({},{})".format(a, b, c, d))
    print("Jednadzba pravca iznosi: y = {} x + {}".format(k, l))
    
pravac(3, 4, 7, 1)