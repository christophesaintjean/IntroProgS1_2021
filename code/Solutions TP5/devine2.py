import math
import random


min, max = 1, 20

x = random.randint(min, max)

n = math.log2(max)
#      Il faut arrondir à l'entier supérieur
print(f"Je suis sûr de trouver en maximum de {int(n + 1)} coups !!")

print(f'Début du jeu [{min},{max}]')
print('-' * 19)
cpt = 0
while True:
    print(f'[{min},{max}]')
    p = (min + max) // 2
    r = print(f"Est ce {p} ? ")
    cpt = cpt + 1
    if p < x:
        min = p + 1
    elif x < p:
        max = p - 1
    else:
        print(f'J’ai trouvé {p} en {cpt} propositions.')
        break
