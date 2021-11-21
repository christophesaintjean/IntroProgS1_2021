L = [2, -1, 5, 3, 4]

print(L[0], L[-5])
print(L[4], L[-1])

L[1] = 0
L[3] = L[2] + L[4]
print(L)    # "[2, 0, 5, 9, 4]"

aux = L[0]
L[0] = L[1]
L[1] = aux

print(L)

L[1], L[0] = L[0], L[1]

print(L)
# L[1], L[0] = L[:2]

L.remove(0)
print(L)
