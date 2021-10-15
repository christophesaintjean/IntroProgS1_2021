x = float(input('x ? '))
y = float(input('y ? '))


cdist = x**2 + y*y <= 1

if x >= 0 and y >= 0 and cdist: 
    print(f"Le point de coordonnées ({x}, {y}) est dans le quart de disque.")
else:
    print(f"Le point de coordonnées ({x}, {y}) n'est pas dans le quart de disque.")