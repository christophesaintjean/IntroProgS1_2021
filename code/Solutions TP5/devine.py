import math

min = 1
max = 20

# (((max /2) /2) / 2) .... / 2 = max / 2 ** n
# arret si (max / 2 ** n) = 1
#      <=> max = 2 ** n
#      <=> ln(max) = n * ln(2)
#      <=> n = ln(max) / ln(2) =: log2(max)
n = math.log2(max)
#      Il faut arrondir à l'entier supérieur
print(f"Je suis sûr de trouver en maximum de {int(n + 1)} coups !!")

print(f'Début du jeu [{min},{max}]')
print('-' * 19)
cpt = 0
while True:
    print(f'[{min},{max}]')
    p = (min + max) // 2
    r = input(f"Est ce {p} ? ")
    cpt = cpt + 1
    if r == '+':
        min = p + 1
    elif r == '-':
        max = p - 1
    elif r == '=':
        print(f'J’ai trouvé {p} en {cpt} propositions.')
        break
    else:
        cpt = cpt - 1  # Erreur de saisie on ne compte pas
    if min > max:
        print("J'arrête, je ne joue pas avec un tricheur")
        break