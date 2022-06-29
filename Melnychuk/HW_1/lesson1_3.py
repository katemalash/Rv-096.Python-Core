import turtle


#turtle.tracer(0, 0)
turtle.pensize(3)

turtle.begin_fill()
turtle.color('black', 'yellow')
for i in range(360):
    turtle.left(1)
    turtle.forward(2)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(40)
turtle.pendown()
turtle.left(90)

for i in range(30):
    turtle.right(1)
    turtle.forward(2)
def draw_small_line():
    turtle.left(90)
    turtle.forward(7)
    turtle.right(180)
    turtle.penup()
    turtle.forward(7)
    turtle.pendown()
    turtle.forward(7)
    turtle.penup()
    turtle.right(180)
    turtle.forward(7)
    turtle.left(90)
draw_small_line()
for i in range(30):
    turtle.left(1)
    turtle.forward(2)
turtle.pendown()
for i in range(30):
    turtle.left(1)
    turtle.forward(2)
draw_small_line()
for i in range(30):
    turtle.right(1)
    turtle.forward(2)

turtle.right(90)
turtle.forward(65)
turtle.left(90)
turtle.forward(40)

turtle.pendown()
turtle.begin_fill()
turtle.color('black', 'black')
for i in range(90):
    turtle.right(1)
    turtle.forward(0.3)
turtle.forward(15)
for i in range(180):
    turtle.right(1)
    turtle.forward(0.3)
turtle.forward(15)
for i in range(90):
    turtle.right(1)
    turtle.forward(0.3)
turtle.end_fill()

turtle.penup()
turtle.left(180)
turtle.forward(80)

turtle.pendown()
turtle.begin_fill()
turtle.color('black', 'black')
for i in range(90):
    turtle.left(1)
    turtle.forward(0.3)
turtle.forward(15)
for i in range(180):
    turtle.left(1)
    turtle.forward(0.3)
turtle.forward(15)
for i in range(90):
    turtle.left(1)
    turtle.forward(0.3)
turtle.end_fill()

turtle.exitonclick()
