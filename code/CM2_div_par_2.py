# Combien de fois peut on diviser un nombre par deux ?

n = int(input('n ? '))

cpt = 0
while n > 0:
    n = n // 2
    print(n)
    cpt = cpt + 1
print('Compteur', cpt)
