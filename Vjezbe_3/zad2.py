def iteracija(N):
    br = 5
    i = 0
    while i < N:
        br += 1/3
        i += 1
    j = 0
    while j < N:
        br -= 1/3
        j += 1
    print(br)
    
iteracija(200)
iteracija(2000)
iteracija(20000)

# sto je veca iteracija, veca je pogreska
# greska se javlja zbog prebacivanja u binarni sustav