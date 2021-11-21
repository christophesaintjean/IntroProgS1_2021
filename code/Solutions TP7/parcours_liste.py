import random

R = []
for _ in range(10):
    alea = random.randint(1,20)
    R.append(alea)
print(R)

long = len(R)

for i in range(long):   # range(0, long)
    print(R[i], end= ": ")

print()    

for Ri in R:
    print(Ri, end= ": ")
   
print()

for _, Ri in enumerate(R):
    print(Ri, end= ": ")
    
print()

for i, _ in enumerate(R):
    print(R[i], end= ": ")
   
print()

somme = 0    
for Ri in R:
    somme = somme + Ri
print(f"Somme : {somme}")

i_max, max = 0, R[0]

for i, Ri in enumerate(R):
    if Ri > max:
        i_max = i
        max = R[i]
print(f"Le maximum {max} est en position {i_max}")

cpt = 0
for Ri in R:
    if Ri >= 10:
        cpt = cpt + 1
print(f"Le nombre d'élements supérieurs à 10 est {cpt}")

R2 = []
for Ri in R:
    if Ri <= 10:
        R2.append(Ri)
    else:
        R2.append(-Ri)
print(R2)

R3 = R + R2
print(R3)
