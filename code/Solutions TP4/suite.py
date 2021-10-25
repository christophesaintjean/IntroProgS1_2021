u0 = float(input("u0 ? "))
r = float(input("r  ? "))

while True:                        # Repeter jusqu'a
    n = int(input("n  ? "))
    if n >= 0:
        break

i = 0
u = u0
while i<n:
    print(u, end=" ")
    u = u + r
    i = i + 1