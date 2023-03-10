
    
i = 0
j = 0
k = 0
l = 0
while i == 0:
    try:
        x1 = int(input("Unesi x komponentu 1. tocke: "))
        i += 1
    except:
        print("Niste unijeli valjani podatak.")
while j == 0:
    try:
        y1 = int(input("Unesi y komponentu 1. tocke: "))
        j += 1
    except:
        print("Niste unijeli valjani podatak.")       
while k == 0:
    try:
        x2 = int(input("Unesi x komponentu 2. tocke: "))
        k += 1
    except:
        print("Niste unijeli valjani podatak.")      
while l == 0:
    try:
        y2 = int(input("Unesi y komponentu 2. tocke: "))
        l += 1
    except:
        print("Niste unijeli valjani podatak.")
        
k = (y2-y1) / (x2-x1)    
l = ( (y2-y1) / (x2-x1) ) * (-x1) + y1
print("Dvije odabrane tocke su: ({},{}) , ({},{})".format(x1, y1, x2, y2))
print("Jednadzba pravca iznosi: y = {} x + {}".format(k, l))
