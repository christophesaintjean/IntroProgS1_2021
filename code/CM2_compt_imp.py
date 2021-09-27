# Compter le nombre de entiers impairs entre 1 et 100 divisibles par 3 mais pas par 7.

n = 1
cpt = 0

while n <= 100:
    Cimpair = n % 2 == 1
    C3 = n % 3 == 0
    C7 = n % 7 == 0
    if Cimpair and (C3 and not C7):
        print('x', end='')
        cpt = cpt + 1
    else:
        print('-', end='')
    n = n + 1

print()
print(cpt)