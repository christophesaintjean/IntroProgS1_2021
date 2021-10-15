n = 1
while n <= 5:
    print(n, end=" ")
    n = n + 1
print()

n = 2
while n <= 12:
    print(n, end=" ")
    n = n + 2
print()

n = 2
while n <= 12:
    if n % 2 == 0:
        print(n, end=" ")
    n = n + 1
print()

n = 3
while n <= 21:
    if n % 2 == 0:
        print(n, end=" ")
    n = n + 1
print()


cpt = 0
n = 130
while cpt < 10:
    if n % 5 == 0:
        print(n, end=" ")
        cpt = cpt + 1
    n = n - 1
    
