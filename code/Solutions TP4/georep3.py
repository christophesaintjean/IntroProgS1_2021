import turtle
import math

k = int(input("k ? "))

for m in range(179, 90, -1):
    if 360* k % m == 0:
        break
else:
    print("m n'est pas trouvé")
    
#print(turtle.xcor(), turtle.ycor())

while True:
    turtle.forward(100)
    turtle.right(m)
    #print(turtle.xcor(), turtle.ycor())
    cond_x_0 = math.isclose(turtle.xcor(), 0, abs_tol=1e-8)
    cond_y_0 = math.isclose(turtle.ycor(), 0, abs_tol=1e-8)
    if cond_x_0 and cond_y_0:
        break
    
turtle.exitonclick()