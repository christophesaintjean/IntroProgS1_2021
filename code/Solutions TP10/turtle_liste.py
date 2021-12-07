import turtle

def rect(h, l, x=0, y=0):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)

def histo(L, l, x, y):
    for i, hi in enumerate(L):
        rect(hi, l, x + i * l, y)



if __name__ == "__main__":
    turtle.setup(600, 600)
    """
    rect(200, 50, 0 + 0*50, 10)
    rect(300, 50, 0 + 1*50, 10)
    rect(50 , 50, 0 + 2*50, 10)
    rect(-30, 50, 0 + 3*50, 10)
    """
    L = [100, 50, 120, 12, -30, 60, 250, 100]
    histo(L, 50, -200, -100)
    turtle.exitonclick()