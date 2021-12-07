import turtle
from random import randint

def rect(l, h, x=0, y=0, color=(0,0,0)):
    # Sauvegarde l'etat de la tortue
    pen_state = turtle.isdown()
    pos_state = turtle.position()
    heading_state = turtle.heading()
    # Le tracé
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pencolor(*color)
    for _ in range(2):
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.penup()
    # restauration de l'etat de la tortue
    turtle.setposition(pos_state)
    turtle.setheading(heading_state)
    if pen_state:
        turtle.pendown()

def histo(L, l, x, y):
    for i, hi in enumerate(L):
        color =  randint(0, 255), randint(0, 255), randint(0, 255)
        rect(l, hi, x + l * i, y, color)



if __name__ == "__main__":
    turtle.setup(600, 600)
    turtle.colormode(255)

    """
    rect(50, 200, -200+50*0, -100)
    rect(50, 100, -200+50*1, -100)
    rect(50, 400, -200+50*2, -100)
    """
    L = [100, 50, 120, 12, -30, 60, 250, 100]
    histo(L, 20, -200, -100)
    turtle.exitonclick()