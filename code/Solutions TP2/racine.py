import math

x = float(input("x ? "))

if x >= 0:
    print(f"Racine de {x} : {math.sqrt(x)}")
else:
    print(f"Impossible de calculer la racine de {x}")
    
