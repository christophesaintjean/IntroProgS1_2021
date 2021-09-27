# Compter le nombre de entiers impairs entre 1 et 1000 divisibles par 3 mais pas par 7.

cpt = 0

for n in range(1, 101):
    Cimpair = n % 2 == 1
    C3 = n % 3 == 0
    C7 = n % 7 == 0
    if Cimpair and (C3 and not C7):
        print('x', end='')
        cpt = cpt + 1
    else:
        print('-', end='')

print()
print(cpt)
