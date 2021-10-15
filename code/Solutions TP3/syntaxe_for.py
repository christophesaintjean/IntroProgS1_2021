"""
n = 1
while n < 6:
    print(n, end=" ")
    n = n + 1
print()
"""
for n in range(1, 6):
    print(n, end=" ")
print()

a = int(input("a ? "))
b = int(input("b ? "))
prod = 0
if a <= b:
    for i in range(a):
        prod = prod + b
else:
    for i in range(b):
        prod = prod + a
    
print(f"{a} * {b} = {a*b} vs {prod}")


