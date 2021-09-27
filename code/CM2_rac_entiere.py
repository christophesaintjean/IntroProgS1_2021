#Racine carrée entière:
#  Etant donné un entier $n$, déterminer le plus grand nombre entier $r$
#  tel que $r^2 \leq n$.

import math

n = int(input("n ? "))

r = 0
while r*r <= n:
    r = r + 1
    
# on a donc r*r > n, on est allé trop loin
r = r - 1
print("La racine carrée entière de", n, "est", r)
print("C'est aussi int(math.sqrt(n))", int(math.sqrt(n)))
 