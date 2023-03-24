a = 5.0
b = 4.935
print(a-b)
# ocekujemo rezultat: 0.065
# dobili smo rezultat: 0.06500000000000039
# python aproksimira a i b i rezultat (aproksimacija nije dobra)

c = 0.1
d = 0.2
e = 0.3
f = 0.6

g = c + d + e

if g == f:
    print("Isti su.")
else:
    print("Nisu isti.")
print(g)

# python krivo aproksimira rezultat 
# samo razlomke oblika " 1/(2**n) " možemo zapisati u konačnoj binarnoj formi. Sve ostalo su aproksimacije
# python za float rezervira 64 bita, te zbog toga dosta neki brojevi imaju identičan zapis u memoriji