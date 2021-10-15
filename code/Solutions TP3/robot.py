import turtle


pasfini = True

while pasfini:
    ordre = input("Entrez un ordre : ")
    if ordre == "A" or ordre == "a":
        print("Le robot avance de 100 pixels")
        turtle.forward(100)
    elif ordre == "R" or ordre == "r":
        print("Le robot recule de 100 pixels")
        turtle.backward(100)
    elif ordre == "G" or ordre == "g":
        print("Le robot tourne à gauche de 90 degrés.")
        turtle.left(90)
    elif ordre == "D" or ordre == "d":
        print("Le robot tourne à droite de 90 degrés.")
        turtle.right(90)
    elif ordre == "Q" or ordre == "q":
        pasfini = False
    else:
        print(f"Le robot ne comprend pas {ordre}")
else:
    print("Fin des instructions")

turtle.exitonclick()