from time import perf_counter
n = 97

# n (= 97) est il premier ?
for i in range(2, n):
    if n % i == 0:
        print(f"{n} n'est pas premier : {i} > 1 le divise")
        break
else:
    print(f"{n} est premier")

# Transformation en fonction
def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = 10000
print("*" * 5 + " Stratégie 1 " + "*" * 5)
start = perf_counter()
P = []
for n in range(2, N + 1):  # les nombres pour lesquels on va tester la primalité
    for i in range(2, n):
        if n % i == 0:
            break        # n divise i, on quitte la boucle sur i
    else:
        P.append(n)
print(perf_counter() - start)
print(f"Il y a {len(P)} nombres premiers inférieurs à {N}")
print(P)

print("*" * 5 + " Stratégie 2 " + "*" * 5)
start = perf_counter()
P = []
for n in range(2, N + 1):  # les nombres pour lesquels on va tester la primalité
    for i in P:       # La seule difference est ici !
        if n % i == 0:
            break
    else:
        P.append(n)
print(f"Il y a {len(P)} nombres premiers entre 2 et {N}")
print(perf_counter() - start)  # Cela marche bien mieux

print("*" * 5 + " Stratégie 3 " + "*" * 5)
start = perf_counter()
L = []
for i in range(2, N + 1):
    L.append(i)

P = []
while L:  # L n'est pas vide
    p = L[0]
    P.append(p)
    L2 = []
    for Li in L:
        if Li % p != 0:     ### on garde que ceux qui ne sont pas multiples de p
            L2.append(Li)
    L = L2
print(perf_counter() - start)  # C'est moins rapide
print(f"Il y a {len(P)} nombres premiers entre 2 et {N}")


