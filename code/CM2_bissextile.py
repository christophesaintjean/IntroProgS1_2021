année = int(input("Année ? "))

# si l'année est divisible par 4 et non divisible par 100, ou
# si l'année est divisible par 400.

C4 = année % 4 == 0
C100 = année % 100 == 0
C400 = année % 400 == 0

bissextile = (C4 and not C100) or C400

if bissextile:
    print("l'année", année, "est bissextile")
else:
    print("l'année", année, "n'est pas bissextile")

