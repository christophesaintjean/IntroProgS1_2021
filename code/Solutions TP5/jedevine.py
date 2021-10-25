import random

min = 1
max = 20
alea = random.randint(min, max)


print(f'Début du jeu [{min},{max}]')
print('-' * 19)
while True:
    n = int(input("Propose un nombre: "))
    if alea > n:
        print('Plus grand.')
    elif alea <n:
        print('Plus petit.')
    else:
        print(f'Bravo, j’avais choisi {alea}.')
        break