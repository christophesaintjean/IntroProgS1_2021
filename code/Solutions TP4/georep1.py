import turtle

"""
turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)
"""

cpt = 0
while cpt < 4:
    turtle.forward(100)
    turtle.left(90)
    cpt = cpt + 1
turtle.exitonclick()