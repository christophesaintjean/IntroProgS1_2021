a = float(input("a ?  "))

if a < 0:
    print(f"{a} à l'exterieur de [0,1]")
else:
    if a > 1:
        print(f"{a} à l'exterieur de [0,1]")
    else:
        print(f"{a} à l'intérieur de [0,1]")


if a < 0 or a > 1:
    print(f"{a} à l'exterieur de [0,1]")
else:
    print(f"{a} à l'intérieur de [0,1]")

