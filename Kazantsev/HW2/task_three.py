import turtle

pen = turtle.Turtle()


def eye_draw(color, radius):

    for x in range(2):
        pen.down()
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(radius, 90)
        pen.circle(radius // 2, 90)
        pen.end_fill()
        pen.fillcolor(color)
        pen.up()


    #pen.down()
    #pen.fillcolor(color)
    #pen.begin_fill()
    #pen.circle(radius)
    #pen.end_fill()
    #pen.up()



# draw body
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

# draw eyes
pen.goto(-40, 120)
eye_draw('white', 15)
pen.goto(-37, 125)
eye_draw('black', 5)
pen.goto(40, 120)
eye_draw('white', 15)
pen.goto(40, 125)
eye_draw('black', 5)
pen.up()

# draw mouth
pen.goto(-70, 85)
pen.down()
pen.right(90)
pen.circle(70, 180)
pen.up()

pen.hideturtle()
turtle.mainloop()
