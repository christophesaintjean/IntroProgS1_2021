import turtle
import math

n = int(input("Nombre de cotés ? "))
diametre = 300                      # petite modification de la valeur de cot pour s'assurer que le dessin reste dans la fenetre
cote = math.pi * diametre / n

for i in range(n):
    turtle.forward(cote)
    turtle.left(360/n)
turtle.exitonclick()